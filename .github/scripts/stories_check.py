#!/usr/bin/env python3
"""Prüft User Stories und gibt einen Markdown-Bericht aus."""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STORIES_PATH = ROOT / "stories" / "Kartenverwaltung_User_Stories.md"
GLOSSARY_PATH = ROOT / "quellen" / "Glossar.md"
PROTOTYPE_PATH = ROOT / "index.html"


@dataclass(frozen=True)
class Finding:
    level: str
    location: str
    message: str


@dataclass(frozen=True)
class Story:
    story_id: str
    title: str
    text: str
    line: int


def parse_stories(text: str) -> list[Story]:
    headings = list(
        re.finditer(r"(?m)^##[ \t]+(US-\d+)[ \t]+([^\n]+?)[ \t]*$", text)
    )
    stories: list[Story] = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        stories.append(
            Story(
                story_id=heading.group(1),
                title=heading.group(2).strip(),
                text=text[heading.end() : end],
                line=text.count("\n", 0, heading.start()) + 1,
            )
        )
    return stories


def parse_forbidden_terms(glossary: str) -> list[tuple[str, re.Pattern[str]]]:
    terms: list[tuple[str, re.Pattern[str]]] = []
    for line in glossary.splitlines():
        if not line.startswith("|"):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        if len(columns) < 3 or columns[0] == "Begriff":
            continue
        if all(column and set(column) <= {"-", ":"} for column in columns):
            continue
        for raw_term in columns[2].split(","):
            term = raw_term.strip().strip("*`")
            if not term or term in {"–", "-"}:
                continue
            if term == "PIN (ohne Zusatz)":
                pattern = re.compile(r"(?<![\w-])PIN(?![\w-])", re.IGNORECASE)
                term = "PIN"
            else:
                expression = r"\s+".join(re.escape(part) for part in term.split())
                pattern = re.compile(rf"(?<!\w){expression}(?!\w)", re.IGNORECASE)
            terms.append((term, pattern))
    return terms


def field_value(text: str, name: str) -> str | None:
    match = re.search(
        rf"(?m)^\*\*{re.escape(name)}:\*\*[ \t]*(.*?)[ \t]*$", text
    )
    return match.group(1).strip() if match else None


def criteria_text(text: str) -> str | None:
    heading = re.search(r"(?m)^\*\*Akzeptanzkriterien\*\*\s*$", text)
    if not heading:
        return None
    following_heading = re.search(
        r"(?m)^(?:\*\*[^*\n].*?\*\*|---)\s*$", text[heading.end() :]
    )
    end = heading.end() + following_heading.start() if following_heading else len(text)
    return text[heading.end() : end].strip()


def finding_line(story: Story, content: str, offset: int) -> str:
    line = story.line + content.count("\n", 0, offset)
    return f"stories/Kartenverwaltung_User_Stories.md:{line}"


def check_content(
    stories_text: str,
    glossary_text: str,
    prototype_text: str | None = None,
) -> list[Finding]:
    findings: list[Finding] = []
    stories = parse_stories(stories_text)
    if not stories:
        return [
            Finding(
                "Alarm",
                "stories/Kartenverwaltung_User_Stories.md:1",
                "Keine Story-Abschnitte mit US-Kennung gefunden.",
            )
        ]

    criteria_by_story: dict[str, set[str]] = {}
    forbidden_terms = parse_forbidden_terms(glossary_text)
    vague_terms = ("zeitnah", "schnell", "einfach", "sicher")

    for story in stories:
        location = f"stories/Kartenverwaltung_User_Stories.md:{story.line}"
        story_text = field_value(story.text, "Story") or ""
        source = field_value(story.text, "Quelle")
        criteria = criteria_text(story.text)
        criteria_section_exists = criteria is not None

        if not re.search(r"\bAls\s+.+?\s+möchte\s+ich\b", story_text, re.IGNORECASE):
            findings.append(
                Finding(
                    "Alarm",
                    location,
                    f"{story.story_id}: Story ohne Rolle im Format „Als … möchte ich“.",
                )
            )
        if not source:
            findings.append(Finding("Alarm", location, f"{story.story_id}: Quelle fehlt."))
        if criteria is None:
            findings.append(
                Finding("Alarm", location, f"{story.story_id}: Akzeptanzkriterien fehlen.")
            )
            criteria = ""
            criterion_matches: list[tuple[str, str]] = []
        else:
            criterion_matches = re.findall(
                r"(?m)^\s*(?:[-*]\s*)?(AK\d+)\s*:\s*(\S.*)$", criteria
            )
        if not criterion_matches and criteria_section_exists:
            placeholder = re.fullmatch(
                r"\s*(?:[-*]\s*)?noch offen\s*", criteria, re.IGNORECASE
            )
            if not placeholder:
                findings.append(
                    Finding(
                        "Alarm",
                        location,
                        f"{story.story_id}: Akzeptanzkriterien fehlen (außer „noch offen“).",
                    )
                )

        criterion_ids = {criterion_id for criterion_id, _ in criterion_matches}
        criteria_by_story[story.story_id] = criterion_ids

        content = f"{story.title}\n{story.text}\n{criteria}"
        for term in vague_terms:
            match = re.search(rf"\b{re.escape(term)}\b", content, re.IGNORECASE)
            if match:
                findings.append(
                    Finding(
                        "Hinweis",
                        finding_line(story, content, match.start()),
                        f"{story.story_id}: Unbestimmter Begriff „{term}“.",
                    )
                )
        if not re.search(r"\bdamit\b", story_text, re.IGNORECASE):
            findings.append(Finding("Hinweis", location, f"{story.story_id}: „damit …“ fehlt."))

        api_match = re.search(r"\b(?:API|REST)\b", content, re.IGNORECASE)
        if api_match:
            findings.append(
                Finding(
                    "Hinweis",
                    finding_line(story, content, api_match.start()),
                    f"{story.story_id}: Technischer Begriff „{api_match.group()}“.",
                )
            )

        for term, pattern in forbidden_terms:
            match = pattern.search(content)
            if match:
                findings.append(
                    Finding(
                        "Hinweis",
                        finding_line(story, content, match.start()),
                        f"{story.story_id}: Glossar führt „{term}“ als nicht zu verwenden auf.",
                    )
                )

    if prototype_text is not None:
        for match in re.finditer(r"\[\s*(US-\d+)\s+(AK\d+)\s*\]", prototype_text):
            story_id, criterion_id = match.groups()
            if criterion_id not in criteria_by_story.get(story_id, set()):
                line = prototype_text.count("\n", 0, match.start()) + 1
                findings.append(
                    Finding(
                        "Alarm",
                        f"index.html:{line}",
                        f"Prototyp verweist auf nicht vorhandenes Kriterium "
                        f"[{story_id} {criterion_id}].",
                    )
                )

    return findings


def markdown_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ").replace("\r", " ")


def render_report(findings: list[Finding], prototype_exists: bool) -> str:
    rows = [
        "## Prüfung der User Stories",
        "",
        "| Typ | Fundstelle | Hinweis |",
        "|---|---|---|",
    ]
    if findings:
        rows.extend(
            f"| {markdown_cell(finding.level)} | {markdown_cell(finding.location)} "
            f"| {markdown_cell(finding.message)} |"
            for finding in findings
        )
    else:
        rows.append("| — | — | Keine Befunde. |")
    if not prototype_exists:
        rows.extend(
            [
                "",
                "`index.html` nicht vorhanden; Prototypverweise nicht geprüft.",
            ]
        )
    return "\n".join(rows) + "\n"


def main() -> int:
    missing_files = [
        path.relative_to(ROOT).as_posix()
        for path in (STORIES_PATH, GLOSSARY_PATH)
        if not path.is_file()
    ]
    if missing_files:
        findings = [
            Finding("Alarm", ", ".join(missing_files), "Pflichtdatei fehlt.")
        ]
        prototype_exists = PROTOTYPE_PATH.is_file()
    else:
        stories_text = STORIES_PATH.read_text(encoding="utf-8")
        glossary_text = GLOSSARY_PATH.read_text(encoding="utf-8")
        prototype_exists = PROTOTYPE_PATH.is_file()
        prototype_text = (
            PROTOTYPE_PATH.read_text(encoding="utf-8") if prototype_exists else None
        )
        findings = check_content(stories_text, glossary_text, prototype_text)

    report = render_report(findings, prototype_exists)
    print(report, end="")
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(report)
            summary.write("\n")
    return 1 if any(finding.level == "Alarm" for finding in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
