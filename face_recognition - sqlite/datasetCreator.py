import numpy as np
import sqlite3
import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("FaceBase.db")
    c = conn.cursor()
    cmd="SELECT * FROM People Where ID="+str(Id)
    c.execute(cmd)
    isRecordExist=0
    '''for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+" WHERE ID="s(Id)
    else
    '''
    cmd2="INSERT INTO People(ID,Name) Values("+str(Id)+","+str(Name)+")"
    
    c.execute(cmd2)
    conn.commit()
    conn.close()


id=input('Enter user id : ')
name=input('Enter user Name : ')
insertOrUpdate(id,name)
sampleNum=0;
while(True):
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5); 
    for (x,y,w,h) in faces:
    	sampleNum=sampleNum+1;
    	cv2.imwrite("dataSet/User."+str(id)+'.'+str(sampleNum)+".jpg", gray[y:y+h,x:x+w])
    	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    	cv2.waitKey(200);
    	cv2.imshow('frame',img)
    	cv2.waitKey(1);
    if(sampleNum>30):
    	break
    
cap.release()
cv2.destroyAllWindows()