import time

counter = 10
print("DER COUNTDOWN LÄUFT ... ")
while counter > 0:
    if counter == 3:
        print("DREI")
    elif counter == 2:
        print("Z W E I")
    elif counter == 1:
        print("E  I  N  S")
    else:
        print(counter)
    counter = counter - 1
    time.sleep(1)
print("... VÖLLIG LOSGELÖST ...")