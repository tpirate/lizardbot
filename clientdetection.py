## function to detect enemy champions

# imports
# from __future__ import print_function
import numpy as np
import cv2
from mss import mss
import numpy as np

# screen recording props
bounding_box = {'top': 0, 'left': 0, 'width': 1919, 'height': 1079}

# template for champ
# template = cv2.imread('temminion2.png',0)
# w, h = template.shape[::-1]
# # template for minion
template = cv2.imread('templates/client/client.png',0)
w, h = template.shape[::-1]
threshold = 0.8
# breaking while loop after 8 seconds
# endTime = datetime.datetime.now() + datetime.timedelta(seconds=10)

# def get_templates(path='./templates', template_mask='png'):
#     for f in glob.glob(os.path.join(path, '**', '*.' + template_mask)):
#         yield cv2.imread(f, 0)


def clienton():
    
    sct = mss()
    # break loop if time has come
    # record screen
    sct_img = sct.grab(bounding_box)
    # convert to numpy to use in opencv
    img = np.array(sct_img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #  az canli dusmanlar anlasilmiyor
    # takim arkadaslari da anlasiliyor
    # tresholddan dolayi yanlis anladigi oluyor
    # template matching
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold )
    #  print(loc)
    chcoord = []
    for pt in zip(*loc[::-1]):
        chcoord.append([pt[1], pt[0]]) 
        
        # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    if chcoord:
        return True
    else: 
        return False
    # if chcoord:
    #     print(chcoord)
    #     return chcoord
    # cv2.imshow('screen', np.array(sct_img))
    


if __name__ == "__main__":
    clienton()