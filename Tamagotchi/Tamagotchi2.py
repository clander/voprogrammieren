import time, random

from threading import Timer

tendenzZurMuedigkeit = 60
tendenzZurLangeweile = 50
tendenzZumHunger = 30
zeitTick = 10
timeout = 10

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
    
    if(random.randint(1,100)<tendenzZumHunger):
        hunger = hunger + 1
    if(random.randint(1,100)<tendenzZurLangeweile):
        langeweile = langeweile + 1
    if(random.randint(1,100)<tendenzZurMuedigkeit):
        muedigkeit = muedigkeit + 1

    if hunger > 5:
        print(f"\a____ Ich bin hungrig ... ({hunger}) ____")
    time.sleep(0.5)
    if langeweile > 5:
        print(f"\a____ Ich bin gelangweilt ... ({langeweile}) ____")
    time.sleep(0.5)
    if muedigkeit > 5:
        print(f"\a____ Ich bin müde ... ({muedigkeit}) ____")
    
    aktion = input(f"Was möchtest du mit {name} tun? (1) Spielen (2) Füttern (3) Schlafen lassen (4) nichts? ")
     
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
        break;
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Ich mag nicht mehr dein Haustier sein, ich renne jetzt weg ...")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")