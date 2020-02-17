import builtins
import json
import requests

def print_flush(*objects, sep='', end='\n', flush=False):
    return builtins.print(objects, sep, end, flush=True)

builtins.__print__ = print_flush

def write_file(filename, content, write=True):
    with open(filename,"w" if write else "a", encoding="UTF-8") as file:
        file.write(content)

def get_url(url: str):
    response = requests.get(url)

    return json.loads(response.text)