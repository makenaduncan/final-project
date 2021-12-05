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
IMAGE_WEAPON = os.path.join(os.getcwd(), "./batter/assets/greenbox.png")
IMAGE_DETECTIVE = os.path.join(os.getcwd(), "./batter/assets/bluebox.png")
IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")


W_CLUES = open(os.path.join(os.getcwd(), "./batter/game/wclues.txt")).read().splitlines
P_CLUES = open(os.path.join(os.getcwd(), "./batter/game/pclues.txt")).read().splitlines

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

# BALL_X = MAX_X / 2
# BALL_Y = MAX_Y - 125

# BALL_DX = 8
# BALL_DY = BALL_DX * -1

# PADDLE_X = MAX_X / 2
# PADDLE_Y = MAX_Y - 25

DETECTIVE_X = MAX_X / 3
DETECTIVE_Y = MAX_Y -440

WEAPON_X = MAX_X / 3
WEAPON_Y = MAX_Y -375

PEOPLE_X = MAX_X / 3
PEOPLE_Y = MAX_Y -480

# BRICK_WIDTH = 48
# BRICK_HEIGHT = 24

# BRICK_SPACE = 5

# PADDLE_SPEED = 15
BOX_SPEED = 15

# PADDLE_WIDTH = 96
# PADDLE_HEIGHT = 24

# BALL_WIDTH = 24
# BALL_HEIGHT = 24

DETECTIVE_WIDTH = 38
DETECTIVE_HEIGHT = 38

PERSON_WIDTH = 10
PERSON_HEIGHT = 10

WEAPON_WIDTH = 40
WEAPON_HEIGHT = 40