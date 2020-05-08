# This should help walkthrough using `_polling.py`

# Perhaps this should generate `_settings.py`?

# Perhaps this should run `requirements.py`?

from _polling import *

# setup _settings.py for screenFinder
# do polling

# The number of repetitions before confirming value.
REPEAT_MAX = 5;
REPEAT_VAL = REPEAT_MAX;


def _setupWindow():

def _setSetting(setting: str):
	print(f'SET : {setting}')

	val = _confirmPolling

	print(f'CONFIRM : {setting}')

	return val

def _confirmPolling():
	VAL = _get_coordinates()

	while REPEAT_VAL > 0:
		time.sleep(.5)
		TMP = _get_coordinates()
		print(TMP)

		if VAL == TMP:
			REPEAT_VAL -= 1
		else:
			REPEAT_VAL = REPEAT_MAX

	return VAL

def configureScreenFinder():
