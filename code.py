import board
from kmk.extensions.LED import LED
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string as ss
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation

keyboard = KMKKeyboard()
led_ext = LED(
    led_pin=board.GP0,
    brightness_step=5,
    brightness_limit=100,
    breathe_center=1.5,
    animation_mode=3,
    animation_speed=0.1,
    val=100,
)
keyboard.extensions = [led_ext, MediaKeys()]
# keyboard.debug_enabled = True

keyboard.col_pins = (board.GP19, board.GP20, board.GP21)
keyboard.row_pins = (board.GP11, board.GP12, board.GP13)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

GMEET_MIC = KC.LGUI(KC.D)
GMEET_VID = KC.LGUI(KC.E)
send_roll_no = ss("15 ")

keyboard.keymap = [
    [
        KC.LGUI(KC.C),KC.LGUI(KC.V),KC.LGUI(KC.SPC),  # 1st row
        KC.LED_TOG,KC.MPLY,KC.MNXT,  # 2nd Row
        GMEET_VID,GMEET_MIC,send_roll_no,  # 3rd Row
    ]
]

if __name__ == "__main__":
    keyboard.go()
