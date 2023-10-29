# SCHARADE

## Anleitung / Problemstellung

https://makecode.microbit.org/courses/csintro/arrays/activity

## Blöcke
![](./scharademicrobit.png)

## Python Code

```python
def on_button_pressed_a():
    global index
    if index >= 0 and index < len(woerter):
        countdownAnzeigen(3)
        basic.show_string("..." + woerter[index])
        index += 1
    else:
        basic.show_string("Ende")
input.on_button_pressed(Button.A, on_button_pressed_a)

def countdownAnzeigen(startenVon: number):
    global i
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # # .
        . . . . .
        . . # . .
        """)
    basic.pause(200)
    i = startenVon
    while i >= 0:
        basic.pause(100)
        basic.show_number(i)
        i += -1
i = 0
woerter: List[str] = []
index = 0
index = 0
woerter = ["Katze", "Gitarre"]



````
``

