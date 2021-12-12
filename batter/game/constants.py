import os

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

BACKGROUND_COLOR = COLOR_BLACK

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_PERSON = os.path.join(os.getcwd(), "./batter/assets/redbox.png")
IMAGE_MUSTARD = os.path.join(os.getcwd(), "./batter/assets/mustard.png")
IMAGE_PLUM = os.path.join(os.getcwd(), "./batter/assets/plum.png")
IMAGE_GREEN = os.path.join(os.getcwd(), "./batter/assets/green.png")
IMAGE_PEACOCK = os.path.join(os.getcwd(), "./batter/assets/peacock.png")
IMAGE_SCARLET = os.path.join(os.getcwd(), "./batter/assets/scarlet.png")
IMAGE_WHITE = os.path.join(os.getcwd(), "./batter/assets/white.png")

IMAGE_WEAPON = os.path.join(os.getcwd(), "./batter/assets/weapon.jpg")
IMAGE_KNIFE = os.path.join(os.getcwd(), "./batter/assets/knife.png")
IMAGE_ROPE = os.path.join(os.getcwd(), "./batter/assets/rope.png")
IMAGE_PISTOL = os.path.join(os.getcwd(), "./batter/assets/pistol.png")
IMAGE_CANDLESTICK = os.path.join(os.getcwd(), "./batter/assets/candlestick.png")
IMAGE_POISON = os.path.join(os.getcwd(), "./batter/assets/poison.png")
IMAGE_AXE = os.path.join(os.getcwd(), "./batter/assets/axe.png")
IMAGE_WRENCH = os.path.join(os.getcwd(), "./batter/assets/wrench.png")
IMAGE_HORSESHOE = os.path.join(os.getcwd(), "./batter/assets/horseshoe.png")

IMAGE_DETECTIVE = os.path.join(os.getcwd(), "./batter/assets/detective.png")


W_CLUES = open(os.path.join(os.getcwd(), "./batter/game/wclues.txt")).read().splitlines
P_CLUES = open(os.path.join(os.getcwd(), "./batter/game/pclues.txt")).read().splitlines

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

DETECTIVE_X = MAX_X / 3
DETECTIVE_Y = MAX_Y -440

WEAPON_X = MAX_X / 3
WEAPON_Y = MAX_Y -375

PEOPLE_X = MAX_X / 3
PEOPLE_Y = MAX_Y -480

BOX_SPEED = 8

DETECTIVE_WIDTH = 38
DETECTIVE_HEIGHT = 38

PERSON_WIDTH = 10
PERSON_HEIGHT = 10

WEAPON_WIDTH = 40
WEAPON_HEIGHT = 40