# Lerntheorie und Programmierunterricht
## Programmieren lernen und Piaget
Die Berücksichtigung der kognitiven Entwicklungsstufen nach Piaget können im Rahmen der Gestaltung von Programmierunterricht didaktisch hilfreich sein.

Dazu ist die Theorie von Raymond Lister interessant, der seine Findings in folgendem Paper publiziert hat: Raymond Lister. 2016. Toward a Developmental Epistemology of Computer Programming. In Proceedings of the 11th Workshop in Primary and Secondary Computing Education (WiPSCE '16). Association for Computing Machinery, New York, NY, USA, 5–16. https://doi.org/10.1145/2978249.2978251

Eine zusammenfassende Darstellung des Papers wird hier geboten (incl. Video):
https://textbooks.cs.ksu.edu/cis400/a-learning-programming/

Kurz beschrieben geht es darum, den Fortschritt, den die Lernenden bei der Nutzung von Programmiersprachen zur Lösung von Problemstellungen in verschiedene Entwicklungsphasen machen, methodisch-didaktisch zu nutzen:

<table>
    <tr>
        <th>Stufe</th>
        <th>Beobachtungen (nach Lister)</th>
    </tr>
    <tr>
        <td>Sensomotorische Phase (Pre-Tracing-Phase)</td>
        <td>
            <ul>
                <li>Zeilenweise Codeerklärungen zu < 50 % ok</li>
                <li>Vorherrschende Problemlösungsstrategie: Versuch und Irrtum</li>
            </ul>
        </td>
    </tr>
    <tr> 
        <td>Präoperationale Phase (Tracing-Phase)</td><td>
            <ul>
                <li>Zeilenweise Codeerklärungen zu > 50 % ok</li>
                <li>Zeilenweise Codeerklärungen ohne Bezug zur Semantik des gesamten Programmteils</li>
                <li>Keine Beziehungen zwischen den Codezeilen interpretierbar</li>
                <li>Ikonische Repräsentationen von Code (Diagramme) können nicht sinnbringend eingesetzt werden</li>
                <li>Vorherschende Problemlösunsstrategie: Zufällige Codeänderungen und intensives Testen der Ergebnisse</li>
            </ul>
        </td>
    </tr>
    <tr> 
        <td>Phase der konkreten Operationen (Tracing-Phase)</td><td>
            <ul>
                <li>Vorherschende Problemlösunsstrategie: Copy-Paste mit Lösungsidee; da und dort ausbessern</li>
                <li>Auf die Semantik des Codes (und damit auch schon ansatzweise die Beziehungen zwischen den Zeilen) kann durch intensive Beschäftigung mit der Laufzeit und den Ausführungsergebnissen geschlossen werden</li>
                <li>Beschäftigung auf mit der Lösung sehr kontextualisiert; Abstraktionsfähigkeit noch eingeschränkt</li>
            </ul>
        </td>
    </tr>
    <tr> 
        <td>Phase der formalen Operationen (Post-Tracing-Phase)</td><td>
            <ul>
                <li>Hypothetisches und deduktives Denken ist ausgeprägt</li>
                <li>Code kann "gelesen" werden -> es geht nicht mehr um die Interpretation der einzelnen Zeilen und ihrer Beziehungen sondern um das Gesamtkonstrukt -> Schema</li>
            </ul>
        </td>
    </tr>
</table>

(https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/)

Dieses Modell geht also davon aus, dass Lernende beim Programmieren diese Phasen durchlaufen und letztendlich neues Wissen durch Akkomodation aufbauen bzw. entsprechend der Cognitive Load Theorie entsprechende Schemata aufbauen. Ein Experte hat solche Schemata bereits ausgebildet. Ein Anfänger muss hingegen Code zeilenweise interpretieren, die einzelnen Codezeilen zueinander in Beziehung bringen und dann im Gesamten ableiten, was der Code macht. Ein Experte liest code durch Applikation seiner Schemata auf Teilstrukturen im Code, ohne darüber nachzudenken zu müssen, was einzelne Zeilen bedeuten, wie sie syntaktisch genau aufgebaut sind, wie sie zueinander in Beziehung stehen etc.

Beim Codieren selbst hat der Experte bereits vor Beginn der Codierphase eine klare Vorstellung der betroffenen Schemata und implementiert diese zur Problemlösung direkt. Er kennt die Syntax der Sprache. Er kennt die Werkzeuge, die er dabei verwendet. Anfänger müssen sich jede Codezeile sowohl syntaktisch als auch semantisch hart erarbeiten. Sie müssen lernen die Beziehungen zwischen den Zeilen korrekt herzustellen. Sie müssen abschätzen, was ihr Code nun in Bezug auf die Lösung Problemstellung bedeutet und sie müssen darüber nachdenken, wie sie mit ihrem Code dann auch noch eine ganze Klasse von ähnlichen Problemstellungen lösen können (Abstraktion). Sie müssen sich außerdem mit Syntaxproblemen und Tooling-Problemen (Compiler, Kommandozeile, IDEs etc.) auseinandersetzen.

(https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/)
## Parallelen zur CLT und zu SOLO
Es fallen zwei offensichtliche Parallelen zu weiteren bekannten Theorien auf: Die Cognitive Load Theorie nach Sweller argumentiert im Rahmen der Theorie der Elementinteraktion sowie der Schemakonstruktion den Lernprozess auf ähnliche Art und Weise.

Für die Lösung von Programmierproblemstellungen ist ein hoher Grad an Elementinteraktivität nötig. Lösungen in der Programmierung bestehen aus der zueinander passenden Anwendungen von im Prinzip vielen kleinen Lösungselementen. Das Arbeitsgedächtnis kann aber immer nur 3 bis 5 Lösungselemente gleichzeitig verarbeiten. Ziel muss es sein, diese Lösungselemente zusammengenommen als komplette Lösungschemata im Langzeitgedächtnis zu verankern. 

Ein Schema nach Sweller ist ein kognitives Konstrukt mit Hilfe dessen Informationen organisiert, strukturiert und (im Arbeitsgedächtnis) schnell verarbeitet werden können. Im Arbeitsgedächtnis wird ein automatisiertes Schema dabei als ein einziges Element betrachtet, selbst wenn das Schema eine Vielzahl von interagierenden Elementen betreffen kann. Durch die (automatisierte) Anwendung von Schemata können damit komplexe Herausforderungen mit relativ geringer Belastung des Arbeitsgedächtnisses gemeistert werden.

Die SOLO-Lernzieltaxonomie nach Biggs nimmt die piaget'schen Grundgedanken bzw. das Prinzip der Elementinteraktivität nach Sweller ebenfalls auf:

* prästrukturelle Problemlösungen: Die Lösung des Lernenden zeigt, dass er noch nichts verstanden hat. Versuch und Irrtum sind vorherrschend.
* unistrukturelle Problemlösungen: Die Lösung zeigt, dass einzelne Programmzeilen passen, zueinander aber in keinem sinnvollen Verhältnis stehen.
* multistrukturelle Problemlösungen: Die Lösung zeigt, dass mehrere Programmzeilen zusammenpassen und auch zusammen erklärt werden können. Die Erklärungen zu den Lösungen zeigen aber auch, dass die Lernenden Probleme bei der weiteren Abstraktion der Lösung etwa im Sinne der kreativen Zusammensetzung von Lösungsteilen oder im Sinne der Verallgemeinerung der Lösung auf ganze Problemklassen haben.
* erweitert abstrakte Problemlösungen: Die Lösung entspricht einer Lösung, die auch Experten so erstellen und erklären würden. Die Lösung wird auf Ebene der zentralen betroffenen Schemata erklärt. Sie ist allgemein gültig und kann auf Problemklassen angewendet werden.
## Gemäßigt konstruktivistische Sicht auf den Lernprozess
Lernende konstruieren nach konstruktivistischer Auffasung des Lernprozesses aktiv ihre eigene Wirklichkeit indem sie auf kognitive Konflikte mit Assimilation und Akkommodation reagieren und so kognitive Konflikte auflösen. 

* Assimilation: Neues Wissen generieren indem man an bestehende Strukturen im Gedächtnis andockt 
Akkomodation: Neues Wissen generieren, für das es noch keine Aknüpfungspunkte im Gedächtnis gibt.
* Akkomodation erfordert entsprechende Stimuli (intensive Beschäftigung, Fehlschläge, viel Arbeit, Informationen versuchen zu verarbeiten, soziale Stimuli) UND eine entsprechende Haltung zum Lernen (lernen wollen, verstehen wollen, weiterkommen wollen etc.).

Modrow spricht von „Verschärfungsprozess“: nebelhafte, unzureichende Vorstellung der Welt wird durch intensive Beschäftigung den Erfahrungen angepasst.

Für die Informatikdidaktik ist die konstruktivistische Sicht auf den Lernprozess besonders wichtig. Jerome Bruner gilt als einer der Urväter des Konstruktivismus UND als Urvater des didaktischen Konzeptes der Fundamentalen Ideen.

* Lernen erfolgt durch kognitive Konflikte / Kollisionen
    * können nur auftreten, wenn sich Lernende aktiv mit dem Gegenstand auseinandersetzen, sich dafür interessieren, ihn für relevant halten, soziale Aspekte damit verbinden ...
* Aufgabe der Lernenden: 
    * Bereitschaft zur aktiven Auseinandersetzung und zur Persönlichkeitsentwicklung
    * eigene Vorstellungen erproben, ändern, erweitern
    * Blockaden dieser Bereitschaft müssen beseitigt werden (dauerhaft und ggf. mit Konsequenzen)
* Rolle der Lehrenden 
    * beziehen sich auf individuelle Vorkenntnisse, Misskonzeptionen, Lernprozesse und Lebenswelt der Lernenden (Betroffenheit erzeugen)
    * konfrontieren die Lernenden mit ihrem unvollständigen Verständnis zu den Inhalten 
    * müssen fachlich / fachdidaktisch souverän reagieren, um individuell zugeschnittene Anregungen geben zu können

Das bedeutet also für konstruktivistische Settings (Hubwieser): 
* Aktive Beteiligung, Motivation und Interesse sind die Grundvoraussetzungen für das Lernen.
* Die Lernenden übernehmen bis zu einem gewissen Grad selbst die Steuerung und Kontrolle über den Lernprozess.
* Lernen kann nur mit Bezug auf die Erfahrungen, auf das Vorwissen und durch Interpretationen der Lernenden selbst erfolgen.
* Lernen erfolgt immer in Kontexten, d. h. situativ.
* Lernen ist ein sozialer Prozess.

Charakteristika für konstruktivistische Settings:

* Handlungsorientierung, entdeckendes Lernen und aktive Beteiligung in möglichst vielen Bereichen des Unterrichts fördern
* Eigenverantwortung für den Lernprozess fördern
* metakognitive Fähigkeiten fördern (Lernen lernen, Selbstbeobachtung, Selbstbewertung, Selbstverstärkung etc.)
* Authentizität für alle Belange des Unterrichts garantieren (authentische Lernsituationen, lernen in verschiedenen Kontexten, situiertes Lernen)
* kooperatives Lernen fördern (z. B. durch Einbettung des Lernens in einen sozialen, kooperativen Kontext)
* Perspektivenwechsel bei der Erschließung der Inhalte ermöglichen
* Erschließung von Problemlösemethoden durch die Lernenden selbst ermöglichen
* genügend Bearbeitungszeit zur Verfügung stellen
* formatives Feedback intensiv nutzen
* Instruktionsteile nicht vernachlässigen (denn fachspezifisches Vorwissen fördert den Lernprozess nachweislich am stärksten)
* neue Lehrendenrolle als Coach wahrnehmen

Instruktion ist aber trotzdem (oder gerade deswegen) wichtig (auch weil Instruktion entlastet -> siehe Cognitive Load Theorie bzw. Modeling, Scaffoling, Fading, Coaching im ID Cognitive Apprenticeship):

* Unterricht muss Instruktion und Konstruktion bieten 
* hängt auch mit den verschiedenen Zieldimensionen und Constructive Alignment zusammen
    * Ziele höherer Ebenen -> eher konstruktivistisch zu erreichen
    * Ziele niederer Ebenen -> eher kognitivistisch / behavioristisch zu erreichen
* Reinmann / Mandl sprechen vom Wissensbasierten Konstruktivismus:
    * Im wissensbasierten Konstruktivismus wird Lernen als eine persönliche Konstruktion von Bedeutung interpretiert, die nur dann gelingt, wenn eine ausreichende Wissensbasis zur Verfügung steht. Zum Erwerb dieser Wissensbasis  kann auf instruktionale Anleitungen nicht verzichtet werden.
* Auch entdeckendes Lernen funktioniert nach Klauer besonders gut, wenn es als Guided Discovery im Sinne von Jerome Bruner ausgeführt ist, d.h. wenn: 
  * [...] der Prozess des Entdeckens behutsam gelenkt wird, fehlendes, aber notwendiges Wissen im Bedarfsfall direkt vermittelt wird, die Komplexität des Problems nicht zu hoch ist oder angemessen reduziert wird und variierende Aufgaben für eine hinreichende Generalisierung der Erkenntnis und für die Einübung des Transfers sorgen. ([KL07, Seite 99])
* Modrow spricht in seiner Dissertation von pragmatisch konstruktivistisch (und ideenorientierten) Lehr-Lern-Situationen