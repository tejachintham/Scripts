import pyautogui
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True
for i in range(3600):
    if((i%3)==0):
        pyautogui.moveTo(1364, 200, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(64, 200, duration=0.1)
        pyautogui.moveTo(1364, 700, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(300, 100, duration=0.1)
        pyautogui.click(847, 5)
        pyautogui.click(1364,500)
        pyautogui.click(1364,500)
        pyautogui.scroll(100)
        pyautogui.scroll(-100)
    if((i%3)!=0):
        pyautogui.moveTo(1364, 200, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(64, 200, duration=0.1)
        pyautogui.moveTo(1364, 700, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(300, 100, duration=0.1)
        pyautogui.click(109, 10)
        pyautogui.click(1364,500)
        pyautogui.click(1364,500)
        pyautogui.scroll(100)
        pyautogui.scroll(-100)
    if((i%2)==0):
        pyautogui.moveTo(1364, 200, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(64, 200, duration=0.1)
        pyautogui.moveTo(1364, 700, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(300, 100, duration=0.1)
        pyautogui.click(334, 2)
        pyautogui.click(1364,500)
        pyautogui.click(1364,500)
        pyautogui.scroll(100)
        pyautogui.scroll(-100)
    if((i%2)!=0):
        pyautogui.moveTo(1364, 200, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(64, 200, duration=0.1)
        pyautogui.moveTo(1364, 700, duration=0.1)
        pyautogui.click()
        pyautogui.moveTo(300, 100, duration=0.1)
        pyautogui.click(473, 5)
        pyautogui.click(1364,500)
        pyautogui.scroll(100)
        pyautogui.scroll(-100)
        
     
