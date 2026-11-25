---
name: stories-pruefen
description: Prüft User Stories einzeln anhand V1 bis V6. Nur verwenden, wenn der Nutzer diesen Skill ausdrücklich aufruft.
---

# Skill: stories-pruefen

## Aktivierung und Umfang
- Starte den Skill nur nach ausdrücklichem Aufruf durch den Nutzer. Quelle: Auftrag des Nutzers; Zitat: „startet nur, wenn ich ihn selbst aufrufe.“
- Prüfe jede vom Nutzer benannte Story einzeln. Quelle: Auftrag des Nutzers; Zitat: „prüft jede Story einzeln.“
- Vergleiche keine Story mit anderen Dokumenten und prüfe keine dokumentübergreifende Konsistenz. Quelle: Auftrag des Nutzers; Zitat: „nicht die Konsistenz zwischen mehreren Dokumenten.“
- Verwende für jede Story die Checkliste [checkliste.md](checkliste.md). Quelle: Auftrag des Nutzers; Zitat: „mit Anleitung und Checkliste.“

## Vorgehen
- Prüfe die Story und ihre Akzeptanzkriterien anhand jedes der sechs Kriterien V1 bis V6. Quelle: Auftrag des Nutzers; Zitat: „sechs Kriterien V1 bis V6.“
- Gib ausschließlich Hinweise aus, die sich mit einem wörtlichen Zitat aus der Story belegen lassen. Quelle: Auftrag des Nutzers; Zitat: „nur Hinweise mit Zitat.“
- Formuliere jeden Hinweis als offene Frage und füge keine Korrektur oder Lösung hinzu. Quelle: Auftrag des Nutzers; Zitat: „als Frage, ohne Korrekturen.“
- Zitiere pro Hinweis höchstens 15 Wörter und nenne die Fundstelle innerhalb der Story. Quelle: Auftrag des Nutzers; Zitat: „mit Zitat.“
- Trage in `Bewertung (Mensch)` nichts ein. Quelle: Auftrag des Nutzers; Zitat: „Bewertung (Mensch) bleibt leer.“

## Ausgabe
Gib genau diese Tabelle aus:

| Nr | Story | Kriterium | Zitat | Hinweis | Bewertung (Mensch) |
|---|---|---|---|---|---|

- Verwende eine Zeile pro Hinweis; `Nr` nummeriert die Hinweise, `Story` benennt die Story und `Kriterium` das betroffene Kriterium V1 bis V6. Quelle: Auftrag des Nutzers; Zitat: „Ergebnis ist eine Tabelle.“
- Lass die Zelle unter `Bewertung (Mensch)` in jeder Zeile leer. Quelle: Auftrag des Nutzers; Zitat: „Bewertung (Mensch) bleibt leer.“
- Führe unter der Tabelle `Ohne Befund` auf und nenne dort die geprüften Kriterien ohne Hinweis, je Story. Quelle: Auftrag des Nutzers; Zitat: „darunter „Ohne Befund“.“
- Führe anschließend `Nicht geprüft` auf und nenne dort alles, was nicht geprüft wurde. Quelle: Auftrag des Nutzers; Zitat: „darunter „Nicht geprüft“.“
