# I'm aware of convention but I find this more helpful.  I'll format at the end.

def write_file(filename, content, write: bool=True):
    with open(filename,"w" if write else "a", encoding="UTF-8") as file:
        file.write(content)

def log(f):
    def print_log(*args, **kwargs):
        params = ', '.join([str(arg) for arg in args])
        print(f"Running : {f.__name__}({params})")

        ret = f(*args, **kwargs)
        print(f"\t {ret}")

        print(f"Exiting : {f.__name__}({params})")

        return ret

    return print_log

import builtins

def print_flush(*objects, sep='', end='\n', flush=False):
    return builtins.print(objects, sep, end, flush=True)

builtins.__print__ = print_flush

import json
import requests

def get_url(url: str):
    response = requests.get(url)

    return json.loads(response.text)

import pyscreenshot
import time

def take_screenshot(min_x, min_y, max_x, max_y, filename: str=None):
    box = (min_x, min_y, max_x, max_y)
    im = pyscreenshot.grab(bbox=box)

    if not filename:
    	filename = str(int(time.time())) + '.png'

    im.save(filename)

    return filename