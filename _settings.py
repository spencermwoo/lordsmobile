CALCULATOR = [(0,0)] * 11

# =======================
# MODIFY BELOW VALUES
# refer to `settings.png`

WINDOW_TOP_LEFT = (259, 158)
WINDOW_BOTTOM_RIGHT = (1277, 730)

MAGNIFIER_ICON = (733, 233)
COORDINATE_X = (768, 365)
COORDINATE_Y = (876, 369)

COORDINATE_GO = (762, 461)

# refer to `CALCULATOR.png`
CALCULATOR[1] = (948, 393)
CALCULATOR[9] = (1082, 497)

# refer to `settings.png`
# MODIFY ABOVE VALUES
# =======================

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