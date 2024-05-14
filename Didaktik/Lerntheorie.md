# Lerntheorie und Programmierunterricht

## Piaget's genetische Epistemologie (Erkenntnistheorie)

Ausgangspunkt unserer Überlegungen bildet Piaget mit seiner Erkenntnistheorie.

### Begriffsdefinitionen
  - Epistemologie = Erkenntnistheorie: Studium des menschlichen Wissens / Erkenntnisgewinnungsprozesses / Lernens
  - Genese: Das Entstehen von etwas; im Sinne von Ursprung und Entwicklung
  
### Zwei Lernmechanismen
  - Assimilation: 
    - Neues Wissen wird generiert, indem man an bestehende Strukturen (Vorwissen) im Gedächtnis andockt.
    - Beispiel: Lernende haben verstanden, wie While-Schleifen funktionieren. Der Weg zum Verständnis eines weiteren Schleifentyps ist über Assimilation möglich.
  - Akkomodation (deutlich aufwändiger als Assimilation): 
    - Neues Wissen generieren, für das es noch keine Anknüpfungspunkte im Gedächtnis gibt.
    - Bauen von neuen strukturierenden Elementen / neuen Schemata
    - Gleichbedeutend mit dem Aufbau und der Verstärkung von neuen Verbindungen zwischen Nervenzellen (Neurodidaktik).
    - Beispiel: Lernende wissen noch nichts von Schleifen und müssen für ein Verständnis der Funktionsweise von Schleifen (insb. incl. des Zusammenwirkens der konstitutiven Teile) völlig neue Strukturen aufbauen.

([Quelle](https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/))

### Akkomodation und Lernen im konstruktivistischen Sinne
  - Akkomodation erfordert entsprechende Stimuli / Anreize / kognitive Konflikte:
    - Eigenartiges, Kontroversielles, Unerklärliches, Erstaunliches
    - soziale Stimuli
  - Akkomodation erfordert entsprechende Haltung und Motivation
    - lernen wollen, verstehen wollen, weiterkommen wollen
    - intensive Beschäftigung, Fehlschläge, viel Arbeit
    - Motivation und Willen zur intensiven Beschäftigung
  - Lernen kann als Verschärfungsprozess verstanden werden (Modrow).  
    - Zunächst nebelhafte, unzureichende Vorstellungen der Welt (Ungleichgewicht in Bezug auf das eigene Verständnis) wird durch intensive Beschäftigung in die bestehenden Erfahrungen eingepasst (Gleichgewicht herstellen).
    - EUREKA-Moment / Aha-Erlebnisse
      - Das Gleichgewicht in den kognitiven Strukturen ist wieder hergestellt.
      - CLT: Ein neues Schema ist ausgebildet.
      - Aha-Erlebnisse: wichtiges Instrument zur Reflexion
    - Üben, üben, üben: 
      - Intensive praktische Beschäftigung hilft beim Bewusstmachen des kognitiven Ungleichgewichts.
      - Das wiederum ist als Anreiz Voraussetzung für Akkomodation.
([Quelle](https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/))

### Neo-Piaget'sche Stufentheorie
Anhäger der Neo-Piaget'schen Stufentheorie (siehe Lister) gehen weiters davon aus, dass Lernende unabhängig ihres Alters und unabhängig vom zu lernenden Inhalt im Rahmen des Lernprozesses die 4 Stufen der kognitiven Entwicklung nach Piaget durchlaufen, um neue Fähigkeiten und Konzepte über Akkomodation und Assimilation zu erlernen (d.h. angepasste oder neue kognitive Strukturen dafür auszubilden).

1. Sensomotorische Stufe
2. Präoperationale Stufe
3. konkret operationale Stufe
4. Stufe der formalen Operationen
   
Diese 4 Stufen gehen fließend ineinander über [Overlapping Waves Model](https://www.researchgate.net/figure/Overlapping-waves-depiction-of-cognitive-development-From-Emerging-Minds-by-Siegler_fig6_274964913). Folgende drei Annahmen sind dabei zentral:
1. Zu einem bestimmten Zeitpunkt, haben Kinder immer verschiedene Sichtweisen bzw. verschiedene kognitive Denkweisen auf Phänomene / Konzepte / Inhalte etc.
2. Diese Sichtweisen auf Phänomene / dieses variantenreiche Denken über Phänomene / Konzepte / Inhalte führt über längere Zeit zu einem inneren Konflikt. Die konkurrierenden Sichtweisen existieren parallel.
3. Kognitive Entwicklung bedeutet dann, dass ein gradueller Wechsel in der Häufigkeit der Anwendung der entsprechend konkurrierenden Sichtweise auftritt. Eine alte Sicht auf ein Phänomen wird zugunsten einer neuen Sicht (die etwa auf Basis neuer Erkenntnisse zustande kommt) langsam weniger häufig genutzt. Das ist der Entwicklungsprozess.

[(Quelle, S. 7)](https://srcd.onlinelibrary.wiley.com/doi/abs/10.1111/1540-5834.00075)

## Developmental Epistemology of Computer Programming (Raymond Lister und Donna M. Teague)
Lister und Teague wenden die Stufentheorie nach Piaget auf die Computerprogrammierung im Unterricht an ([Artikel](https://www.academia.edu/110073788/Toward_a_Developmental_Epistemology_of_Computer_Programming)). Sie beschreiben in ihrer Theorie Eigenschaften von Lernenden, die sich in den einzelnen Entwicklungsstufen und damit in den entsprechenden Phasen des Lernprozesses für einen neuen Inhalt befinden. Sie beschreiben damit auch einen Weg, den Lernende beim Lernen dieser Inhalte beschreiten.

Eine zusammenfassende Darstellung (siehe die folgende Tabelle) der zugrundegelegten Ideen (incl. Video) bietet Nathan Bean auf
https://textbooks.cs.ksu.edu/cis400/a-learning-programming/. Es geht dabei primär um die Frage, wie Lernende Code erklären (= Tracing = Verständnis zur Ablaufverfolgung von Programmcode).

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
        <td>Präoperationale Phase (Tracing-Phase 1)</td><td>
            <ul>
                <li>Zeilenweise Codeerklärungen zu > 50 % ok</li>
                <li>Zeilenweise Codeerklärungen ohne Abstraktion von den einzelnen Zeilen weg und damit ohne Bezug zur Semantik des gesamten Programmteils</li>
                <li>Keine Beziehungen zwischen den Codezeilen interpretierbar</li>
                <li>Ikonische Repräsentationen von Code (Diagramme) können nicht sinnbringend eingesetzt werden</li>
                <li>Vorherrschende Problemlösungsstrategie: Zufällige Codeänderungen und intensives Ausprobieren der Ergebnisse</li>
            </ul>
        </td>
    </tr>
    <tr> 
        <td>Phase der konkreten Operationen (Tracing-Phase 2)</td><td>
            <ul>
                <li>Vorherrschende Problemlösungsstrategie: Copy-Paste mit Lösungsidee; da und dort ausbessern</li>
                <li>Auf die Semantik des Codes (und damit auch schon ansatzweise die Beziehungen zwischen den Zeilen) kann durch intensive Beschäftigung mit der Laufzeit und den Ausführungsergebnissen geschlossen werden</li>
                <li>Beschäftigung mit der Lösung sehr kontextualisiert; Abstraktionsfähigkeit noch eingeschränkt</li>
            </ul>
        </td>
    </tr>
    <tr> 
        <td>Phase der formalen Operationen (Post-Tracing-Phase)</td><td>
            <ul>
                <li>Hypothetisches und deduktives Denken ist ausgeprägt</li>
                <li>Deduktiv: vom Allgemeinen (=Schema / Konzept) auf das Konkrete (= kontextualisierte Anwendung des Schemas) schließen
                <li>Code kann "gelesen" werden -> es geht nicht mehr um die Interpretation der einzelnen Zeilen und ihrer Beziehungen sondern um das Gesamtkonstrukt</li>
                <li>Schema (CLT) ist ausgebaut und wird getriggert</li>
                <li>Akkomodation ist durchgeführt</li>
            </ul>
        </td>
    </tr>
</table>

Dieses Modell geht also davon aus, dass Lernende beim Programmieren diese Phasen durchlaufen und letztendlich neues Wissen durch Akkomodation aufbauen bzw. entsprechend der Cognitive Load Theorie entsprechende Schemata aufbauen. Ein Experte hat solche Schemata bereits ausgebildet. Ein Anfänger muss hingegen Code zeilenweise interpretieren, die einzelnen Codezeilen zueinander in Beziehung bringen und dann im Gesamten ableiten, was der Code macht. Ein Experte liest Code durch Applikation seiner Schemata auf Teilstrukturen im Code, ohne darüber nachdenken zu müssen, was einzelne Zeilen bedeuten, wie sie syntaktisch genau aufgebaut sind, wie sie zueinander in Beziehung stehen etc. ([Quelle](https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/))

Beim Codieren selbst hat der Experte bereits vor Beginn der Codierphase eine klare Vorstellung der betroffenen Schemata und implementiert diese zur Problemlösung direkt. Er kennt die Syntax der Sprache. Er kennt die Werkzeuge, die er dabei verwendet. Anfänger müssen sich jede Codezeile sowohl syntaktisch als auch semantisch hart erarbeiten. Sie müssen lernen die Beziehungen zwischen den Zeilen korrekt herzustellen. Sie müssen abschätzen, was ihr Code nun in Bezug auf die Lösung Problemstellung bedeutet und sie müssen darüber nachdenken, wie sie mit ihrem Code dann auch noch eine ganze Klasse von ähnlichen Problemstellungen lösen können (Abstraktion). Sie müssen sich außerdem mit Syntaxproblemen und Tooling-Problemen (Compiler, Kommandozeile, IDEs etc.) auseinandersetzen. ([Quelle](https://textbooks.cs.ksu.edu/cis400/a-learning-programming/06-developmental-epistemology/))

## Seymour Papert und Mitch Resnick
Seymour Papert (Professor für Mathematik und Erziehungswissenschaften am MIT) war Schüler von Piaget. Er hat Piaget's Ideen in die Informatikdidaktik getragen und unter dem Begriff "Konstruktionismus" weiterentwickelt:

- Wissensrekonstruktion durch die Lernenden selbst
- Herstellen (Konstruktion) von Lernproduktion (Artefakten) durch intensive Beschäftigung / Lernendenaktivität
- Interesse an Produkten und Stolz auf Produkte als Motivation

Papert steht für:

- Situiertes Lernen 
  - Problemorientierung in authentischen Situationen
  - verschiedene Kontexte
  - Artikulation und Reflexion zum Zwecke der individuelle Abstraktion
  - sozialer Kontext
- Frühes Eröffnen von konkret operativen (siehe Piaget) Zugangsmöglichkeiten zu den neuen Technologien
- Entdeckendes Lernen mit Computerunterstützung

Papert entwickelte die Programmiersprache LOGO (incl. Miniwelt-Konzept) und gilt aufgrund der in LOGO realisierten Ideen auch als geistiger Vater von Scratch.

### Das Design von Scratch
Scratch ist nach Mitch Resnick (der für die Entwicklung der LEGO Mindstorms und zusammen mit Yasmin Kafai für Scratch verantwortlich) in diesem konstruktivistischen bzw. konstruktionistischen Geiste als Lernumgebung konzipiert, die folgende didaktische Aspekte in den Vordergrund stellt:

- **Product**: Lernprodukte erzeugen, aktiv sein, Ideen entwickeln und umsetzen, ...
- **Passion**: stolz sein, sich engagieren, 
- **Peers**: teilen, zusammenarbeiten, diskutieren
- **Play**: eigene Lebenswelt, Spieltrieb ausleben, Wirkprinzipien verstehen, Herausforderungen designen und bewältigen, ...

Scratch greift in der Tradition von LOGO viele Ideen auf und entwickelt diese konsequent und mit weiterhin starkem Fokus auf die konstruktivistische bzw. konstruktionistische Sicht auf den Lernprozess weiter.

- Miniwelt-Konzept im Geiste von LOGO 
    - visuelles und enaktives Nachverfolgen von Programmierkonzepten 
    - sofortiges, visuelles und interaktives Feedback
    - Code für zu sofort sichtbaren Zustandsänderungen in der Miniwelt
    - damit wird die kognitive Weiterentwicklung im Sinne der Phasen nach Piaget / Lister  unterstützt
- Konzeptorientierung vs. Werkzeugorientierung
  - Umsetzung zentraler Konzepte der Programmierung (siehe Blockkategorien)
  - Blockbasierung vermeidet hohen Zeitaufwand für Training von Syntax
- Blockbasierung
  - gehört zum Training-Wheels-Konzept von Scratch
  - Blockkategorien konzeptionell gebildet
  - Andocken, korrektes Einsetzen etc. wird interaktiv / visuell untersützt
  - Blöcke können interaktiv genutzt werden (Doppelklick auf den Block führt den Block sofort aus)
  - High-Level-Blöcke (z.B. [Entfernung von Mauszeiger], Sprite-Steuerung etc.)
  - Lernmaterialien (incl. interaktive Tutorials)
  - Diese Art der Blockbasierung ist für sich schon ein defacto-Standard geworden
- Lernmaterialien
  - Interaktive Tutorials
  - Beispiele von Peers
- Lebenswelt der Schüler
  - Problemdomäne spezialisiert auf Spiele, Multimedia
  - Extensions für Robotik, Microcontroller, KI, Turtle-Grafik etc.
  - Konzeptioneller Fokus auf Lebenswelt der Schüler:innen:
    - Interaktiv vs. EVA
    - Events vs. Batch
    - Parallel vs. Sequentiell
    - Multimedia vs. Kommandozeile
    - Austauschplattform für die Projekte
- Keine lokale Installation nötig

## Parallelen der Theorie von Lister zur Cognitive Load Theorie (CLT)
Für die Lösung von Programmierproblemstellungen ist ein hoher Grad an Elementinteraktivität nötig. Lösungen in der Programmierung bestehen aus  zueinander passenden Anwendungen von vielen kleinen Lösungselementen (incl. deren Abstraktion in weiterer Folge). Das Arbeitsgedächtnis kann aber immer nur 3 bis 5 Lösungselemente gleichzeitig verarbeiten. Ziel muss es sein, diese Lösungselemente zusammengenommen als komplette Lösungsschemata im Langzeitgedächtnis zu verankern (= Schemakonstruktion). Entsprechend der CLT ist es wichtig, beim Aufbau der Schemata das Arbeitsgedächtnis nicht zu überlasten.

Ein Schema nach Sweller ist ein kognitives Konstrukt mithilfe dessen Informationen organisiert, strukturiert und (im Arbeitsgedächtnis) schnell verarbeitet werden können. Im Arbeitsgedächtnis wird ein automatisiertes Schema dabei als ein einziges Element betrachtet, selbst wenn das Schema eine Vielzahl von interagierenden Elementen betreffen kann. Durch die (automatisierte) Anwendung von Schemata können damit komplexe Herausforderungen mit relativ geringer Belastung des Arbeitsgedächtnisses gemeistert werden.

Ziel entsprechenden Unterrichts ist es, das Arbeitsgedächtnis beim Aufbau der Schemata nicht zu überbelasten. Dazu muss der extrinsische Cognitive Load (bedingt durch die Komplexität der Lernumgebung) sowie der instrinsische Cognitive Load (dem Lerngegenstand inhärenter CL) so weit reduziert werden, dass er vom Arbeitsgedächtnis bewältigt werden kann. Speziell im Bereich der Programmierung ist dabei Vorsicht geboten, weil der ICL aufgrund der hohen Elementinteraktivität der Inhalte ohne entsprechend ausgebildeter Schemata sehr schnell überhandnimmt.

## Parallelen der Theorie von Lister zur SOLO-Taxonomie
Die SOLO-Lernzieltaxonomie nach Biggs nimmt die piaget'schen Grundgedanken bzw. das Prinzip der Elementinteraktivität nach Sweller ebenfalls auf. SOLO ist ein Akronym und bedeutet "Structure of Observed Learning Outcome". SOLO ist also an sich ein hierarchisches Kategorienschema für die Klassifizierung von beobachteten Schüler:innen-Leistungen, das aber auch für Entwicklung von Lernzielhierarchien oder auch für die Entwicklung von Aufgabenstellungen (verschiedener Komplexitätsgrade) verwendet werden kann.

- **Prästrukturell** (Misserfolg, Inkompetenz, Kernpunkte nicht verstanden, zusammenhangslos): Die Aufgabe wurde nicht korrekt angegangen, die Lernenden haben den Kern der Aufgabe nicht verstanden.
- **Unistrukturell** (identifizieren, benennen, nachmachen): Ein Aspekt oder einige wenige Aspekte einer (komplexeren) Aufgabe wurden aufgegriffen und bearbeitet.
- **Multistrukturell** (kombinieren, beschreiben, aufzählen, einfache Fertigkeiten, auflisten): Mehrere Aspekte der Aufgabe wurden gelernt, aber separat behandelt und können nicht integriert werden.
- **Relational** (verstehen, analysieren, anwenden, argumentieren, vergleichen, kritisieren, in Beziehung setzen, rechtfertigen): Die Teilkomponenten der Aufgabe wurden gelernt und (unter Anwendung entsprechender Konzepte) zusammen verwendet, um ein großes Ganzes zu bilden. Die Anwendung erfolgte durch (nahen) Transfer.
- **Erweitert abstrakt** (erzeugen, formulieren, generieren, Hypothesen bilden, reflektieren, Theoriebildung): Eine Lösung aus der vorhergehenden Stufe wurde abstrahiert und auf ein neues Thema angewendet bzw. reflektiert (nicht spezifischer Transfer).

## Bezug zum Konzept der Fundamentalen Ideen (Jerome Bruner)
Jerome Bruner gilt einerseits als einer der Väter der konstruktivisitischen Lerntheorie, andererseits begründete er die **Theorie der Fundamentalen Ideen (FI)**, das für Informatikunterricht ganz besonders relevant ist. 

Die Eigenschaften von Fundamentalen Ideen definiert Andreas Schwill mit Bezug auf Bruner (und andere) für die Informatikdidaktik in dern 1990er Jahren wie folgt: 

> "Eine fundamentale Idee bezüglich eines Gegenstandsbereichs (Wissenschaft, Teilgebiet) ist ein Denk-, Handlungs-, Beschreibungs- oder Erklärungsschema, das
> 1. in verschiedenen Gebieten des Bereichs vielfältig anwendbar oder erkennbar ist (Horizontalkriterium)
> 2. auf jedem intellektuellen Niveau aufgezeigt und vermittelt werden kann (Vertikalkriterium)
> 3. zur Annäherung an eine gewisse idealisierte Zielvorstellung dient, die jedoch faktisch möglicherweise unerreichbar ist (Zielkriterium)
> 4. in der historischen Entwicklung des Bereichs deutlich wahrnehmbar ist und längerfristig relevant bleibt (Zeitkriterium)
> 5. einen Bezug zur Sprache und Denken des Alltags und der Lebenswelt besitzt (Sinnkriterium)" 
> (Schwill, 1993)

Die Relevanz der Fundamentalen Ideen für unser Fach begründet sich u.A. auf der Erfüllung der verschiedenen Kriterien, die für FI gelten müssen. Informatische Inhalte ...

- scheinen an der Oberfläche oft sehr kurzlebig zu sein, die FI dahinter haben jedoch Bestand (Zeitkriterium)
- haben genau dann besonderen allgemeinbildenden Wert, wenn sie aufgrund der zugrundegelegten FIn auf andere Disziplinen übertragbar sind (Horizontalkriterium)
- sind oft abstrakt, nicht sichtbar, schwer greifbar. Sie müssen daher früh eingeführt und dann später in immer wieder abstrakteren Versionen thematisiert werden (Vertikalkriterium, Curriculumspirale)
- lassen genau dann einen direkten Bezug zur Lebenswelt der Lernenden zu, wenn sie auf den zugrundegelegten FIn basieren (Sinnkriterium).

Wiggins und McTighe (Einstieg zu iherer Understanding-By-Design-Didaktik siehe [hier](https://www.researchgate.net/publication/318021095_Wiggins_G_McTighe_J_2005_Understanding_by_design_2nd_ed_Alexandria_VA_Association_for_Supervision_and_Curriculum_Development_ASCD)) beschreiben die Eigenschaften FIn so:

- FIn sind der Kern eines Faches und daher für den Erkenntnisgewinn in einer Fachdisziplin besonders wichtig,
- sind Denkweisen und Wahrnehmungsweisen von Experten,
- sind abstrakt und für Novizen oft nicht sofort eingängig, nicht intuitiv, führen oft zu Misskonzeptionen,
- ermöglichen eine konzeptorientierte, priorisierende und reduzierende Sicht auf die wesentlichen Aspekte eines Faches und zwar durch die Verbindung von Fakten, Fertigkeiten, Erfahrungen zu einem größeren Ganzen
- ermöglichen Transfer (sowohl vertikal über die Zeit als auch horizontal über die Teilbereichs- und Fachgrenzen hinweg).
- können nicht gelehrt werden, sondern müssen durch lehrergelenkten, entdeckenden Unterricht von den Lernenden selbst entdeckt werden.

Wiggins und McTighe identifizieren folgende Erscheigunsformen von FIn:

- Konzepte (die Verbindungen zwischen einzelnen Inhalten eines Faches herstellen)
- Themen (die ein Fach strukturieren)
- Kernstrategien
- Faustregeln
- fortwährende Debatten und Streitfragen
- Paradoxons, Dilemmas
- langlebige Problemfelder und Herausforderungen
- wichtige Theorien
- Kernannahmen, Kernperspektiven
- Erkenntnisse
- Prinzipien

Eine weitere Kernaussage aus der Theorie von Bruner:

>"Jedem Kind kann auf jeder Entwicklungsstufe jeder Lehrgegenstand in einer intellektuell ehrlichen Form gelehrt werden"

Mit dieser provokanten Aussage tritt Jerome Bruner in gewisser Weise in Konkurrenz zu den Ansichten von Piaget, der ja von einer Stufentheorie des Lernens ausgeht und damit imipliziert, dass diese Annahme eben gerade nicht gilt.

Im Kern geht es in Bruners Theorie (siehe dazu sein Standardwerk "The Process of Education") darum, die Lernenden im Unterricht dazu zu befähigen, das Erlernte in immer wieder neuen Problemsituationen effektiv zur Anwendung zu bringen. Bruner plädiert dafür, den kognitiven Rekonstruktionsprozess von "Fundamentale Ideen" ins Zentrum einer jeden Ausbildung zu stellen. Lernende sollen damit dazu behäfigt werden, das im Unterricht gelernte auf immer wieder neue Problemsituationen des Alltags, des späteren Lebens etc. umzulegen. Es geht also im Kern um die Befähigung zum Wissenstransfer (vgl. dazu insb. auch die österreichische Leistungsbeurteilungsverordnung, deren Notenstufen an genau diesem Aspekt ausgerichtet sind).

> The first object of any act of learning, over and beyond the pleasure it may give, is that it should serve us in the future. Learning should not only take us somewhere; it should allow us later to go further more easily. There are two ways in which learning serves the future.
One is through its specific applicability to tasks that are highly similar to tho- se we originally learned to perform. Psychologists refer to this phenomenon as specific transfer of training; perhaps it should be called the extension of habits or associations. Its utility appears to be limited in the main to what we usually speak of as skills. Learning in school undoubtedly creates skills of a kind that transfers to activities encountered later, either in school or after. A second way in which earlier learning renders later performance more effi- cient is through what is conveniently called nonspecific transfer or, more accurately, the transfer of principles and attitudes. In essence, it consists of learning initially not a skill but a general idea, which can then be used as a basis for recognizing subsequent problems as special cases of the idea originally mastered. This type of transfer is at the heart of the educational process – the continual broadening and deepening of knowledge in terms of basic and general ideas. ([Bru60, Seite 17])

In Bezug auf Methodik können nach Bruner (insb. auch aufgrund seiner These, dass jedes wichtige Konzept auf jeder Altersstufe gelernt weden kann) folgende Schwerpunkte identifiziert werden:

- Spiralcurriculum
  - Vorwegnehmendes Lernen 
    - Inhalte werden möglichst früh didaktisch reduziert, aber inhaltlich redlich eingeführt
  - Fortsetzbarkeit
    - Inhalte werden im Laufe des Curriculums immer wieder aufgegriffen, auf immer neuen kognitiven Niveaus, in immer komplexerer Art und Weise
  - Präfiguration
    - Inhalte werden in unterschiedlichen Darstellungsformen, darunter ikonisch, symbolisch und enaktiv präsentiert (Repräsentationstrias)
- Projektunterricht / Problemorientierung / Schülerzentrierung
- (Gelenktes) Entdeckendes Lernen

## Gemäßigt konstruktivistische Sicht auf den Lernprozess
Insgesamt ist die Sicht auf den Lernprozess vor dem Hintergrud der Lehre von Piaget, Papert und auch jener von Jerome Bruner stark konstruktivistisch geprägt. Lernende konstruieren nach konstruktivistischer Auffassung des Lernprozesses aktiv ihre eigene Wirklichkeit, indem sie auf kognitive Konflikte mit Assimilation und Akkommodation reagieren und so kognitive Konflikte auflösen. Das bedeutet zusammengefasst nach Modrow:

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

Instruktion ist aber trotzdem (oder gerade deswegen) wichtig, auch weil Instruktion entlastet (vgl. dazu die Grundaussagen der Cognitive Load Theorie):

* Unterricht muss Instruktion und Konstruktion bieten 
* hängt auch mit den verschiedenen Zieldimensionen und Constructive Alignment zusammen
    * Ziele höherer Ebenen -> eher konstruktivistisch zu erreichen
    * Ziele niederer Ebenen -> eher kognitivistisch / behavioristisch zu erreichen
* Reinmann / Mandl sprechen vom Wissensbasierten Konstruktivismus:
    * Im wissensbasierten Konstruktivismus wird Lernen als eine persönliche Konstruktion von Bedeutung interpretiert, die nur dann gelingt, wenn eine ausreichende Wissensbasis zur Verfügung steht. Zum Erwerb dieser Wissensbasis  kann auf instruktionale Anleitungen nicht verzichtet werden.
* Auch entdeckendes Lernen funktioniert nach Klauer besonders gut, wenn es als Guided Discovery im Sinne von Jerome Bruner ausgeführt ist, d.h. wenn: 
  * [...] der Prozess des Entdeckens behutsam gelenkt wird, fehlendes, aber notwendiges Wissen im Bedarfsfall direkt vermittelt wird, die Komplexität des Problems nicht zu hoch ist oder angemessen reduziert wird und variierende Aufgaben für eine hinreichende Generalisierung der Erkenntnis und für die Einübung des Transfers sorgen. ([KL07, Seite 99])
* Modrow spricht in seiner Dissertation von pragmatisch konstruktivistisch (und ideenorientierten) Lehr-Lern-Situationen