import cv2
import pytesseract
import numpy as np

from pytesseract import Output
from matplotlib import pyplot as plt
import re
# from _utils import *

from _configurations import *

def _psm():
    img_name = '1'
    img = img_name + '.jpg'
    for i in range(1,13):
        text = pytesseract.image_to_string(img,lang='eng',config=r'--psm {i}')
        write_file(f'{img_name}{i}.txt', text)

def _bounding_box_naive(image):
    h, w, c = image.shape
    boxes = pytesseract.image_to_boxes(image) 
    for b in boxes.splitlines():
        b = b.split(' ')
        image = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

    b,g,r = cv2.split(image)
    rgb_img = cv2.merge([r,g,b])

    plt.figure(figsize=(16,12))
    plt.imshow(rgb_img)
    plt.title('NAIVE BOUNDING BOX RECOGNITION')
    plt.show()

def _bounding_box(image):
    d = pytesseract.image_to_data(image, output_type=Output.DICT)

    n_boxes = len(d['text'])
    valid_pattern = '^(a-zA-Z0-9\[\]])+$'

    for i in range(n_boxes):
        if int(d['conf'][i]) > 30:
            if re.match(valid_pattern, d['text'][i]):
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    b,g,r = cv2.split(image)
    rgb_img = cv2.merge([r,g,b])

    plt.figure(figsize=(16,12))
    plt.imshow(rgb_img)
    plt.title('CONFIDENCE BOUNDING BOX RECOGNITION')
    plt.show()

# grayscale
def _get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def _remove_noise(image):
    return cv2.medianBlur(image,3)
 
# thresholding
def _thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # return cv2.threshold(image, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# dilation
def _dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
# erosion
def _erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

# erosion followed by dilation
def _opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# canny edge detection
def _canny(image):
    return cv2.Canny(image, 240, 260)

# skew correction
def _deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

# template matching
def _match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# image string
def _stringify(image, whitelist):
    custom_config = f'-l {LANG} --oem {OEM} --psm {PSM} -c tessedit_char_whitelist={whitelist}'
    d = pytesseract.image_to_string(image, config=custom_config)
    return d.split()

# image mask
def _high_mask(image):
    data = np.array(image)

    mask = np.all(image < MASK_THRESHOLD[0], axis=2)
    data[mask] = [0, 0, 0]

    return data

def _mask(image):
    data = np.array(image)

    mask = np.all(image < MASK_THRESHOLD[0], axis=2)
    data[mask] = [255, 255, 255]

    mask = np.all(image > MASK_THRESHOLD[1], axis=2)
    data[mask] = [255, 255, 255]

    return data

def _low_mask(image):
    data = np.array(image)

    mask = np.all(image > MASK_THRESHOLD[1], axis=2)
    data[mask] = [0, 0, 0]

    return data

def _preprocess_alpha(image):
    g = get_grayscale(image)
    t = thresholding(g)
    o = opening(t)
    r = canny(o)
    n = remove_noise(r)

    cv2.imwrite(FN_TMP, n)

def _preprocess(image):
    data = _mask(image)

    # return data
    cv2.imwrite(FN_TMP, data)

def screen_read(whitelist):
# def screen_read(whitelist, im):
    image = cv2.imread(FN_PSSR)
    # image = cv2.imread(im)

    im = _preprocess(image)

    image = cv2.imread(FN_TMP)

    return _stringify(image, whitelist)