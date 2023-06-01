# Tamagotchi

## Situation @showdialog

Bruno und Ksenia haben in der Wühlkiste ihres Vaters ein sonderbares Ei gefunden. Es hat einen kleinen Bildschirm und drei Knöpfe, in großen Buchstaben steht TAMAGOTCHI darauf.

„Papa, was ist denn das?“, fragt Ksenia.
„Oh, mein Tamagotchi!“, ruft dieser erstaunt. „Das war in den 90er-Jahren ein beliebtes Spielzeug, sozusagen ein virtuelles Haustier, um das man sich kümmern musste. Man konnte mit ihm spielen, es füttern und knuddeln. Wenn man es jedoch vernachlässigt hat, ist es traurig geworden und irgendwann gestorben. Ich habe auf meines aber immer sehr gut aufgepasst!“

„Sowas möchte ich auch!”, ruft Bruno. „Leider ist die Batterie ausgelaufen.“
Ksenia grübelt kurz und sagt: „Warte, ich habe doch den neuen BBC micro:bit V2, mit dem bauen wir unser eigenes Haustier! Wir nennen es Betty!“

(Quelle für die Aufgabenstellung: https://microbit.eeducation.at/wiki/Tamagotchi)


## Aufgabenstellung
Was soll unser Tamagotchi-Nachbau alles können?

- Wenn der BBC micro:bit V2 eingeschaltet wird, zeigt er ein neutrales Gesicht und spielt den Hallo-Sound ab.
- In einer Dauerschleife (Dauerhaft-Schleife) wird der Timer jede Sekunde hinaufgezählt.
- Nur wenn man mit Betty spielt (schüttelt) oder sie streichelt (das Logo streichelt) zeigt sie ein fröhliches Gesicht und der Timer wird auf 0 zurückgesetzt.
- Wenn der Timer auf 20 steht, zeigt Betty ein trauriges Gesicht und macht ein trauriges Geräusch.
- Wenn der Timer auf 30 steht, gähnt Betty und schläft ein.
- Wenn der Timer auf 40 steht, wird ein trauriger Sound abgespielt und Betty stirbt.

## Variable erstellen
Erstelle eine ``||variables:Variable||`` mit dem Namen **timer**. 

 ``||basic:beim Start||`` des Programms soll die Variable mit dem Wert 0 belegt werden (``||variables:setze timer auf 0||``).

```blocks
let timer = 0
timer = 0
```
Konzepte:
- [Was ist ein Computerprogramm?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/programme/konzept_programme)

## Smiley anzeigen
Mit ``||basic: zeige Symbol||`` wird ``||basic:beim Start||`` außerdem ein neutrales Gesicht angezeigt.

```blocks
let timer = 0
timer = 0
basic.showIcon(IconNames.Meh)
```
Konzepte:
- [Was sind Variablen?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/variablen/konzept_variable)
- [Was ist eine Zuweisung?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/variablen/konzept_zuweisung)

MakeCode:
- [Variablen in MakeCode](https://makecode.microbit.org/blocks/variables)

## Musik abspielen
Es soll außerdem ``||basic:beim Start||`` ein Hallo-Sound  ``||music: spiele Ton Hallo bis zum Ende||`` abgespielt werden.

```blocks
let timer = 0
timer = 0
basic.showIcon(IconNames.Meh)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
```
MakeCode:
- [Symbole am Display anzeigen](https://makecode.microbit.org/reference/basic/show-icon)
- [Musik abspielen](https://makecode.microbit.org/reference/music)

## Dauerschleife

``||loops:Alle 1000 Millisekunden||`` soll der Timer um eins erhöht werden.

```blocks
loops.everyInterval(1000, function () {
    timer += 1
})
```

Dieser Block wird wie in einer Schleife (Wiederholung) immer wieder ausgeführt, wenn die eingestellte Zeit verstrichen ist.

Konzept:
- [Was ist ein Ereignis / Ereignisbehandlung?](https://www.python-online.ch/turtle.php?inhalt_links=turtle/navigation.inc.php&inhalt_mitte=turtle/ereignisse.inc.php)

MakeCode:
- [Ereignisbehandlung](https://makecode.microbit.org/reference/event-handler)

## Mit Betty spielen
Wenn wir mit Betty spielen (``||input: wenn geschüttelt||``), zeigt sie ein fröhliches Gesicht und der Timer wird auf 0 zurückgesetzt.

```blocks
input.onGesture(Gesture.Shake, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})

```
Konzept:
- Auch hierbei handelt es sich um eine Art von Ereignisbehandlung!

## Betty streicheln
Auch wenn wir Betty streicheln (``||input: wenn Logo berührt||``), zeigt sie ein fröhliches Gesicht und der Timer wird auf 0 zurückgesetzt.

```blocks
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})
```

## Betty wird traurig
Wenn die Variable ``||variables: timer||`` den Wert 20 enthält, zeigt Betty ein trauriges Gesicht und macht ein trauriges Geräusch (``||music:spiele Ton traurig bis zum Ende||``).

Verwende den Logikblock ``||logic: Wenn||`` und eine ``||logic: Bedingung||``, die prüft, ob der Timerwert gleich 20 ist. Platziere alles im Block, der alle 1000 Millisekunden gestartet wird.
```blocks
loops.everyInterval(1000, function () {
    timer += 1
    if (timer == 20) {
        basic.showIcon(IconNames.Sad)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
    }
})
```

Konzept:
- [Was ist eine bedingte Verzweigung?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/entscheidungen/konzept_fallunterscheidungen)
- [Was ist eine Bedingung?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/bedingungen/konzept_bedingungen)

MakeCode:
- [Verzweigungen in MakeCode](https://makecode.microbit.org/blocks/logic/if)
- [Bedingungen in MakeCode](https://makecode.microbit.org/blocks/logic/boolean)

## Betty schläft ein
Wenn ``||variables: timer||`` auf 30 steht, gähnt Betty und schläft ein.

Verwende das Plus-Zeichen im ``||logic: Wenn||``-Block um einen weiteren ``||logic: sonst wenn||``-Zweig mit einer weiteren ``||logic: Bedingung||`` hinzuzufügen.

```blocks
loops.everyInterval(1000, function () {
    timer += 1
    if (timer == 20) {
        basic.showIcon(IconNames.Sad)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 30) {
        basic.showIcon(IconNames.Surprised)
        basic.showIcon(IconNames.Asleep)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.yawn), SoundExpressionPlayMode.UntilDone)
    } 
})
```
Wenn die erste Bedingung (timer == 20) zutrifft, dann wird der Block dazu ausgeführt. Falls die erste Bedingung nicht zutrifft, wird die zweite Bedingung überprüft und - falls diese zutrifft - der zugehörige Block ausgeführt, usw.

## Betty stirbt

Wenn ``||variables: timer||`` auf 40 steht, wird ein trauriger Sound abgespielt (``||music:beginne Melodie Beerdingung wiederhole einmal||``) und Betty stirbt (``||basic: Pausiere eine lange Zeit||``).

Jetzt kann man Betty nur noch durch einen Reset / Neustart zum Leben erwecken.

```blocks
loops.everyInterval(1000, function () {
    timer += 1
    if (timer == 20) {
        basic.showIcon(IconNames.Sad)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 30) {
        basic.showIcon(IconNames.Surprised)
        basic.showIcon(IconNames.Asleep)
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.yawn), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 40) {
        basic.showIcon(IconNames.Skull)
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
        basic.pause(1000000)
    }
})
```

## Erweiterung
Die Symbole für die Anzeige des Gemütszustandes von Betty sollen animiert werden.

Verwende dazu eine Schleife ``||loops: mache 3-mal wiederholen||`` und verschiedene  Symbole (``||basic: zeige Symbol||``) zur Anzeige auf dem Display. Du kannst die Ausführung auch kurz Anhalten:  ``||basic: pausiere (ms) 100||``

```blocks
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})
input.onGesture(Gesture.Shake, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})
let timer = 0
timer = 0
basic.showIcon(IconNames.Meh)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
loops.everyInterval(1000, function () {
    timer += 1
    if (timer == 20) {
        for (let index = 0; index < 3; index++) {
            basic.showIcon(IconNames.Happy)
            basic.pause(100)
            basic.showIcon(IconNames.Sad)
        }
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 30) {
        for (let index = 0; index < 3; index++) {
            basic.showIcon(IconNames.Surprised)
            basic.pause(100)
            basic.showIcon(IconNames.Asleep)
        }
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.yawn), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 40) {
        basic.showIcon(IconNames.Skull)
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
        basic.pause(1000000)
    }
})
```

Konzept:
- [Was sind Schleifen?](https://www.inf-schule.de/imperative-programmierung/python/konzepte/wiederholungen/konzept_wiederholungen)

MakeCode:
- [Schleifen in MakeCode](https://makecode.microbit.org/blocks/loops)

## Gratulation @showdialog
Gratulation, du hast das dein eigenes Tamagotchi programmiert! Lade es nun auf deinen micro:bit Microcontroller und teste es aus!