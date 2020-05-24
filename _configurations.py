from _settings import * 

# _settings.py
calc_min_x = CALCULATOR[1][0]
calc_min_y = CALCULATOR[1][1]

calc_x = (int)(CALCULATOR[9][0] - calc_min_x) / 2
calc_y = (int)(CALCULATOR[9][1] - calc_min_y) / 2

CALCULATOR[2] = (calc_min_x + calc_x 			, calc_min_y)
CALCULATOR[3] = (calc_min_x + calc_x + calc_x 	, calc_min_y)

CALCULATOR[4] = (calc_min_x 					, calc_min_y + calc_y)
CALCULATOR[5] = (calc_min_x + calc_x			, calc_min_y + calc_y)
CALCULATOR[6] = (calc_min_x + calc_x + calc_x	, calc_min_y + calc_y)

CALCULATOR[7] = (calc_min_x 					, calc_min_y + calc_y + calc_y)
CALCULATOR[8] = (calc_min_x + calc_x			, calc_min_y + calc_y + calc_y)

CALCULATOR[0] = (calc_min_x + (calc_x / 4), calc_min_y + calc_y + calc_y + calc_y)
CALCULATOR[10] = (calc_min_x + calc_x + calc_x - (calc_x / 4), calc_min_y + calc_y + calc_y + calc_y)

for i in range(0, len(CALCULATOR)):
	CALCULATOR[i] = ((int)(CALCULATOR[i][0]), (int)(CALCULATOR[i][1]))

WINDOW_TOP_RIGHT = (WINDOW_BOTTOM_RIGHT[0], WINDOW_TOP_LEFT[1])
WINDOW_BOTTOM_LEFT = (WINDOW_TOP_LEFT[0], WINDOW_BOTTOM_RIGHT[1])

WIDTH = WINDOW_TOP_RIGHT[0] - WINDOW_BOTTOM_LEFT[0]
HEIGHT = WINDOW_TOP_RIGHT[1] - WINDOW_BOTTOM_LEFT[1]

MID_X = (WIDTH / 2) + WINDOW_BOTTOM_LEFT[0]
MID_Y = (HEIGHT / 2) + WINDOW_BOTTOM_LEFT[1]

LOGGING = True

# _screen.py
MASK_THRESHOLD = [180, 80]
MASK = [255, 255, 255]

# WHITELIST = '^[a-zA-Z0-9\[\]=^ ]$'
WHITELIST = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890\[\]=\^ #\$><'
# BLACLIST = r'~`\'\"'
OEM=3
PSM=6
LANG='eng'

FN_PSSR='screen.jpg'
FN_TMP='tmp.jpg'

# Allow word swap for OCR
# l, 1, I look similiar
PRECISE = False
# True is strict
# False is generous


# Return word if CONTAINS
CONTAINS = True
# True is generous
# False is strict