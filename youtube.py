import pyautogui
import time
import keyboard
pozitie_initiala_x = 276
pozitie_initiala_y = 596

def cautare_google():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\googlesearch.png', confidence=0.7) !=None:
        camp_google=pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\googlesearch.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('http://youtube.com')
        pyautogui.press('enter')
        
    else:
        print("Imaginea nu este pe ecran")


def cautare_youtube():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\cautareyt.png', confidence=0.7) !=None:
        camp_google=pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\cautareyt.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
        pyautogui.write('python')
        pyautogui.press('enter')
        time.sleep(3)
        camp_google=pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\chanel.png', confidence=0.7)   
        pyautogui.click(camp_google)     
    else:
        print("Imaginea nu este pe ecran")

def cautare_subscribe():
    time.sleep(5)
    if pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\subscribe.png', confidence=0.7) !=None:
        camp_google=pyautogui.locateOnScreen(r'C:\Users\Student\Desktop\lab\subscribe.png', confidence=0.7)
        pyautogui.click(camp_google)
        time.sleep(1)
    else:
        print("Imaginea nu este pe ecran")


def coordonate():
    print(pyautogui.position())

def click_video():
    time.sleep(3)
    pyautogui.locateOnScreen(pozitie_initiala_x, pozitie_initiala_y)
    pyautogui.click()

col = 1
time.sleep(1)
while not keyboard.is_pressed('esc'):
    diferenta_y = 0
    #coordonate()
    while(col < 3):
        if col == 1:
            coordonate()
            pyautogui.locateOnScreen(pozitie_initiala_x, pozitie_initiala_y)
            pyautogui.click()
            col = 2
        elif col == 2:
            coordonate()
            pyautogui.locateOnScreen(pozitie_initiala_x, pozitie_initiala_y + diferenta_y)
            pyautogui.click()
            col = 3

click_video()

cautare_google()
cautare_youtube()
cautare_subscribe()