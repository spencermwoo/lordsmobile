# this should install everything necessary locally

# prerequisite : Python 3.6+
import platform
import sys

print(f'{platform.system()},  {platform.platform()}, {platform.machine()}')
print(f'{platform.uname()}')
print(f'Python {sys.version}')

print('============')

# print("""Python version: %s
# dist: %s
# system: %s
# machine: %s
# platform: %s
# uname: %s
# version: %s
# mac_ver: %s
# """ % (
# sys.version.split('\n'),
# str(platform.dist()),
# platform.system(),
# platform.machine(),
# platform.platform(),
# platform.uname(),
# platform.version(),
# platform.mac_ver(),
# ))

# (0) Check OS
print('Valdiating : OS')
if platform.system() != 'Windows':
	raise ValueError(f'Invalid : Operating System {platform.system()}')

if platform.release() == 'XP':
	raise ValueError(f'Invalid : Release {platform.release()}')	

# (1) Check Python 3.6+
print('Validating : Python')
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
	raise ValueError(f'Invalid : Python {version_info.release()}')

# naive checks for now

# (2) Check pip
print('Validating : Pip')

import subprocess
import os

dir_path = os.getcwd()

def run_process(output, program, cmd, *params):
    args = [program] + [cmd] + params[0]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=dir_path)

    if output:
    	return process.communicate()[0].decode("UTF-8", "replace")

def call_process(output, program, cmd, *params):
    args = [program] + [cmd] + params[0]
    process = subprocess.call(args, stdout=subprocess.PIPE, cwd=dir_path)

# (3) Install pip
def pip_install():
	print('Installing : Pip')

	print('Downloading : https://bootstrap.pypa.io/get-pip.py')
	run_process(False, "curl", "https://bootstrap.pypa.io/get-pip.py", ['-o', 'get-pip.py'])

	print('Running : python get-pip.py')
	run_process(False, "python", "get-pip.py", ['--no-index'])	

def pip_validate():
	try:
		run_process(False, "pip", "--version", [])
		# run_process(False, "python", "-m", ['pip', 'install', '--upgrade', 'pip'])
	except Exception:
		pip_install()

pip_validate()

# (3) Check Python Modules
print('Validating : Python Modules')
# run_process(False, "python", "-m", ['pip', 'install', '--upgrade', 'pip'])
# run_process(False, "python", "-m", ['pip', 'install', '-r', 'requirements.txt'])
call_process(False, "pip", "install", ['-r', 'requirements.txt'])

print('Requirements have been installed.')
print('Run ./setup to setup the program')

# (2) Install pip
	# try:
	# 	run_process("pxxx", "--verszz", [])

	# except FileNotFound:


	#otherwise
	# python -m ensurepip --default-pip

	# #otherwise install pip
	# wget https://bootstrap.pypa.io/get-pip.py
	# python get-pip.py

	# return ''
	# try:
	# 	import pip

	# 	def import_or_install(package):
	# 	    try:
	# 	        __import__(package)
	# 	    except ImportError:
	# 	        pip.main(['install', package])     

	# 	import_or_install('pyscreenshot')
	# 	# import_or_install('pywin32')
	# 	# import_or_install('pillow')
	# 	# import_or_install('opencv-python')
	# 	# import_or_install('pytesseract')
	# 	# import_or_install('image')
	# except Exception:
	# 	raise Exception(f'Requirement : pip')

# # (3) 

# from setuptools import setup

# pip install -r requirements.txt 
# #--no-index --find-links

# setup(
#     name='spam',
#     scripts=['bash_scripts/spam.sh']
# )
# pip install pyscreenshot
# pip install pywin32
# pip install pillow
# pip install opencv-python
# pip install pytesseract
# pip install image

# Set tesseract path

# pip install numpy
# pip install pytesseract
# pip install mss
# pip install opencv-python

# pip install python3
# pip install

# (4) Optionally