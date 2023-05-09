# Tamagotchi ePet


## Aufgabe für micro:bit

![](./bilder/tamagotchiMicrobitAufgabe.png)
(Quelle: Denken lernen -Probleme lösen mit BBC micro:bit V1 + V2, S. 73 - S. 74, https://microbit.eeducation.at/images/c/c7/Buch_microbit_sek_i-Auflage_2022_20220905_30MB.pdf)

### Implementierung
![](./bilder/tamagotchiMicrobitLoesung.png)

```python
def on_logo_pressed():
    global timer
    timer = 0
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_shake():
    global timer
    timer = 0
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

timer = 0
timer = 0
basic.show_icon(IconNames.ASLEEP)

def on_every_interval():
    global timer
    timer += 1
    if timer == 10:
        basic.show_icon(IconNames.ASLEEP)
    elif timer == 20:
        basic.show_icon(IconNames.SAD)
    elif timer == 30:
        basic.show_icon(IconNames.SURPRISED)
        basic.show_string("z z z")
    elif timer == 40:
        basic.show_icon(IconNames.SKULL)
        control.reset()
loops.every_interval(1000, on_every_interval)

```

## Komplexere Version für Python (ohne micro:bit)

Die folgende Version eines Tamagotchi ePets ist etwas komplexer. Das ePet kann müde, gelangweilt oder hungrig sein. Es gibt verschiedene Tendenzen für die einzelnen Zustände (Tendenz meint eine Wahrscheinlichkeit für die Verschlechterung des jeweiligen Zustands).

Zwischen jeder Aktion, die mit dem Tier durchgeführt werden kann, vergeht ein wenig Zeit (zufällig immer eine etwas andere Zeitspanne).

Das Tier möchte außerdem nicht immer spielen, essen oder schlafen. Das hängt vom aktuellen jeweiligen Zustand ab.

Jede mit dem Tier durchgeführt Aktion (füttern, schlafen legen, spielen) hat Auswirkungen auf alle Zustände.

Die Implementierung dazu sieht wie folgt aus:

```python
import time, random

tendenzZurMuedigkeit = 60
tendenzZurLangeweile = 50
tendenzZumHunger = 30
zeitTick = 10
name = input("Wie soll dein virtuelles Haustier heißen? ")
hunger = 5
langeweile = 5
muedigkeit = 5
while True: 
    print("")
    print("**************************")
    print("Ein wenig Zeit vergeht ...")
    print("**************************")
    time.sleep(random.randint(zeitTick-zeitTick/2, zeitTick+zeitTick/2))
    if random.randint(1,100)<tendenzZumHunger:
        hunger = hunger + 1
    if random.randint(1,100)<tendenzZurLangeweile:
        langeweile = langeweile + 1
    if random.randint(1,100)<tendenzZurMuedigkeit:
        muedigkeit = muedigkeit + 1
    if hunger > 5:
        print("\a____ Ich bin hungrig ... ("+str(hunger)+") ____")
    time.sleep(0.5)
    if langeweile > 5:
        print("\a____ Ich bin gelangweilt ... ("+str(langeweile)+") ____")
    time.sleep(0.5)
    if muedigkeit > 5:
        print("\a____ Ich bin müde ... ("+str(muedigkeit)+") ____")
    aktion = input("Was möchtest du mit " +str(name) + " tun? (1) Spielen (2) Füttern (3) Schlafen lassen (4) nichts? ")
    if aktion == "1":
        if langeweile > 3:
            print("____ Super, ich mag spielen ____ ")
            langeweile = langeweile - 3
            hunger = hunger + 1
            muedigkeit = muedigkeit + 1
        else:
            print("____ Ich mag jetzt nicht spielen ____")
    elif aktion == "2":
        if hunger > 3:
            print("____ Mmmmmh, fressen ____")
            hunger = hunger - 3
            muedigkeit = muedigkeit + 1
            langeweile = langeweile - 1
        else:
            print("____ Ich hab keinen Hunger ____")
    elif aktion == "3":
        if muedigkeit > 3:
            print("____ Ich bin müde, ich gehe schlafen ____")
            muedigkeit = muedigkeit - 3
            hunger = hunger + 1
            langeweile = langeweile + 1
        else:
            print("____ Ich mag jetzt nicht schlafen ____")
    elif aktion =="4":
        print("____")
    else:
        print("____ Ich weiß nicht was du von mir willst ____")
    if hunger > 10 or langeweile > 10 or muedigkeit > 10:
        break
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Ich mag nicht mehr dein Haustier sein, ich renne jetzt weg ...")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


```