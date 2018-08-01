from PIL import ImageGrab
import numpy as np
import cv2
import win32gui
import pyautogui
import time

pyautogui.FAILSAFE = True
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
    #cv2.waitKey(0)
    counter = 0
    for i in range(heart_size[0]):
        for j in range(heart_size[1]):
            tmp1=heart[i, j, 0]
            tmp2=heart[i, j, 1]
            tmp3=heart[i, j, 2]
            if tmp1 == 254 and tmp2 == 55 and tmp3 == 155:
                counter += 1

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
    #cv2.waitKey(0)
    counter = 0
    thr = int(heart_size[0]*heart_size[1])
    for i in range(heart_size[0]):
        for j in range(heart_size[1]):
            tmp1=heart[i, j, 0]
            tmp2=heart[i, j, 1]
            tmp3=heart[i, j, 2]
            if tmp1 < 100 and tmp2 < 100 and tmp3 < 100:
                counter += 1

    if counter > (thr - 30):
        flaggg = False

    return flaggg

def click_first_video():    
    pyautogui.moveTo(left_x + int((box_x*0.02409+box_x*0.14457)/2) , left_y + int((box_y*0.27715+box_y*0.13788)/2) )
    pyautogui.click()
    time.sleep(1)
    like = None
    like = check_liked_or_not(like)
    if like == True:
        click_next_video()
        time.sleep(1)
    else:
        click_like_button()
        time.sleep(0.5)
        click_next_video()
        time.sleep(1)

def add_friends_init():
    pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.13253)/2) , left_y + int((box_y*0.61699+box_y*0.67409)/2) )
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(left_x + int(box_x/2) , left_y + int((box_y*0.93732+box_y)/2) )
    pyautogui.click()

def add_friends():
    for _ in range(9):
        pyautogui.moveTo(left_x + int(box_x/2), left_y + int(box_y/2)) # middle
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(right_x - 15, left_y + int(box_y/2)) # slide to next person
        pyautogui.dragRel(-300,0,1)
        time.sleep(1)
        pyautogui.moveTo(left_x + int((box_x*0.03614+box_x*0.12048)/2) , left_y + int((box_y*0.10445+box_y*0.1532)/2) )
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(left_x + int(box_x/2) , left_y + int((box_y*0.93732+box_y)/2) )
        pyautogui.click()
        time.sleep(0.5)
     
    pyautogui.moveTo(left_x + int(box_x*0.95041), left_y + int(box_y*0.11418)) # 645, 230 460/484=0.95041 95/832=0.11418
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()

def check_dead_or_not():
    img = ImageGrab.grab(bbox = (left_x, left_y, right_x, right_y))
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #cv2.imshow("screen box", frame)
    count = 0
    img_size = img_np.shape
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            if img_np[i, j, 0] == 0 and img_np[i, j, 1] == 0 and img_np[i, j, 2] == 0:
                count += 1

    if count > img_size[0]*img_size[1]/4*3:
        click_next_video()
        time.sleep(2)
    else:
        pass

def send_some_words(input_send_message):
    pyautogui.moveTo((left_x + right_x)/2 , left_y + int((box_y*0.95403+box_y*0.97493)/2) ) # 愛心
    pyautogui.click()
    pyautogui.typewrite(input_send_message)
    pyautogui.moveTo(left_x + int((box_x*0.8265+box_x*0.86506)/2) , left_y + int((box_y*0.95403+box_y*0.97493)/2) ) # send
    pyautogui.click()


# main
print("輸入1, 加10個好友")
print("輸入2, 自動按讚")
print("輸入3, 1 + 2")
print("輸入4, 1 + 2 但是沒有傳訊息")
print("輸入5, exit")
main_flag = True
while main_flag:
    input_order = input("please enter order:")
    if input_order == str(1): # add friends
        add_friends_init()
        add_friends()

    elif input_order == str(2): # like the posts and send message
        input_send_number = input("你想要傳多少次訊息：")
        input_post_number = input("你想要隔幾篇限時動態傳一次訊息：")
        input_send_message = input("你想要傳什麼訊息：")

        # check if user want to use default or not
        if len(input_post_number) == 0 and len(input_send_number) == 0 and len(input_send_message) == 0:
            print("use default settings!")
            input_send_number = 15
            input_post_number = 50
            input_send_message = "Liked! Please like my posts! Thanks!"

        click_first_video()
        flag = True
        post_counter = 0
        send_counter = 0
        while flag:
            like = None
            like = check_liked_or_not(like)
            if like == True:
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)
            else:
                click_like_button()
                time.sleep(0.5)
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)

            post_counter += 1
            if post_counter == int(input_post_number):
                send_some_words(input_send_message)
                send_counter += 1
                post_counter = 0
            
            if send_counter == int(input_send_number): # to avoid be banned
                break

    elif input_order == str(3): # add friends and like the posts
        input_send_number = input("你想要傳多少次訊息：")
        input_post_number = input("你想要隔幾篇限時動態傳一次訊息：")
        input_send_message = input("你想要傳什麼訊息：")

        # check if user want to use default or not
        if len(input_post_number) == 0 and len(input_send_number) == 0 and len(input_send_message) == 0:
            print("use default settings!")
            input_send_number = 15
            input_post_number = 50
            input_send_message = "Liked! Please like my posts! Thanks!"

        add_friends_init()
        add_friends()
        time.sleep(2)
        click_first_video()
        flag = True
        post_counter = 0
        send_counter = 0
        while flag:
            like = None
            like = check_liked_or_not(like)
            if like == True:
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)
            else:
                click_like_button()
                time.sleep(0.5)
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)

            post_counter += 1
            if post_counter == int(input_post_number):
                send_some_words(input_send_message)
                send_counter += 1
                post_counter = 0

            if send_counter == int(input_send_number): # to avoid be banned
                break

    elif input_order == str(4):
        add_friends_init()
        add_friends()
        time.sleep(2)
        click_first_video()
        flag = True

        while flag:
            like = None
            like = check_liked_or_not(like)
            if like == True:
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)
            else:
                click_like_button()
                time.sleep(0.5)
                click_next_video()
                time.sleep(1)
                check_dead_or_not()
                flag = check_end_or_not(flag)

    elif input_order == str(5):
        main_flag = False
        print("Thank you! 888")
