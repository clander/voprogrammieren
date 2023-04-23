"""

Z1: ok

Z2: müde

Z3: hunger

Z4: langeweile

Z5: müde und hungrig

Z6: müde und langweilig

Z7: hungrig und langweilig

Z8: hungrig, langweilig und müde

Jeder Gefühlszustand kann ein oder aus sein (0 oder 1)

Wir haben 3 Stellen

D.h 2 hoch 3 Möglichkeiten

"""
hunger = 0
langeweile = 0
muedigkeit = 0
zustand = "ok"

def on_every_interval():
    global muedigkeit, hunger, langeweile
    muedigkeit += 1
    hunger += 1
    langeweile += 1
loops.every_interval(1000, on_every_interval)

def on_forever():
    global zustand
    if muedigkeit >= 10 or (langeweile >= 10 or hunger >= 10):
        zustand = "tot"
    elif muedigkeit <= 5 and (langeweile <= 5 and hunger <= 5):
        zustand = "ok"
    else:
        zustand = ""
        if muedigkeit > 5:
            zustand = "" + zustand + "Mue"
        if langeweile > 5:
            zustand = "" + zustand + "Lan"
        if hunger > 5:
            zustand = "" + zustand + "Hun"
    basic.show_string(zustand)
basic.forever(on_forever)
