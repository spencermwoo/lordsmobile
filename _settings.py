CALCULATOR = [(0,0)] * 11

# =======================
# MODIFY BELOW VALUES
# refer to `settings.png`

# WINDOW_TOP_LEFT = (259, 158)
# WINDOW_BOTTOM_RIGHT = (1277, 730)

# 1024 x 576 Resolution

# WINDOW_TOP_LEFT = (449, 229)
# WINDOW_BOTTOM_RIGHT = (1472, 843)

# MAGNIFIER_ICON = (733, 233)
# COORDINATE_X = (768, 365)
# COORDINATE_Y = (876, 369)

# COORDINATE_GO = (762, 461)

# # refer to `CALCULATOR.png`
# CALCULATOR[1] = (948, 393)
# CALCULATOR[9] = (1082, 497)

# # ======

# BAG_OPEN = (1265, 803)
# COMBAT_TAB = (1053, 383)
# LOWEST_SHIELD = (1177, 441)
# BAG_CLOSE = (1435, 295)

# MYSTERY_BOX = (1357, 701)
# MYSTERY_BOX_CLAIM = (961, 691)

# BLUESTACKS 1600 x 900, 240 DPI, Landscape 
WINDOW_TOP_LEFT = (79, 126)
WINDOW_BOTTOM_RIGHT = (1576, 967)

MAGNIFIER_ICON = (781, 235)
COORDINATE_X = (768, 365)
COORDINATE_Y = (876, 369)

COORDINATE_GO = (762, 461)

# refer to `CALCULATOR.png`
CALCULATOR[1] = (948, 393)
CALCULATOR[9] = (1082, 497)

# ======

BAG_OPEN = (1251, 916)
COMBAT_TAB = (973, 298)
LOWEST_SHIELD = (1153, 384)
BAG_CLOSE = (1480, 179)

MYSTERY_BOX = (1374, 757)
MYSTERY_BOX_CLAIM = (828, 748)


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

WINDOW_TOP_RIGHT = (WINDOW_BOTTOM_RIGHT[0], WINDOW_TOP_LEFT[1])
WINDOW_BOTTOM_LEFT = (WINDOW_TOP_LEFT[0], WINDOW_BOTTOM_RIGHT[1])