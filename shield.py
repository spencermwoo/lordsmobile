from _move import *
# import threading
# from _utils import *
import time

def screenshot():
    print("Taking screenshot in 5 seconds.")
    time.sleep(5)

    filename = take_screenshot(WINDOW_TOP_LEFT[0], WINDOW_TOP_LEFT[1], WINDOW_BOTTOM_RIGHT[0], WINDOW_BOTTOM_RIGHT[1])

    print(f"Created {filename}")

def activateShield():
	print("CLICKING : BAG_OPEN")
	click_mouse_at(BAG_OPEN)

	print("CLICKING : COMBAT_TAB")
	click_mouse_at(COMBAT_TAB)

	print("CLICKING : LOWEST_SHIELD")
	click_mouse_at(LOWEST_SHIELD)

	print("CLICKING : BAG_CLOSE")
	click_mouse_at(BAG_CLOSE)
	# click_mouse_at(LOWEST_SHIELD)


def shield():
	print("CLICKING : SHIELD")

	time.sleep(5)
	# screenshot()

	# (1) Naive
	# Shield when expired
	# recurringly run every 4 hours
	activateShield()

	# (2) Smart
	# determine if being attacked...

	# (3) Ideal
	# Shield when attacked by X 4Ts

	# Screen in top left.
	# Repeatedly move right until X + Screen_X > Max_X
	# Move down Y

	# Recursively do this zip zag until match
	# Failure at bottom corner

	print("Complete.")
	time.sleep(5)

def mystery_box():
	# every hour
	print("CLICKING : MYSTERY BOX")
	time.sleep(5)
	click_mouse_at(MYSTERY_BOX)

	click_mouse_at(MYSTERY_BOX_CLAIM)


def controller():
	starttime=time.time()
	seconds_in_ten=605.0	#600
	count_til_shield = 22
	while True:

		mystery_box()
 
		count_til_shield -= 1
		if count_til_shield == 0:
			shield()
			count_til_shield = 24

		time.sleep(seconds_in_ten - ((time.time() - starttime) % seconds_in_ten))

	# threading.Timer(60, mystery_box).start()

	# threading.Timer(240, shield).start()

def valid_commands():
	pass

if __name__ == '__main__':
	# screenshot()
    controller()