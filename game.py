import pyautogui as pg
from PIL import ImageGrab
import cv2
import numpy as np
import time

def up(sleep_time):
    time.sleep(sleep_time)
    pg.press("space")
    time.sleep(sleep_time)
    pg.press("down")

def boot():
    template=cv2.imread('cactus.jpg',0)
    template2 = cv2.imread('cactus2.jpg', 0)
    template3 = cv2.imread('cactus3.jpg', 0)
    template4 = cv2.imread('cactus4.jpg', 0)
    template5 = cv2.imread('cactus5.jpg', 0)
    template6 = cv2.imread('bird1.jpg',0)
    flag=0
    sleep_time=0.125
#   site=(140,350,810,500)
    site = (140, 150, 710, 300)  # for google chrome
    while(True):
        printscreen_pil=ImageGrab.grab(bbox=site)
        im=cv2.cvtColor(np.array(printscreen_pil),cv2.COLOR_BGR2RGB)
        temp_im=im[70:150,175:260]
        im_gray=cv2.cvtColor(temp_im,cv2.COLOR_BGR2GRAY)
        res1 = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)
        res5 = cv2.matchTemplate(im_gray, template5, cv2.TM_CCOEFF_NORMED)
        res4 = cv2.matchTemplate(im_gray, template4, cv2.TM_CCOEFF_NORMED)
        res3 = cv2.matchTemplate(im_gray, template3, cv2.TM_CCOEFF_NORMED)
        res2 = cv2.matchTemplate(im_gray, template2, cv2.TM_CCOEFF_NORMED)
        res6 = cv2.matchTemplate(im_gray, template6, cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc1 = np.where(res1 >= threshold)
        loc2 = np.where(res2 >= threshold)
        loc3 = np.where(res3 >= threshold)
        loc4 = np.where(res4 >= threshold)
        loc5 = np.where(res5 >= threshold)
        loc6 = np.where(res6 >= threshold)
        for pt in zip(*loc1[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        for pt in zip(*loc2[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        for pt in zip(*loc3[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        for pt in zip(*loc4[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        for pt in zip(*loc5[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        for pt in zip(*loc6[::-1]):
            flag = 1
            cv2.rectangle(im, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 255), 2)
        if flag==1:
            up(sleep_time)
            flag=0

        #cv2.imshow('window',temp_im)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        sleep_time=sleep_time*0.9996

if __name__=="__main__":
    boot()

