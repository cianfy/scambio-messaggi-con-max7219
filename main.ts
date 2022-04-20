input.onButtonPressed(Button.A, function () {
    radio.sendString("Ciao !!!")
})
radio.onReceivedString(function (receivedString) {
    max7219_matrix.scrollText(
    receivedString,
    75,
    500
    )
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("Che bello")
})
max7219_matrix.setup(
4,
DigitalPin.P16,
DigitalPin.P15,
DigitalPin.P14,
DigitalPin.P13
)
max7219_matrix.for_4_in_1_modules(
rotation_direction.clockwise,
false
)
radio.setGroup(1)
basic.showIcon(IconNames.Heart)
basic.pause(1000)
basic.forever(function () {
	
})
