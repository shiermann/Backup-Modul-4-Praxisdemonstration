# Banking-App · Kartenverwaltung · User Stories

Musterbank AG (fiktiv) · Produktbacklog Team Karten · Stand v2 (Überarbeitung Fachbereich Karten) · 18.11.2026
Quellen: siehe Ordner `quellen/` (A = Fachkonzept Tageslimit, B = Fachliche Beschreibung Kartensperre, Glossar)

---

## US-211 Kartenübersicht anzeigen

**Story:** Als Kund:in möchte ich alle meine Debitkarten in einer Übersicht sehen, damit ich weiß, welche Karte aktiv und welche vorübergehend gesperrt ist.

**Quelle:** B1, B5

**Akzeptanzkriterien**
- AK1: Gegeben: Die Kund:in hat mehrere Debitkarten. Wenn sie die Kartenübersicht öffnet, dann sind alle ihre Debitkarten aufgelistet.
- AK2: Jede Karte zeigt nur die letzten vier Ziffern der Kartennummer.
- AK3: Jede Karte zeigt ihren Status: aktiv oder vorübergehend gesperrt.

---

## US-212 Kartendetails ansehen

**Story:** Als Kund:in möchte ich die Details einer Debitkarte ansehen, damit ich Ablaufdatum und Kartenlimit kenne.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- noch offen

---

## US-213 Tageslimit für Überweisungen ändern

**Story:** Als Kund:in möchte ich mein Tageslimit für Überweisungen in der App selbst ändern, damit ich dafür nicht im Kundenservice anrufen muss.

**Quelle:** A1–A6, SR-12

**Akzeptanzkriterien**
- AK1: Gegeben: Die Kund:in senkt ihr Tageslimit. Dann gilt das neue Limit sofort.
- AK2: Gegeben: Die Kund:in erhöht ihr Tageslimit auf höchstens 10.000 EUR. Wenn sie per Fingerabdruck oder App-PIN bestätigt, dann gilt das neue Limit sofort.
- AK3: Gegeben: Die Kund:in möchte ihr Tageslimit über 10.000 EUR erhöhen. Dann wird die Erhöhung nicht in der App durchgeführt, der Kundenservice ruft zurück.
- AK4: Die Änderung ist in höchstens drei Schritten möglich.
- AK5: Das Standardlimit beträgt 2.000 EUR.

---

## US-214 Karte vorübergehend sperren und entsperren

**Story:** Als Kund:in möchte ich meine Debitkarte in der App vorübergehend sperren und wieder entsperren, damit ich bei einer verlegten Karte nicht die Hotline anrufen muss.

**Quelle:** Ziel, B1–B7

**Akzeptanzkriterien**
- AK1: Gegeben: mehrere Debitkarten. Wenn die Kund:in eine Karte sperrt, dann bleiben die anderen nutzbar.
- AK2: Gegeben: Karte gesperrt. Wenn an der Kasse bezahlt wird, dann wird die Zahlung abgelehnt.
- AK3: Gegeben: Karte gesperrt. Wenn eine Lastschrift oder ein Dauerauftrag fällig ist, dann wird er ausgeführt.
- AK4: Gegeben: Karte aktiv. Wenn die Kund:in sie sperrt, dann wirkt die Sperre sofort (Zeitwert offen).
- AK5: Gegeben: Karte gesperrt. Wenn die Kund:in entsperrt, dann ist eine Bestätigung per Biometrie oder App-PIN nötig.
- AK6: Gegeben: Karte gesperrt. Wenn die Kund:in die Karte in der App ansieht, dann ist der Sperrstatus sichtbar.
- AK7: Wenn eine Karte gesperrt oder entsperrt wird, dann erhält die Kund:in eine Push-Nachricht.
- AK8: Gegeben: Karte gesperrt. Wenn die Sperre 10 Tage besteht, dann erhält die Kund:in eine Erinnerung; die Karte bleibt gesperrt.

---

## US-215 Tageslimit der Debitkarte ändern

**Story:** Als Kund:in möchte ich das Tageslimit meiner Debitkarte für Zahlungen an der Kasse selbst ändern, damit ich auch größere Einkäufe bezahlen kann.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Wenn die Kund:in das Tageslimit erhöht, dann muss sie per Fingerabdruck bestätigen.
- AK2: Eine Senkung des Tageslimits gilt sofort.
- AK3: Das Tageslimit kann bis 5.000 EUR erhöht werden.

---

## US-216 Online-Zahlungen aktivieren und deaktivieren

**Story:** Als Kund:in möchte ich Online-Zahlungen mit meiner Debit- oder Kreditkarte aktivieren und deaktivieren, damit ich mich vor Missbrauch im Internet schütze.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Gegeben: Online-Zahlungen sind deaktiviert. Wenn online mit der Karte bezahlt wird, dann wird die Zahlung abgelehnt.
- AK2: Zahlungen an der Kasse sind davon nicht betroffen.
- AK3: Die Einstellung ist in der Kartenübersicht sichtbar.

---

## US-217 Push-Nachricht bei Kartenzahlung

**Story:** Als Kund:in möchte ich bei jeder Kartenzahlung eine Push-Nachricht erhalten, damit ich unbekannte Zahlungen sofort bemerke.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Nach jeder Kartenzahlung erhält die Kund:in innerhalb weniger Sekunden eine Push-Nachricht mit Betrag und Händler.
- AK2: Die Kund:in kann diese Push-Nachrichten in den Einstellungen ausschalten.

---

## US-218 Karte endgültig sperren

**Story:** Als Kund:in möchte ich meine Debitkarte bei Verlust oder Diebstahl in der App endgültig sperren, damit niemand sie missbrauchen kann.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Vor der endgültigen Sperre muss die Kund:in bestätigen.
- AK2: Eine endgültige Sperre kann nicht rückgängig gemacht werden.
- AK3: Eine vorübergehend gesperrte Karte wird nach 30 Tagen automatisch endgültig gesperrt.

---

## US-219 Karten-PIN anzeigen

**Story:** Als Kund:in möchte ich meine Karten-PIN in der App anzeigen, damit ich sie nicht vergesse.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Die PIN wird sicher angezeigt.
- AK2: Nach 10 Sekunden wird die PIN wieder ausgeblendet.

---

## US-220 Ersatzkarte bestellen

**Story:** Als Kund:in möchte ich nach einer endgültigen Sperre eine Ersatzkarte in der App bestellen.

**Quelle:** Produktbacklog

**Akzeptanzkriterien**
- AK1: Die Bestellung wird per REST-API an den Kartenprozessor übermittelt.
- AK2: Die Ersatzkarte wird an die hinterlegte Adresse geschickt.
- AK3: Die Ersatzkarte wird innerhalb von 5 Werktagen zugestellt.
