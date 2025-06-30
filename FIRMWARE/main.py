import board 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.combos import Combos, Chord, Sequence

combos = Combos()

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

keyboard.modules.append(combos)

make_key(
    names=('MYKEY',),
    on_press=lambda *args: print('I pressed MYKEY'),
)

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.D0]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    #WORK HARD 1
    [
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.LCTL(KC.F),
        KC.TAB,
        KC.ENT,
        KC.LSFT,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.RIGHT,
    ],
    
    #WORK HARD 2
    [
        KC.MACRO("print"),
        KC.MACRO("input"),
        KC.MACRO("while"),
        KC.MACRO(Tap(KC.F4,KC.ALT)),
        KC.CTL,
        KC.HOME,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.DOWN,          
    ],
    #PLAY HARD 1
    [
        KC.Q,
        KC.W,
        KC.E,
        KC.Z,
        KC.X,
        KC.C,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.RIGHT,
    ],
    
    #PLAY HARD 2
    [
        KC.I,
        KC.O,
        KC.P,
        KC.J,
        KC.K,
        KC.L,
        KC.S,
        KC.A,
        KC.W,
        KC.D,          
    ]
]

combos.combos = [
    Chord((KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.LCTL(KC.F),
        KC.TAB,
        KC.ENT,
        KC.LSFT,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.RIGHT,), KC.TG(1)),
    
    Chord((KC.MACRO("print"),
        KC.MACRO("input"),
        KC.MACRO("while"),
        KC.MACRO(Tap(KC.F4,KC.ALT)),
        KC.CTL,
        KC.HOME,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.DOWN,), KC.TG(2)),
    
    Chord((KC.Q,
        KC.W,
        KC.E,
        KC.Z,
        KC.X,
        KC.C,
        KC.DOWN,
        KC.LEFT,
        KC.UP,
        KC.RIGHT,), KC.TG(3)),
    
    Chord((KC.I,
        KC.O,
        KC.P,
        KC.J,
        KC.K,
        KC.L,
        KC.S,
        KC.A,
        KC.W,
        KC.D, ), KC.TG(4)),
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()