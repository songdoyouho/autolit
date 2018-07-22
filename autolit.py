from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
import pyautogui
import time


hwnd = win32gui.FindWindow(None, '夜神模擬器')
# 254,55,155 pink BGR
   
try :
    left_x, left_y, right_x, right_y = win32gui.GetWindowRect(hwnd)
    print(left_x, left_y, right_x, right_y)
except :
    print("找不到視窗")

box_x = right_x - left_x
box_y = right_y - left_y

def display_img(y, x):
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    img_np[y, x, :] = 255
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("screen box", frame)
    cv2.waitKey(0)

def click_like_button():
    pyautogui.moveTo(left_x + int((box_x*0.9253+box_x*0.96385)/2) , left_y + int((box_y*0.95403+box_y*0.97493)/2) ) # 愛心
    pyautogui.click()

def check_liked_or_not(flaggg):
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    heart = img_np[int(box_y*0.95403):int(box_y*0.97493), int(box_x*0.9253):int(box_x*0.96385), :]
    #frame = cv2.cvtColor(heart, cv2.COLOR_BGR2RGB)
    #cv2.imshow("screen box", frame)
    heart_size = heart.shape
    #print(heart_size[0])
    #cv2.waitKey(0)
    counter = 0
    #thr = int(heart_size[0] * heart_size[1])
    for i in range(heart_size[0]):
        for j in range(heart_size[1]):
            tmp1=heart[i, j, 0]
            tmp2=heart[i, j, 1]
            tmp3=heart[i, j, 2]
            #print(tmp1,tmp2,tmp3)
            if tmp1 == 254 and tmp2 == 55 and tmp3 == 155:
                counter += 1
    #print(counter)
    if counter > 100:
        flaggg = True # 有按過愛心

    return flaggg

def click_next_video():
    pyautogui.moveTo(right_x - 15, right_y - int(box_y/2)) # 1065, 541
    pyautogui.click()

def check_end_or_not(flaggg):
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    heart = img_np[int(box_y*0.95403):int(box_y*0.97493), int(box_x*0.9253):int(box_x*0.96385), :]
    #frame = cv2.cvtColor(heart, cv2.COLOR_BGR2RGB)
    #cv2.imshow("screen box", frame)
    heart_size = heart.shape
    #print(heart_size[0])
    #cv2.waitKey(0)
    counter = 0
    thr = int(heart_size[0]*heart_size[1])
    for i in range(heart_size[0]):
        for j in range(heart_size[1]):
            tmp1=heart[i, j, 0]
            tmp2=heart[i, j, 1]
            tmp3=heart[i, j, 2]
            #print(tmp1,tmp2,tmp3)
            if tmp1 < 100 and tmp2 < 100 and tmp3 < 100:
                counter += 1
    #print(counter)
    if counter > (thr - 30):
        flaggg = False
    #print(flaggg)
    return flaggg

def click_first_video():    
    pyautogui.moveTo(left_x + int((box_x*0.02409+box_x*0.14457)/2) , left_y + int((box_y*0.27715+box_y*0.13788)/2) )
    pyautogui.click()
    time.sleep(2)
    like = None
    like = check_liked_or_not(like)
    if like == True:
        click_next_video()
        time.sleep(2)
    else:
        click_like_button()
        time.sleep(1)
        click_next_video()
        time.sleep(2)

def add_friends_init():
    pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.13253)/2) , left_y + int((box_y*0.61699+box_y*0.67409)/2) )
    pyautogui.click()
    time.sleep(2)
    #display_img(545, 44)
    pyautogui.moveTo(left_x + int(box_x/2) , left_y + int((box_y*0.93732+box_y)/2) )
    pyautogui.click()

def add_friends():
    for num in range(9):
        pyautogui.moveTo(left_x + int(box_x/2), left_y + int(box_y/2)) # middle
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(right_x - 15, left_y + int(box_y/2)) # slide to next person
        pyautogui.dragRel(-300,0,1)
        time.sleep(2)
        pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.12048)/2) , left_y + int((box_y*0.10445+box_y*0.1532)/2) )
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(left_x + int(box_x/2) , left_y + int((box_y*0.93732+box_y)/2) )
        pyautogui.click()
        time.sleep(0.5)
     
    pyautogui.moveTo(left_x + int(box_x*0.95041), left_y + int(box_y*0.11418)) # 645, 230 460/484=0.95041 95/832=0.11418
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

def check_error_next(): # 暫時還沒寫好 如果網路太慢，會黑幕導致程式中斷
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    tmp = img_np[793:793+25,209:209+67,:] # 把有字的地方框出來
    frame = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
    #v2.imshow("screen box", frame)
    #cv2.waitKey(0)
    #cv2.imwrite("black.jpg", frame)
    cv2.imwrite("black1.jpg", frame)
        
    black = cv2.imread("black.jpg")
    black1 = cv2.imread("black1.jpg")
    # compare pixel
    count = 0
    for i in range(67):
        for j in range(25):
            pixel1 = black[j, i, 1]
            pixel2 = black1[j, i, 1]
            if pixel1 == pixel2:
                continue
            else:
                count += 1
        
    if count == 0:
        pyautogui.moveTo(left_x + 242 + 200, left_y + 416) # slide to next person
        pyautogui.dragRel(-int(box_x/3*2), 0, 1)
        time.sleep(2)


print("輸入1, 加10個好友")
print("輸入2, 自動按讚, 但是網路要夠快")
print("輸入3, 離開")
main_flag = True
while main_flag:
    input_order = input("please enter order:")
    if input_order == str(1):
        add_friends_init()
        add_friends()
    elif input_order == str(2):
        click_first_video()
        flag = True
        while flag:
            like = None
            like = check_liked_or_not(like)
            if like == True:
                click_next_video()
                time.sleep(2)
                #check_error_next()
                flag = check_end_or_not(flag)
            else:
                click_like_button()
                time.sleep(1)
                click_next_video()
                time.sleep(2)
                #check_error_next()
                flag = check_end_or_not(flag)
    elif input_order == str(3):
        main_flag = False
        print("Thank you! 888")
