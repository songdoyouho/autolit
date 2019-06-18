from PIL import ImageGrab, ImageChops, Image
import numpy as np
import cv2
import win32gui
import pyautogui
import time
import sys

#666

#要算相對距離
hwnd = win32gui.FindWindow(None, '夜神模擬器')
# 606,125 1090,957 left_x, left_y, right_x, right_y
# 寬  高   寬  高
# 0, 0    484, 832  
# 254,55,155 pink

# 483 41 898 759

try :
    left_x, left_y, right_x, right_y = win32gui.GetWindowRect(hwnd)
    print(left_x, left_y, right_x, right_y)
except :
    print("找不到視窗")

box_x = right_x - left_x
box_y = right_y - left_y

def display_img(x):
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    img_np[:, x, :] = 255
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("screen box", frame)
    cv2.waitKey(0)

#  415 718 box_x,box_y

#display_img(28) # 夜神 bar
#display_img(51) # android bar
#display_img(99) # 動態牆 bar 99/718=0.13788
#display_img(199) # 限時動態 bar 199/718=0.27715
#display_img(10) # 限時動態 左標 10/415=0.02409
#display_img(60) # 限時動態 右標 60/415=0.14457

#display_img(443) # add 上標 443/718=0.61699
#display_img(484) # add 下標 484/718=0.67409
#display_img(15) # add 左標 15/415=0.03614
#display_img(55) # add 右標 55/415=0.13253
#display_img(668) # 下 bar 668/718=0.93036

#display_img(75) # 加為好友 上標 75/718=0.10445
#display_img(110) # 加為好友 下標 110/718=0.1532
#display_img(15) # 加為好友 左標 15/415=0.03614
#display_img(50) # 加為好友 右標 50/415=0.12048
#display_img(673) # 加為好友 bar 673/718=0.93732

#display_img(685) # 愛心 上標 685/718=0.95403
#display_img(700) # 愛心 下標 700/718=0.97493
#display_img(384) # 愛心 左標 384/415=0.9253
#display_img(400) # 愛心 右標 400/415=0.96385

#display_img(685) # 愛心 上標 685/718=0.95403
#display_img(700) # 愛心 下標 700/718=0.97493
#display_img(343) # send 左標 343/415=0.8265
#display_img(359) # send 右標 359/4150.86506
#pyautogui.moveTo(left_x + int((box_x*0.02409+box_x*0.14457)/2) , left_y + int((box_y*0.27715+box_y*0.13788)/2) ) # 限時動態頭像
#pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.13253)/2) , left_y + int((box_y*0.61699+box_y*0.67409)/2) ) # 主頁加好友頭像
#pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.12048)/2) , left_y + int((box_y*0.10445+box_y*0.1532)/2) ) # 下一個好友頭像
#pyautogui.moveTo(left_x + int((box_x*0.9253+box_x*0.96385)/2) , left_y + int((box_y*0.95403+box_y*0.97493)/2) ) # 愛心
#pyautogui.moveTo(left_x + int((box_x*0.8265+box_x*0.86506)/2) , left_y + int((box_y*0.95403+box_y*0.97493)/2) ) # send
#pyautogui.moveTo(left_x + int(box_x/2) , left_y + int((box_y*0.93732+box_y)/2) ) # 加為好友 bar
