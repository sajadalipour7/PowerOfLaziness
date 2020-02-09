"""
In the name of god


#################

PowerOfLaziness

################# 



Created By : Sajad Alipour

COPYRIGHT@2020
"""
import cv2
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
        if IsInTheBaze(x,210,260) and IsInTheBaze(y,40,65):
            up+=1
            down=0
            middle=0
            right=0
            left=0
            if(up>8):
                print("Up")
                up=0
        if IsInTheBaze(x,210,260) and IsInTheBaze(y,230,255):
            up=0
            down+=1
            middle=0
            right=0
            left=0
            if(down>8):
                print("Down")
                down=0
        if IsInTheBaze(x,210,260) and IsInTheBaze(y,115,135):
            #print("Middle")
        if x>350 and IsInTheBaze(y,115,135):
            print("Right")
        if x<80 and IsInTheBaze(y,115,135):
            print("Left")
        
        
        
        """
        if x<185:
            
            print("Left")
        elif x>360:
            print("Right")
        elif y<130:
            print("Up")
        """
        
    cv2.imshow('PythonChallenge',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()