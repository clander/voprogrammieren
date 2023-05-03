# Handlungsanleitungen

## Lehrplanbezug

Erste Klasse

Kompetenzbereich Produktion: Inhalte digital erstellen und veröffentlichen, Algorithmen entwerfen und Programmieren
Die Schülerinnen und Schüler können

(T) eindeutige Handlungsanleitungen (Algorithmen) nachvollziehen, ausführen sowie selbstständig formulieren.

Anwendungsbereiche: Sequenzen und einfache Schleifen

## Idee
Schüler:innen befolgen Handlungsanleitungen / Algorithmen und lösen damit bestimmte Probleme.

Wichtig ist, dass die Handlungsanleitungen  neben einfachen Anweisungen und Sequenzen von Anweisungen auch Bedingungen, Wiederholungen und bedingte Anweisungen enthalten. Auch sollte die Notwendigkeit der Verwendung von Variablen bzw. Datenstrukturen gegeben sein.

## Steuerung von Robotern auf dem Papier 
https://microbit.eeducation.at/wiki/Hauptseite, Version 2, S. 11 bis S. 18

## Rollenspiel Bubblesort

Algorithmus: https://de.wikipedia.org/wiki/Bubblesort

Einstimmung: Die Lehrperson bringt eine Flasche Limonade oder Mineralwasser und ein paar Gläser in den Unterricht mit. Die Lernenden sollen einschenken und bevor sie trinken, die Bläschen (Bubbles) im Glas beobachten. 

Vorbereitung: Einige Schüler:innen stellen sich als Teilnehmer:innen des Rollenspiels in einer beliebigen Reihenfolge nebeneinander auf.

- Tauschüberwacher:in: Die Lehrperson bestimmt aus dem Rest der Klasse eine(n) Schüler:in als „Tauschüberwacher:in“. Er/Sie überwacht, ob ein Tauschvorgang stattgefunden hat. Falls ein Tauschvorgang bemerkt wird, hebt dieser/diese die Hand. Mit jedem neuen Durchgang wird die Hand zunächst wieder heruntergenommen.
- Vergleicher:in: Ein(e) zweite(r) Schüler:in hat die Aufgabe, je zwei Schüler:innen der Reihe miteinander zu vergleichen und dem/der Tauscher:in „Ja“ zu antworten, falls zwei nebeneinander Stehende in der Reihe so stehen, dass der Rechte kleiner ist als der Linke.
- Tauscher:in: Ein(e) dritte(r) Schüler:in wird nun beauftragt, von vorne beginnend immer zwei Schüler:innen der Reihe zu tauschen, falls der/die Vergleicher:in „Ja“ antwortet.
  - Wenn der/die Tauscher:in am Ende der Reihe angelangt ist, beginnt alles von vorne, falls der/die Tauschüberwacher:in die Hand oben hat.
  - Hat der/die Tauschüberwacher:in nach einem Durchlauf die Hand nicht oben, ist der Vorgang beendet und die Schüler:innenreihe sortiert. 

Nachbereitung: Am Ende kommt man nochmals auf die Limonade zurück. Warum trägt BubbleSort diesen Namen?

## Kürzeste-Wege-Algorithmus von Dijkstra

Algorithmus: https://de.wikipedia.org/wiki/Dijkstra-Algorithmus

Dijkstra: https://de.wikipedia.org/wiki/Edsger_W._Dijkstra

### Pseudocode (Handlungsanleitung)

Vorbereitung: Mit Straßenkreide wird ein Wegenetz in Form eines Graphen (Knoten + Kanten + Kantengewichte + Daten pro Knoten) auf den Asphalt im Schulhof / auf die Tafel gezeichnet

1. Schritt: **Startaufstellung**:
Markiere im Graphen zunächst den Startknoten als besucht (grün). Trage die Distanz zum Starknoten mit 0 ein. Dieser Startknoten wird zum aktuellen Knoten.

2. Schritt: **Distanzen zu den Nachbarknoten (Relaxierung)**: Für alle Nachbarknoten des aktuellen Knotens, die noch nicht als besucht markiert sind (also noch nicht grün sind), erledigst du folgende Punkte:
      - Berechne die Entfernung zum Startknoten: Entfernung zum aktuellen Knoten + Entfernung zum Nachbarn.
      - Wenn der betroffene Nachbar noch keine Entfernung eingetragen hat, dann trage die gerade berechnete Entfernung einfach ein und merke dir den aktuellen Knoten als Vorgänger des Nachbarn.
      - Wenn der betroffene Nachbar bereits eine Entfernung eingetragen hat und diese größer ist, als die gerade berechnete Entfernung, dann trage die neue Entfernung ein und merke dir den aktuellen Knoten als Vorgänger des Nachbarn.
2. Schritt 3: **Weiterreise**
   - Wenn es nicht besuchte Knoten gibt, suchst du denjenigen mit der aktuell kleinsten Entfernung aus. Markiere diesen Knoten als besucht. Dieser Knoten wird der aktuelle Knoten. Fahre mit Schritt 2 fort.
   - Wenn es keine nicht besuchten Knoten mehr gibt (alle Knoten sind grün), dann ist der Algorithmus zu Ende. Du hast nun die kürzesten Wege vom Startknoten aus zu allen restlichen Knoten des Graphen berechnet.

### Der kürzeste Weg für alle zum Startknoten

Wenn du nun den kürzesten Weg von einem beliebigen Knoten des Graphen zum gewählten Starknoten wissen möchtest, dann kannst du von diesem Knoten aus über die jeweiligen Vorgänger den kürzesten Weg zum Startknoten finden.
### Beispiel-Ablauf:

![image](/ProgrammierenOhneComputer/bilder/DijkstraGross.gif)

## Algorithmenvisualisierungen mit Visualgo
Auf dieser Plattform finden sich weitere Algorithmen und Datenstrukturen zusammen mit enaktiver, ikonischer und symbolischer Repräsentation:

https://visualgo.net/en

## "Computer spielen" einmal anders

### Abkürzungen
PZ – Programmzählerregister, AR – Akkumulatorregister, BR – Befehlsregister, SR – Speicheradressenregister, E – Eingabe, A – Ausgabe;
### Befehlssatz
|Instruction|Mnemonic|Machine Code|Explanation|Handlungsanleitung|
|-----------|--------|------------|-----------|-----------------|
|Load Accumulator|LDA|5xx|Load the contents of the given memory address (xx) into the Accumulator|Gehe zur Speicherstelle mit der Adresse die im SR angegeben ist und kopiere den Wert von dort in das AR.
|Store Accumulator|STA|	3xx|	Store the contents of the Accumulator at the given memory address (xx)|Schreibe den Wert aus dem AR in die Speicherstelle mit der Adresse die im SR angegeben ist.|
|Add|	ADD|	1xx|	Add the contents of the given memory address (xx) to the value in the Accumulator|Gehe zur Speicherstelle mit der Adresse die im SR angegeben ist und lies dort die Zahl. Addiere dann diese Zahl zur Zahl im AR und schreibe das Ergebnis wieder zurück in das AR.
|Subtract|	SUB|	2xx|	Subtract the contents of the given memory address (xx) from the value in the Accumulator|Gehe zur Speicherstelle mit der Adresse die im SR angegeben ist und lies dort die Zahl. Subtrahiere dann diese Zahl von der Zahl im AR und schreibe das Ergebnis wieder zurück in das AR.
|Input|	INP|	901|	Copy the value from the Input 'mailbox' into the Accumulator|Frag deinen Banknachbarn nach einer Zahl zwischen 0 und 99 und leg die Zahl in E ab. Kopiere dann den Wert aus E in das AR.
|Output|	OUT|	902|	Copy the value from the Accumulator into the Output 'mailbox'| Kopiere den Wert aus dem AR nach A.
|Branch|	BRA|	6xx|	Branch (jump) to the instruction at the given memory address (xx)|Schreibe die Zahl die im SR steht in das PZ.
|Branch if positive|	BRP|	8xx|	If the value in the Accumulator is positive (including zero), then branch to the instruction at the given memory address (xx)|Wenn im AR 0 oder eine positive Zahl steht, dann schreibe die Zahl die im SR steht in das PZ.
|Branch if zero|	BRZ|	7xx|	If the value in the Accumulator is zero, then branch to the instruction at the given memory address (xx)|Wenn im AR 0 steht dann schreibe die Zahl die im SR steht in das PZ.
|Halt|	HLT|	000|	Stop execution of the program|Beende die Programmausführung.
|Data|	DAT|	value of the data|	Indicates that the current memory address holds a data value 

### Programmausführung
Die folgenden Anweisungen sagen dir im Detail wie die Ausführung jedes Programms ablaufen muss. Halte dich bei der Ausführung der Programme ganz genau an diese Anweisungen. Verwende die erstellte Tabellenvorlage für die Speicherung aller während der Programmsauführung relevanten Daten.

**Vor jedem Programmstart** machst du folgendes:
1. Schreib den Wert 0 in das PZ.
2. Lösche den Inhalt aller sonstigen Register (AR, BR, SR).
3. Lösche den Inhalt aus Eingabe und Ausgabe (E, A).
4. Übertrage das auszuführende Computerprogramm in die Arbeitsspeichertabelle.

Führe das Programm nach folgenden Angaben aus:
1. **Befehl holen** (FETCH):
   1. Lies die Zahl im PZ.
   2. Gehe in deiner Arbeitsspeicher-Tabelle in die Zeile mit der Speicheradresse die der gelesenen Zahl entspricht.
   3. Schreibe den Befehl der an dieser Speicherstelle angegeben ist in das BR.
   4. Schreibe die hinter dem Befehl angegebene Speicheradresse in das SR. Wenn hinter dem Befehl nichts angegeben ist, lösche den Inhalt von SR.
2. **Befehl dekodieren**:
   1. Lies den Befehl im BR und lies in der Befehlssatz-Tabelle nach
was zu tun ist. 
3. **Befehl ausführen**:
   1. Erhöhe PZ um +1.
   2. Führe jetzt den Befehl entsprechend den Angaben in der
Befehlssatz-Tabelle aus.
4. **Beginne wieder mit Punkt 1** falls du nicht an einem ENDE-Befehl
   angelangt bist.

### Beispielprogramme

Adition von zwei Zahlen:

|Zeile|Label|Befehl|Operand|
|-----|-----|------|-------|
|00|start||
|01||STA|A|
|02||INP||
|03||ADD|A|
|04||OUT||
|05||HLT||
|06||||
|07|A|DAT|0|
...

Zwei Nummern eingeben, die höhere zurückgeben:
|Zeile|Label|Befehl|Operand|
|-----|-----|------|-------|
|00||INP||
|01||STA|FIRST|
|02||INP||
|03||STA|SECOND|
|04||SUB|FIRST|
|05||BRP|HIGHER|
|06||LDA|FIRST|
|07||BRA|DONE|
|08|HIGHER|LDA|SECOND|
|09|DONE|OUT||
|10||HLT||
|11|FIRST|DAT||
|12|SECOND|DAT||
### "Echte" Little-Man-Computers zum Ausführen
Auf den folgenden Websites gibt es LMC-Implementierungen, mit denen man die Ausführung von Code wie oben ausprobieren kann:

* https://wellingborough.github.io/LMC/LMC0.3.html
* https://peterhigginson.co.uk/LMC/
* https://www.101computing.net/LMC/

Weiter Details dazu siehe https://en.wikipedia.org/wiki/Little_man_computer

## Weitere Ressourcen
- Denken lernen, Probleme lösen / digi.case: https://men.baa.at/?men=digi.case.dlpl
- Informatik erleben (Uni Klagenfurt): http://informatik-erleben.uni-klu.ac.at
- Buch: Abenteuer Informatik von Jens Gallenbacher: https://link.springer.com/book/10.1007/978-3-662-53965-1
- Biber der Informatik-Aufgabenhefte: https://www.ocg.at/node/269
- IKEA-Bauanleitungen
- Kochbücher / Kochrezepte
- Schulbuch "Denken lernen - Probleme lösen mit BBC micro:bit", S. 11 - S. 16, https://microbit.eeducation.at/images/c/c7/Buch_microbit_sek_i-Auflage_2022_20220905_30MB.pdf 