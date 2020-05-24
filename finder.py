from _move import *
from _screen import *

import sys

@log
def screenshot():
    filename = take_screenshot(WINDOW_TOP_LEFT[0], WINDOW_TOP_LEFT[1], WINDOW_BOTTOM_RIGHT[0], WINDOW_BOTTOM_RIGHT[1], FN_PSSR)
    
    print(f"Created {filename}")

@log
def screen():
    im = take_image(WINDOW_TOP_LEFT[0], WINDOW_TOP_LEFT[1], WINDOW_BOTTOM_RIGHT[0], WINDOW_BOTTOM_RIGHT[1], FN_PSSR)

    return im

def _validate(name):
    name = name.replace(" ","")

    regex = f'^[{WHITELIST}]+$'
    if re.match(regex, name):
        return name
    else:
        raise ValueError('Invalid Name')

def _validate_confidence(name):
    l = len(name)

    low_confidence = ['ol1i']

@log
def validate_name(name):
    name = _validate(name)

    if PRECISE:
        name = _validate_confidence(name)

    return name

def _search_name(name):
    screenshot()
    # im = screen()
    # print(type(im))
    # print(im)

    text = screen_read(name)
    success = False
    for word in text:
        if CONTAINS:
            if name in word:
                success = True
                break
        else:
            if name == word:
                success = True
                break

    if success:
        im = Image.open(FN_TMP)
        im.show()

        return f'Successfully found {name} in {word}'

    # time.sleep(1)
    # get_coordinates()
    # set_coordinates()
    drag(0, False)
    # drag


    # Screen in top left.
    # Repeatedly move right until X + Screen_X > Max_X
    # Move down Y

    # Recursively do this zip zag until match
    # Failure at bottom corner
        # if we're in the bottom corner
        # print("Not Found.")
        # return 

    # return f'NOT FOUND : {name}'
    return _search_name(name)

def finder():
    num_args = len(sys.argv)

    if num_args < 2:
        name = input('Enter name : ')
    elif num_args > 2:
        raise Exception('Invalid Input')
    else:
        name = sys.argv[1]

    print(f'Validating {name}')
    name = validate_name(name)

    time.sleep(5)

    print(f'Searching for {name}')

    print(_search_name(name))

    return

def valid_commands():
    pass

if __name__ == '__main__':
    finder()