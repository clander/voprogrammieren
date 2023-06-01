input.onLogoEvent(TouchButtonEvent.Touched, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})
input.onGesture(Gesture.Shake, function () {
    timer = 0
    basic.showIcon(IconNames.Happy)
})
let timer = 0
timer = 0
basic.showIcon(IconNames.Meh)
music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
loops.everyInterval(1000, function () {
    timer += 1
    if (timer == 20) {
        for (let index = 0; index < 3; index++) {
            basic.showIcon(IconNames.Happy)
            basic.pause(100)
            basic.showIcon(IconNames.Sad)
        }
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.sad), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 30) {
        for (let index = 0; index < 3; index++) {
            basic.showIcon(IconNames.Surprised)
            basic.pause(100)
            basic.showIcon(IconNames.Asleep)
        }
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.yawn), SoundExpressionPlayMode.UntilDone)
    } else if (timer == 40) {
        basic.showIcon(IconNames.Skull)
        music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.Once)
        basic.pause(1000000)
    }
})
