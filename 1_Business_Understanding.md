# CRISP-DM Phase 1: Business Understanding

Die Abfallwirtschaft und insbesondere das Recycling von Leichtstoffverpackungen ist eine der zentralen Säulen der modernen Kreislaufwirtschaft (Circular Economy). Die nachfolgenden Abschnitte definieren die wirtschaftlichen Treiber, Bewertungsmaßstäbe und die Stakeholder-Perspektiven für den Einsatz von Deep Learning in der kamerabasierten Abfallsortierung.

## 1. Rationale: Motivation für Maschinelles Lernen in der Sortierung

Die konventionelle automatisierte Abfallsortierung verlässt sich stark auf Nah-Infrarot-Sensoren (NIR), Magnetabscheider und Druckluftdüsen, um Materialien (PET, PE, PP, Alu) zu trennen. Diese Systeme stoßen unter realen Bedingungen an ihre Grenzen:
*   **Objektüberlappungen & Verschmutzung**: Ein vom Post-Consumer-Markt stammender Joghurtbecher ist oft mit Essensresten verschmutzt, deformiert oder von Folien überdeckt. Konventionelle Sensoren messen unter Umständen nur den Dreck oder das falsche Oberflächenmaterial.
*   **Fehlender Objektkontext**: Ein NIR-Sensor erkennt "PET", weiß aber nicht, ob es sich um eine gut recycelbare PET-Flasche oder eine schwer recycelbare PET-Schale (Thermoform-PET) handelt. 

**Warum Machine Learning (Computer Vision)?**
Deep Learning Modelle (wie YOLO oder DETR) analysieren hochauflösende RGB-Kamerabilder und lernen nicht nur pixelbasierte Materialeigenschaften, sondern den **geometrischen, semantischen Kontext** (Form, Branding, Deckel, typische Verformung). Das ermöglicht Sortieranlagen, Abfallströme *objektbasiert* statt nur *materialbasiert* zu klassifizieren und führt zu einer drastischen Erhöhung der Sortenreinheit.

## 2. Metriken für die Erkennungsleistung

In der Abfallsortierung kann eine falsch gewählte Metrik katastrophale Business-Entscheidungen nach sich ziehen. Die bloße „Accuracy“ (Genauigkeit) ist aufgrund von Klassenungleichgewichten ("Class Imbalance" - viel mehr kleine transparente Folien als große Waschmittelflaschen) ungeeignet.

Die entscheidenden Metriken sind:
1.  **Precision (Genauigkeit der Vorhersage) -> Indikator für Sortenreinheit**:
    *   *Bedeutung*: Von allen Objekten, die das System als "PET-Flasche transparent" klassifiziert hat, wie viele waren *wirklich* transparente PET-Flaschen?
    *   *Business Impact*: Hohe Precision bedeutet wenig Fremdstoffe im Endprodukt. Die Anlage produziert hochreine Sekundärrohstoffe, die am Markt teurer verkauft werden können.
2.  **Recall (Sensitivität) -> Indikator für Masse/Ausbeute**:
    *   *Bedeutung*: Von *allen tatsächlich existierenden* transparenten PET-Flaschen auf dem Laufband, wie viele hat das System gefunden?
    *   *Business Impact*: Hoher Recall bedeutet weniger Wertstoffverlust in den Restmüll. Die Ausbeute maximiert sich.
3.  **Mean Average Precision (mAP)**: 
    *   Errechnet die Fläche unter der Precision-Recall-Kurve über verschiedene Schwellenwerte (Confidence & IoU - Intersection over Union) hinweg. Dies ist die Standardmetrik zum Vergleich verschiedener Modelle (z.B. YOLOv8 vs. RT-DETR).
4.  **Cost-Sensitive Evaluation ("Kostenmatrix")**:
    *   Da Fehler unterschiedlich teuer sind (z.B. eine schwarze Plastikschale in der PET-Fraktion zerstört die Klarheit eines ganzen Batches und senkt den Preis drastisch; ein Joghurtbecher im Restmüll verbrennt nur wertlos), muss eine monetäre Kostenfunktion über die Confusion Matrix gelegt werden.

## 3. Ökologische und ökonomische Implikationen für Stakeholder

| Stakeholder | Ökonomische Implikationen | Ökologische Implikationen |
| :--- | :--- | :--- |
| **Recyclinganlagen / Entsorger (z.B. Lobbe)** | **+ Umsatz**: Verkauf von hochreinen (Single-Stream) Rezyklaten zu Premiumpreisen.<br>**- Kosten**: Vermeidung von Verbrennungsgebühren, da weniger Wertstoffe im Restmüll ("Ersatzbrennstoff") landen. Reduzierte Kosten für personelle Nachsortierung. | **+ Ressourceneffizienz**: Maximierung des extrahierten Materialwerts, Unterstützung interner Nachhaltigkeits-KPIs. |
| **FMCG-Hersteller / Marken (Nestlé, Coca Cola)** | **- Risiko**: Leichtere Erfüllung gesetzlicher Vorgaben (EU Packaging and Packaging Waste Directive) durch Zugang zu hochwertigen recycelten Kunststoffen (rPET). | **+ Umweltziele**: Verringerung des CO2-Fußabdrucks durch Einsatz von recyceltem Material anstelle von fossil-basiertem Primärplastik. |
| **Gesellschaft & Umwelt** | **+ Wertschöpfung**: Förderung lokaler Kreislaufwirtschaft statt Rohstoffimporten. | **+ Klima**: Direkte Reduktion von Treibhausgasen durch Verringerung abfallbedingter Verbrennung; weniger Plastik in der Umwelt. Verhinderung einer linearen "Take-Make-Dispose" Wirtschaft. |
