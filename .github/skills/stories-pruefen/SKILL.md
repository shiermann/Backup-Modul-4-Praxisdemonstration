---
name: stories-pruefen
description: Prüft eine einzelne User Story anhand V1 bis V6. Nur verwenden, wenn der Nutzer diesen Skill selbst aufruft.
---

# Skill: stories-pruefen

## Aktivierung
- Starte diesen Skill nur nach ausdrücklicher Selbstaufrufung durch den Nutzer. Quelle: Auftrag des Nutzers; Zitat: „startet nur, wenn ich ihn selbst aufrufe.“
- Prüfe nur eine einzelne User Story; vergleiche nicht mehrere Dokumente miteinander. Quelle: Auftrag des Nutzers; Zitat: „prüft jede Story einzeln, nicht die Konsistenz zwischen mehreren Dokumenten.“
- Verwende die Checkliste [checkliste.md](checkliste.md). Quelle: Auftrag des Nutzers; Zitat: „mit Anleitung und Checkliste.“

## Vorgehen
- Ermittle die zu prüfende Story aus dem vom Nutzer benannten Dokument. Quelle: Auftrag des Nutzers; Zitat: „mit dem ich User Stories prüfen lasse.“
- Prüfe für diese Story ausschließlich V1 bis V6; kennzeichne jede Nichtprüfung unter „Nicht geprüft“. Quelle: Auftrag des Nutzers; Zitat: „Die Checkliste hat sechs Kriterien V1 bis V6.“
- Prüfe nur den Inhalt der einzelnen Story und deren dort genannten Akzeptanzkriterien. Quelle: Auftrag des Nutzers; Zitat: „prüft jede Story einzeln.“
- Gib keine Korrekturen aus. Quelle: Auftrag des Nutzers; Zitat: „ohne Korrekturen.“
- Nutze Fundstellen und wörtliche Zitate von höchstens 15 Wörter. Quelle: Auftrag des Nutzers; Zitat: „Hinweise mit Zitat.“

## Ausgabe
Erstelle genau diese Struktur:

| Nr | Story | Kriterium | Zitat | Hinweis | Bewertung (Mensch) |
|---|---|---|---|---|---|

- Jede Befundzeile muss als Frage formuliert sein. Quelle: Auftrag des Nutzers; Zitat: „nur Hinweise mit Zitat, als Frage.“
- Die Spalte `Bewertung (Mensch)` bleibt leer. Quelle: Auftrag des Nutzers; Zitat: „Bewertung (Mensch) bleibt leer.“
- Unter der Tabelle füge den Abschnitt `Ohne Befund` ein. Quelle: Auftrag des Nutzers; Zitat: „darunter „Ohne Befund“.“
- Unter „Ohne Befund“ füge den Abschnitt `Nicht geprüft` ein und benenne dort jede Nichtprüfung. Quelle: Auftrag des Nutzers; Zitat: „darunter „Nicht geprüft“.“
