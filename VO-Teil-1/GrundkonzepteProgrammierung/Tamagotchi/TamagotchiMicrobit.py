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