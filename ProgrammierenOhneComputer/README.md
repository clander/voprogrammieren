# Enaktive Handlungsanleitungen

## Lehrplanbezug

Erste Klasse

Kompetenzbereich Produktion: Inhalte digital erstellen und veröffentlichen, Algorithmen entwerfen und Programmieren
Die Schülerinnen und Schüler können

(T) eindeutige Handlungsanleitungen (Algorithmen) nachvollziehen, ausführen sowie selbstständig formulieren.

Anwendungsbereiche: Sequenzen und einfache Schleifen

## Umsetzungsmöglichkeiten
### Steuerung von Robotern auf dem Papier 
https://microbit.eeducation.at/wiki/Hauptseite, Version 2, S. 11 bis S. 18

### Bekannte Algorithmen nachspielen

#### Rollenspiel Bubblesort:

* Algorithmus: https://de.wikipedia.org/wiki/Bubblesort

Einstimmung: Die Lehrperson bringt eine Flasche Limonade oder Mineralwasser und ein paar Gläser in den Unterricht mit. Die Lernenden sollen einschenken und bevor sie trinken, die Bläschen (Bubbles) im Glas beobachten. 

Vorbereitung: Einige Schüler:innen stellen sich als Teilnehmer:innen des Rollenspiels in einer beliebigen Reihenfolge nebeneinander auf.

- Tauschüberwacher:in: Die Lehrperson bestimmt aus dem Rest der Klasse eine(n) Schüler:in als „Tauschüberwacher:in“. Er/Sie überwacht, ob ein Tauschvorgang stattgefunden hat. Falls ein Tauschvorgang bemerkt wird, hebt dieser/diese die Hand. Mit jedem neuen Durchgang wird die Hand zunächst wieder heruntergenommen.
- Vergleicher:in: Ein(e) zweite(r) Schüler:in hat die Aufgabe, je zwei Schüler:innen der Reihe miteinander zu vergleichen und dem/der Tauscher:in „Ja“ zu antworten, falls zwei nebeneinander Stehende in der Reihe so stehen, dass der Rechte kleiner ist als der Linke.
- Tauscher:in: Ein(e) dritte(r) Schüler:in wird nun beauftragt, von vorne beginnend immer zwei Schüler:innen der Reihe zu tauschen, falls der/die Vergleicher:in „Ja“ antwortet.
  - Wenn der/die Tauscher:in am Ende der Reihe angelangt ist, beginnt alles von vorne, falls der/die Tauschüberwacher:in die Hand oben hat.
  - Hat der/die Tauschüberwacher:in nach einem Durchlauf die Hand nicht oben, ist der Vorgang beendet und die Schüler:innenreihe sortiert. 

Nachbereitung: Am Ende kommt man nochmals auf die Limonade zurück. Warum trägt BubbleSort diesen Namen?

#### Kürzeste-Wege-Algorithmus von Dijkstra
* Algorithmus: https://de.wikipedia.org/wiki/Dijkstra-Algorithmus
* Dijkstra: https://de.wikipedia.org/wiki/Edsger_W._Dijkstra

**Algorithmus in Pseudocode**:

Vorbereitung: Mit Straßenkreide wird ein Wegenetz in Form eines Graphen (Knoten + Kanten + Kantengewichte + Daten pro Knoten) auf den Asphalt im Schulhof / auf die Tafel gezeichnet

1. **Startaufstellung**:
Markiere im Graphen zunächst den Startknoten als besucht (grün). Trage die Distanz zum Starknoten mit 0 ein. Dieser Startknoten wird zum aktuellen Knoten.

2. Schritt: **Distanzen zu den Nachbarknoten (Relaxierung)**: Für alle Nachbarknoten des aktuellen Knotens, die noch nicht als besucht markiert sind (also noch nicht grün sind), erledigst du folgende Punkte:
      - Berechne die Entfernung zum Startknoten: Entfernung zum aktuellen Knoten + Entfernung zum Nachbarn.
      - Wenn der betroffene Nachbar noch keine Entfernung eingetragen hat, dann trage die gerade berechnete Entfernung einfach ein und merke dir den aktuellen Knoten als Vorgänger des Nachbarn.
      - Wenn der betroffene Nachbar bereits eine Entfernung eingetragen hat und diese größer ist, als die gerade berechnete Entfernung, dann trage die neue Entfernung ein und merke dir den aktuellen Knoten als Vorgänger des Nachbarn.
2. Schritt 3: **Weiterreise**
   - Wenn es nicht besuchte Knoten gibt, suchst du denjenigen mit der aktuell kleinsten Entfernung aus. Markiere diesen Knoten als besucht. Dieser Knoten wird der aktuelle Knoten. Fahre mit Schritt 2 fort.
   - Wenn es keine nicht besuchten Knoten mehr gibt (alle Knoten sind grün), dann ist der Algorithmus zu Ende. Du hast nun die kürzesten Wege vom Startknoten aus zu allen restlichen Knoten des Graphen berechnet.

Beispiel

![image](/ProgrammierenOhneComputer/bilder/DijkstraGross.gif)

**Der kürzeste Weg für alle zum Startknoten**

Wenn du nun den kürzesten Weg von einem beliebigen Knoten des Graphen zum gewählten Starknoten wissen möchtest, dann kannst du von diesem Knoten aus über die jeweiligen Vorgänger den kürzesten Weg zum Startknoten finden.

## Weitere interessanter Algorithmus: Kürzeste Wege nach Dijkstra
- Erklärung auf YouTube: https://www.youtube.com/watch?v=KiOso3VE-vI
- Wikipedia: https://de.wikipedia.org/wiki/Dijkstra-Algorithmus
- Multiple Repräsentation: https://visualgo.net/en/sssp

## Visualgo
Auf dieser Plattform finden sich weitere Algorithmen und Datenstrukturen zusammen mit enaktiver, ikonischer und symbolischer Repräsentation:

https://visualgo.net/en

## Weitere Ressourcen
- Denken lernen, Probleme lösen / digi.case: https://men.baa.at/?men=digi.case.dlpl
- Informatik erleben (Uni Klagenfurt): http://informatik-erleben.uni-klu.ac.at
- Buch: Abenteuer Informatik von Jens Gallenbacher: https://link.springer.com/book/10.1007/978-3-662-53965-1
- Biber der Informatik-Aufgabenhefte: https://www.ocg.at/node/269
- IKEA-Bauanleitungen
- Kochbücher / Kochrezepte
- Schulbuch "Denken lernen - Probleme lösen mit BBC micro:bit", S. 11 - S. 16, https://microbit.eeducation.at/images/c/c7/Buch_microbit_sek_i-Auflage_2022_20220905_30MB.pdf 

Wichtig: die Handlungsanleitungen sollten neben einfachen Anweisungen und Sequenzen von Anweisungen auch Bedingungen, Wiederholungen und bedingte Anweisungen enthalten. Auch sollte die Notwendigkeit der Verwendung von Variablen bzw. Datenstrukturen gegeben sein.