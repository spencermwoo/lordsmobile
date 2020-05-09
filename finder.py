from _move import *
from _screen import *

def screenshot():
    print("Taking screenshot in 5 seconds.")
    time.sleep(5)

    filename = take_screenshot(WINDOW_TOP_LEFT[0], WINDOW_TOP_LEFT[1], WINDOW_BOTTOM_RIGHT[0], WINDOW_BOTTOM_RIGHT[1])

    print(f"Created {filename}")

def _validate(name):
    name = name.replace(" ","")

    regex = f'^[{CHAR_WHITELIST}]+$'
    if re.match(regex, name):
        return name
    else:
        raise ValueError('Invalid Name')

def _validate_confidence(name):
    l = len(name)

    low_confidence = ['ol1i']

def validate_name(name):
    _validate(name)

    if PRECISE:
        name = _validate_confidence(name)

    return name

def _search_name(name):
    screenshot()

    text = screen_read()

    for word in text:
        if CONTAINS:
            if name in word:
                return f'Successfully found {name}'
        else:
            if name == word:
                return f'Successfully found {name}'

    # Screen in top left.
    # Repeatedly move right until X + Screen_X > Max_X
    # Move down Y

    # Recursively do this zip zag until match
    # Failure at bottom corner
        # if we're in the bottom corner
        # print("Not Found.")
        # return 

    return
    # return _search_name(name)

def finder():
    print("Running finder().")

    name = 'thanksmom'
    name = validate_name(name)

    print(_search_name(name))

    return

def valid_commands():
    pass

if __name__ == '__main__':
    finder()