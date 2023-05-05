def on_button_pressed_a():
    global zufallBuchstabe
    if len(alphabet) > 0:
        zufallBuchstabe = alphabet.remove_at(randint(0, len(alphabet) - 1))
        basic.show_string("" + (zufallBuchstabe))
        basic.pause(5000)
        basic.show_leds("""
            . . # . .
                        . # # . .
                        # # # . .
                        . # # . .
                        . . # . .
        """)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

zufallBuchstabe = ""
alphabet: List[str] = []
basic.show_leds("""
    . . # . .
        . # # . .
        # # # . .
        . # # . .
        . . # . .
""")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]