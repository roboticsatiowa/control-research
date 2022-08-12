import pyautogui

def main():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'Desktop \ filename.png')
    print('test')