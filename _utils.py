# I'm aware of convention but I find this more helpful.  I'll format at the end.

quiet = False

def write_file(filename, content, write: bool=True):
    with open(filename,"w" if write else "a", encoding="UTF-8") as file:
        file.write(content)

def log(f):
    def print_log(*args, **kwargs):
        params = ', '.join([str(arg) for arg in args])
        if not quiet:
            print(f"Running : {f.__name__}({params})")

        ret = f(*args, **kwargs)
        if not quiet:
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

import subprocess

def run_process(output, program, cmd, *params):
    if not quiet:
        print("\t" + program + " " + cmd + " " +
              ' '.join(str(x) for x in params[0]), flush=True)

    args = [program] + [cmd] + params[0]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=dir_path)

    if output:
        return process.communicate()[0].decode("UTF-8", "replace")