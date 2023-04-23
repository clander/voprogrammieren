"""
Z1: ok
Z2: müde
Z3: hungrig
Z4: gelangweilt
Z5: müde und hungrig
Z6: müde und gelangweilt
Z7: hungrig und gelangweilt
Z8: hungrig, gelangweilt und müde
Jeder Gefühlszustand kann ein oder aus sein (0 oder 1)
Wir haben 3 Stellen, d.h 2 hoch 3 Möglichkeiten

MERMAID:
    stateDiagram-v2
    [*] --> ok
    ok --> müde: Müdigkeit>=5
    ok --> gelangweilt: Langeweile>=5
    ok --> hungrig: Hunger>= 5

    müde --> ok: Müdigkeit<5
    gelangweilt --> ok: Langeweile<5
    hungrig --> ok: Hunger<5

    müde --> tod: Müdigkeit>10
    gelangweilt --> tod: Langeweile>10
    hungrig --> tod: Hunger>10
    
    müde+hungrig --> müde: Hunger<5
    müde+gelangweilt --> müde: Langeweile<5
    müde+hungrig --> hungrig: Müdigkeit<5
    müde+gelangweilt --> gelangweilt: Müdigkeit<5

    müde+hungrig --> tod: Müdigkeit>10 oder Hunger>10
    müde+gelangweilt --> tod: Müdigkeit>10 oder Langeweile>10

    hungrig+gelangweilt --> hungrig: Langeweile<5
    hungrig+gelangweilt --> gelangweilt: Hunger<5

    hungrig+gelangweilt --> tod: Hunger>10 oder Langeweile>10

    müde+hungrig+gelangweilt-->müde+hungrig: Langeweile<5
    müde+hungrig+gelangweilt-->müde+gelangweilt: Hunger<5
    müde+hungrig+gelangweilt-->hungrig+gelangweilt: Müdigkeit<5

    müde+hungrig+gelangweilt-->tod: Müdigkeit>10 oder Hunger>10 oder Langeweile>10


"""

hunger = 0
langeweile = 0
muedigkeit = 0
zustand = "ok"

while True:
    muedigkeit += 1
    hunger += 1
    langeweile += 1

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
    print(zustand)
