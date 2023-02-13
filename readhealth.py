from os import name
import cv2
import pytesseract
from mss import mss
import numpy as np
from time import sleep
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


sct = mss()

def readhealth2():
    bounding_box = {'top': 685 , 'left': 420  , 'width': 100 , 'height': 15}
    # print(bounding_box) 
    sct_img = sct.grab(bounding_box)
    # convert to numpy to use in opencv
    img = np.array(sct_img)
    # cv2.imshow('sa', img)
    # cv2.waitKey(0)
    text = pytesseract.image_to_string(img)
    # print(text)
    return text

if __name__ == "__main__":
    readhealth2()