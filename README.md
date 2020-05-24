# lordsmobile

[1](/assets/naive2.png)
[2](/assets/orange.png)
[3](/assets/orange_pp.png)

This project is functional however it is not possible to search the entire kingdom via UI in the time frame I desired.  I've discontinued this project.

# Index
1. Lords Mobile
	- [Introduction](#introduction)

2. Usage
	- [Setup](#setup)
	- [Usage](#run)
3. Credits
	- [Developers](#developers)
	- [License](#license)
	- [Reference](#reference)

# Set Up

### <a id="introduction"></a>Introduction

Problem : Searching in a Kingdom is difficult and not supported.

Goal : Input `text` and this will search the Kingdom for `text`.

Examples : 

* (1) Phantom Knight
* (2) `[G1K] thanksmom` is being rallied

### <a id="setup"></a>Setup

Requirements : Windows, Python 3.6+

Run `configure.py` to 
* (1) Install requirements
* (2) Validate requirements
* (3) Generate settings `_settings.py`

`python3 configure.pwc`

<!-- 1. Install requirements `./requirements.pyw` -->
<!-- 2. Gather configuration values with `./configuration.py` -->

### <a id="usage"></a>Usage

Run `finder.py`

`python3 finder.py`

# Credits

### <a id="developers"></a>Developers

### <a id="license"></a>License

This is released under [GNU General Public License v3.0](#LICENSE).  

A copy is provided in this repository however if for some reason it is absent, it can be viewed [here](https://www.gnu.org/licenses/gpl-3.0.txt).

### <a id="reference"></a>Reference

* https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117
* https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/