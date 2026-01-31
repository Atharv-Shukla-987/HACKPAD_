import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Pin mapping based on your schematic
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Define your shortcuts
# Note: Key 7 and 8 use 'Sequences' for "Ctrl+M then B/I"
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
VS_CMD = KC.LCTL(KC.LSFT(KC.P))
VS_OPEN = KC.LCTL(KC.P)
ML_RUN = KC.LSFT(KC.ENT)
ML_ALL = KC.LCTL(KC.F9)
ML_NEW = KC.LCTL(KC.M, KC.B)  # Ctrl+M, then B
ML_KILL = KC.LCTL(KC.M, KC.I) # Ctrl+M, then I
TASK_V = KC.LGUI(KC.TAB)
CLIP_H = KC.LGUI(KC.V)
RE_TAB = KC.LCTL(KC.LSFT(KC.T))
ALT_TAB = KC.LALT(KC.TAB)

keyboard.keymap = [
    [
        COPY,   PASTE,  VS_CMD, VS_OPEN, # Row 1
        ML_RUN, ML_ALL, ML_NEW, ML_KILL, # Row 2
        TASK_V, CLIP_H, RE_TAB, ALT_TAB, # Row 3
        KC.NO,  KC.NO,  KC.NO,  KC.NO    # Row 4 (Empty)
    ]
]

if __name__ == '__main__':
    keyboard.go()
