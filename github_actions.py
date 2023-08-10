import subprocess

import pyperclip
import time

import os
import pyautogui
import firebase

import shogigui

import datetime
import pywinctl as gw

import kifu_loader


if os.path.exists("local.py"):
    local = True
    debug = False
else:
    local = False
    debug = False


def upload_screenshot(directory,filename="image"):

    time.sleep(1)
    filename = filename+".png"
    screen_shot = pyautogui.screenshot() 
    path = directory+"/"+filename
    screen_shot.save(path)
    if not debug:
        firebase.upload_image(path)
        #print("upload image")


subprocess.Popen("ShogiGUI\ShogiGUI.exe")



time.sleep(15)

#print(gw.getAllTitles())



shogigui.activate()

if not local:    
    shogigui.set_engine(local)
    time.sleep(5)
    shogigui.separate_window()
    time.sleep(2)

shogigui.kentou()

usernames = os.environ.get("USERNAMES").split(",")

print(usernames)

kifus = []
for username in usernames:
    a = kifu_loader.SyogiQuestBeta()
    a.set_username(username)
    for minute in [2,5,10]:
        ids = a.get_game_ids(minutes=minute,game_count=10)
        get_kifus = a.get_kifus(ids)
        print(username,minute,len(get_kifus))
        kifus.extend(get_kifus)

# 既にアップロードされている棋譜を除外
kifus = [kifu for kifu in kifus if not firebase.exsits_kifu(kifu)]


print("kifu_num",len(kifus))


for kifu in kifus:

    pyperclip.copy(kifu.text)
    shogigui.paste_kifu()

    

    #盤面画像のアップロード
    directory = kifu.id
    print("directory",directory)
    os.makedirs(directory,exist_ok=True)
    for i in range(kifu.move_count):
        pyautogui.press("1")
        time.sleep(5)
        upload_screenshot(directory,str(i+1))
    
    #棋譜情報のアップロード
    firebase.upload_kifu(kifu)



# time.sleep(10)


# upload_screenshot()

