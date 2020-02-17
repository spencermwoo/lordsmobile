import builtins

def print_flush(*objects, sep='', end='\n', flush=False):
    return builtins.print(objects, sep, end, flush=True)

builtins.__print__ = print_flush

def write_file(filename, content, write: bool=True):
    with open(filename,"w" if write else "a", encoding="UTF-8") as file:
        file.write(content)

import json
import requests

def get_url(url: str):
    response = requests.get(url)

    return json.loads(response.text)

import pyscreenshot
import time

def screenshot(min_x, min_y, max_x, max_y, filename: str=None):
    box = (min_x, min_y, max_x, max_y)
    im = pyscreenshot.grab(bbox=box)

    if not filename:
    	filename = str(int(time.time())) + '.png'

    im.save(filename)