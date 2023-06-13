WIDTH = 1280
HEIGHT = 720
FPS = 30
BLACK = (0, 0, 0)
BACKGROUND = BLACK
SMALL_NONZERO_VALUE = 10**-6  # used to prevent division by zero
SPEED_SENSITIVITY = .1  # used to scale the speed of the player
PLAYER_ENEMY_SIZE = (30, 30)
RANDOMIZED_MATRIX_COUNT = 5  # number of randomized placement matrices to generate
ENEMY_SPEED = 2
ENEMY_SPAWN_X_RANGE = 25  # how far from the sides of the screen the enemy can spawn
# how far from the top of the screen the enemy must spawn
ENEMY_SPAWN_Y_MIN = -PLAYER_ENEMY_SIZE[1]
# the enemy can spawn up to this many times the sprite size above the top of the screen
ENEMY_SPAWN_AREA = 5
# how far from the top of the screen the enemy can spawn
ENEMY_SPAWN_Y_MAX = -PLAYER_ENEMY_SIZE[1] * ENEMY_SPAWN_AREA
ENEMY_POS_DISPLACEMENT = 40  # minimum gap between enemies
PLAYER_MAX_SPEED = 5
PLAYER_GAMEPLAY_AREA = 100  # how far from the bottom of the screen the player can move
PLAYER_MAX_HEIGHT = HEIGHT-PLAYER_GAMEPLAY_AREA
# in agario style movement, this is where you put the cursor to avoid moving anywhere
PLAYER_CENTER_AREA = 5
# blinking is to be done at the start of a wave
BLINK_TIMES = 3
BLINK_DURATION = 500
# flashing is to be done when the player dies
FLASH_TIMES = 4
FLASH_DURATION = 100
# scales how many enemies the player can face per wave, range is (0,1]
DIFFICULTY = .1
REGULAR_BULLET_SIZE = (3, 10)
REGULAR_BULLET_SPEED = 40
