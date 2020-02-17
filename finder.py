from _move import *

def screenshot():
	print("Taking screenshot in 5 seconds.")
	time.sleep(5)

	filename = take_screenshot(WINDOW_TOP_LEFT[0], WINDOW_TOP_LEFT[1], WINDOW_BOTTOM_RIGHT[0], WINDOW_BOTTOM_RIGHT[1])

	print(f"Created {filename}")

def finder():
	print("Running finder().")

	# Screen in top left.
	# Repeatedly move right until X + Screen_X > Max_X
	# Move down Y

	# Recursively do this zip zag until match
	# Failure at bottom corner

	print("Not Found.")

def valid_commands():
	pass

if __name__ == '__main__':
    finder()