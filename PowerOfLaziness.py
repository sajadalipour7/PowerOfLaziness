"""
In the name of god


#################

PowerOfLaziness

################# 



Created By : Sajad Alipour

COPYRIGHT@2020
"""
import cv2
import time
import pyautogui
import os


def IsInTheBaze(x,a,b):
    if(x>a and x<b):
        return True
    else:
        return False

#Delay for Movements
up=0
down=0
right=0
left=0
middle=0
TimeIntegerSimulator=7


cap=cv2.VideoCapture(0)
cascPath='FACES.xml'
faceCascade=cv2.CascadeClassifier(cascPath)
while(True):
    _,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30)
            )
    
    
    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        if cv2.waitKey(1) & 0xFF==ord('d'):
            print('x= ',x,' y= ',y)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            quit()
        
        if IsInTheBaze(x,200,280) and IsInTheBaze(y,0,77):
            up+=1
            down=0
            middle=0
            right=0
            left=0
            if(up>5+TimeIntegerSimulator):
                print("Up")
                os.popen('explorer')
                time.sleep(1)
                up=0
        if IsInTheBaze(x,100,380) and IsInTheBaze(y,250,300):
            up=0
            down+=1
            middle=0
            right=0
            left=0
            if(down>TimeIntegerSimulator):
                print("Down")
                pyautogui.hotkey('alt', 'f4')
                time.sleep(3)
                down=0
        if IsInTheBaze(x,150,280) and IsInTheBaze(y,115,155):
            up=0
            """
            up=0
            down=0
            middle+=1
            right=0
            left=0
            if(middle>TimeIntegerSimulator):
                print("Middle")
                middle=0
            """

        if x>340 and IsInTheBaze(y,25,265):
            up=0
            down=0
            middle=0
            right+=1
            left=0
            if(right>TimeIntegerSimulator):
                print("Right")
                #in here you should put your favarite Key of Keyboard
                #for example it's default is Enter
                #you can change it to anything like 'a' 'b' 'ctrl' 'shift' and etc.
                pyautogui.press("\n")
                #Here is a list for available keys of keyboard
                """
                ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                'command', 'option', 'optionleft', 'optionright']
                """
                right=0
        if x<110 and IsInTheBaze(y,25,265):
            up=0
            down=0
            middle=0
            right=0
            left+=1
            if(left>TimeIntegerSimulator):
                print("Left")
                #in here you should put your executable application file address
                os.popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                
                time.sleep(2)
                left=0
        
    cv2.imshow('PowerOfLaziness',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()