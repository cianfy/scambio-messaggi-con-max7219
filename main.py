def on_received_string(receivedString):
    max7219_matrix.scroll_text(receivedString, 75, 500)
radio.on_received_string(on_received_string)

max7219_matrix.setup(4,
    DigitalPin.P16,
    DigitalPin.P15,
    DigitalPin.P14,
    DigitalPin.P13)
max7219_matrix.for_4_in_1_modules(rotation_direction.CLOCKWISE, False)
radio.set_group(1)
basic.show_icon(IconNames.HEART)
basic.pause(1000)

def on_forever():
    if input.button_is_pressed(Button.A):
        radio.send_string("Ciao !!!")
    if input.button_is_pressed(Button.B):
        radio.send_string("Che bello")
basic.forever(on_forever)
