# Simulation der wirtschaftlichen Fehlerkosten (Cost-Matrix)

Dieses Dokument erläutert die Straf-Logik (Penalties), welche in Phase 4 (Modellierung und Evaluation) zur Berechnung des Business Impacts auf die trainierten KI-Modelle angewendet wird. 

## Warum bestrafen wir nicht jeden Fehler gleich?
Standardmäßige KI-Metriken (wie Accuracy oder mAP) werten jede Fehlklassifizierung als „einen Fehler“. In der realen Abfallwirtschaft (z.B. bei Lobbe RSW GmbH) hat jedoch nicht jeder Fehler die gleichen finanziellen oder ökologischen Konsequenzen. 
**Zielsetzung:** Wir wollen das Modell belohnen, welches die „teuren“ Fehler vermeidet, selbst wenn es dafür vielleicht mehr „günstige“ Fehler macht.

## Übersicht der Straf-Faktoren (Heuristik)

Wir haben für unseren Proof of Concept fiktive, aber maximal realitätsnahe Business Units (Straf-Einheiten) definiert, mit denen die Confusion Matrix multipliziert wird. 

| Reales Material auf dem Band | Vorhersage der KI | Penalty-Faktor | Ökonomisches / Ökologisches Rationale |
| :--- | :--- | :--- | :--- |
| **Alle** | Korrekte Klasse | **0.0** | Wird korrekt sortiert und verkauft. Keine Verluste. |
| **Alle** | Irgendeine falsche Klasse | **1.0** (Baseline) | Standardfehler. Material landet voraussichtlich im Ersatzbrennstoff (Verbrennung) oder führt zu leichtem Wertverlust. |
| `plastic-bottle` | `paper-other` | **25.0** | **Fataler Fehler!** Plastikflaschen in der Altpapierfraktion blockieren den Auflöseprozess in der Papierfabrik (Pulper) und senken den Preis der Papiercharge massiv. Starke wirtschaftliche Strafe. |
| `plastic-foil/bag` | `paper-bag` | **10.0** | **Starke Verunreinigung:** Plastikfolien werden oft von Windsichtern mit Papier mitgerissen, was bei optischer Falscherkennung durch die KI zu verunreinigten Papier-Batches führt. |
| `aluminium-coated-foil` | `undefined` | **5.0** | **Ressourcenverlust:** Aluminium ist extrem energieaufwendig in der Herstellung und bringt als Rezyklat hohe Marktpreise. Landet es in `undefined` (oft gleichbedeutend mit thermischer Verwertung), ist die wirtschaftliche Ausbeute ruiniert. |

> [!TIP]
> **Erweiterung für die Thesis / das finale Projekt:**
> Diese Gewichte sind aktuell als *Proof of Concept* angelegt. Für einen echten Return-on-Investment (ROI) Case für den Entsorger (Lobbe) könnten diese relativen Penalty-Faktoren durch echte negative Eurowerte je Tonne (z.B. Sortierabzüge der dualen Systeme) ersetzt werden.
