def on_logo_touched():
    global timer
    timer = 0
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_gesture_shake():
    global timer
    timer = 0
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

timer = 0
timer = 0
basic.show_icon(IconNames.MEH)
music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),SoundExpressionPlayMode.UNTIL_DONE)

def on_every_interval():
    global timer
    timer += 1
    if timer == 20:
        basic.show_icon(IconNames.SAD)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad), SoundExpressionPlayMode.UNTIL_DONE)
    elif timer == 30:
        basic.show_icon(IconNames.SURPRISED)
        basic.show_icon(IconNames.ASLEEP)
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),SoundExpressionPlayMode.UNTIL_DONE)
    elif timer == 40:
        basic.show_icon(IconNames.SKULL)
        music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
        basic.pause(1000000)
loops.every_interval(1000, on_every_interval)