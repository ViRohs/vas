import pyautogui
import pywinctl as gw
import os 

import time

def activate():
    print("activate")
    window_title = "ShogiGUI"
    retry_count = 0
    while retry_count < 10:
        try:
            window = gw.getWindowsWithTitle(window_title)[0]
            window.activate()
            window.maximize()
            
            # window.resize(0,50)
            # window.move(0,-50)
            break
        except IndexError:
            print("retry")
            retry_count += 1
            time.sleep(5)

def save_graph():

    pyautogui.press('alt')
    pyautogui.press('f')
    pyautogui.press('g')
    #pyautogui.write(active_window_title)
    pyautogui.press('enter')


def paste_kifu():
    pyautogui.press('alt')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('alt')

def kentou():
    
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('c')
    time.sleep(1)
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')

    pyautogui.press('down',4)
    time.sleep(1)
    pyautogui.press('tab',3)

    pyautogui.press('enter')

# ウィンドウサイズが(1024,768)の場合
def separate_window():
    pyautogui.moveTo(85, 575)
    pyautogui.dragTo(85, 470, 2, button='left')

def kaiseki():
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('a')
    #pyautogui.press('enter')

    # while True:
    #     windows = gw.getWindowsWithTitle("解析結果")
    #     if len(windows) > 0:
    #         time.sleep(1)
    #         pyautogui.press('enter')
    #         print("解析終了")
    #         break

def set_engine(local):
    path = os.getcwd()

    pyautogui.press('alt')
    pyautogui.press('t')
    pyautogui.press('e')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    if not local:
        full_path = path+"\ShogiGUI\Suisho5-YaneuraOu-v7.5.0-windows\YaneuraOu_NNUE-tournament-clang++-avx2.exe"
    else:
        full_path = "YaneuraOu_NNUE-tournament-clang++-avx2.exe"
    print(full_path)
    pyautogui.write(full_path)

    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('shift', 'tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')

