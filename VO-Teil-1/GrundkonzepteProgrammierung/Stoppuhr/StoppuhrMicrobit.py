def on_button_pressed_a():
    global timer_gestartet, sekunden
    timer_gestartet = True
    sekunden = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global timer_gestartet
    if timer_gestartet:
        timer_gestartet = False
        basic.show_number(sekunden)
        music.play_melody("F F G A B B B B ", 250)
input.on_button_pressed(Button.B, on_button_pressed_b)

sekunden = 0
timer_gestartet = False
timer_gestartet = False

def on_every_interval():
    global sekunden
    if timer_gestartet:
        sekunden += 1
loops.every_interval(1000, on_every_interval)

def on_every_interval2():
    if timer_gestartet:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
loops.every_interval(1000, on_every_interval2)

def on_forever():
    pass
basic.forever(on_forever)