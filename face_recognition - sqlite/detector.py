import numpy as np
from PIL import Image
import cv2,os
import pickle
import sqlite3

#detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer\\trainningData.yml")
#path=rec.read("haarcascade_frontalface_default.xml")
facecachecade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

id=0

def getprofile(id):
    conn=sqlite3.connect("FaceBase.db")
    c = conn.cursor()
    cmd="SELECT Name FROM People WHERE ID = '" + str(id) + "'"
    #cmd="SELECT Name FROM People WHERE ID="+str(id)
    c.execute(cmd)
    profile=None
    for row in c:
        profile=row[0]
    conn.close()
    return profile

font=cv2.FONT_HERSHEY_COMPLEX #InitFont(cv2.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while(True):
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecachecade.detectMultiScale(gray, 1.3, 5)# flags=cv2.CASCADE_SCALE_IMAGE)
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        name=getprofile(id)
        cv2.putText(img,name,(x,y+h),font,1,255);
    cv2.imshow("face",img);
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 

