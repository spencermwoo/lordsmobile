import win32api, win32con

from _settings import *
from _utils import *

# Perhaps scroll screen via drag?

# ==============
# BASE FUNCTIONS
def _mouse_set(coordinates):
    win32api.SetCursorPos(coordinates)

def _mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)

def _open_coordinates():
    _mouse_set(MAGNIFIER_ICON)
    _mouse_click()

# =========
# FUNCTIONS

def button_magnify():
    _open_coordinates()

def button_go():
    _mouse_set(COORDINATE_GO)
    _mouse_click()

def set_x(x):
    _mouse_set(COORDINATE_X)
    _mouse_click()

    calculator(x)

def set_y(y):
    _mouse_set(COORDINATE_Y)
    _mouse_click()

    calculator(y)

def calculator_set_number(value):
    pass

def calculator(value):

    print(value)

    time.sleep(1)
    # parse value into digits
    # input digits calculator_set_number()

    _mouse_set(CALCULATOR[10])
    _mouse_click()

# ===================
# TOP LEVEL FUNCTIONS

def set_coordinates(coordinates):
    button_magnify()

    time.sleep(1)

    set_x(coordinates[0])
    time.sleep(1)

    set_y(coordinates[1])
    time.sleep(1)

    button_go()

def click_mouse_at(coordinates):
    _mouse_set(coordinates)

    time.sleep(1)

    _mouse_click()

def move_mouse_at(coordinates):
    _mouse_set(coordinates)