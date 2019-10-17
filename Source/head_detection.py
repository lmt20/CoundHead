import numpy as np 
import cv2 as cv
import os

# path_xml = "/home/lmtruong/Documents/HaarTraining/opencv_workspace1/data/cascade.xml"
path_xml = "/home/lmtruong/Desktop/Work_Space/shop_data2/data/cascade.xml"
head_cascade = cv.CascadeClassifier()
head_cascade.load(path_xml)
# cap = cv.VideoCapture("/home/lmtruong/Desktop/Count_Head_Data/g022_color.avi")
cap = cv.VideoCapture("/home/lmtruong/Videos/shop1_CUT.mp4")
# cap = cv.VideoCapture("/home/lmtruong/Videos/Count_Head_Video/Dataset_1/30min_day3_cam1_20fps_960x540.MP4")


num_save = 0
def detectAndDisplay(frame, num_save):

	
    # width = int(frame.shape[1]*0.5)
    # height = int(frame.shape[0]*0.5)
    frame = cv.resize(frame, (640, 360))
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # print(frame.shape)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    heads = head_cascade.detectMultiScale(frame_gray,scaleFactor = 1.2, minNeighbors=5	,minSize=(50,50),maxSize=(100,100))
    # heads = head_cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in heads:
        center = (x + w//2, y + h//2)
        startX, startY, endX, endY = x, y, x+w, y+h
        # img_save = frame[startX:endX, startY: endY]
        img_save = frame[startY:endY, startX: endX]

        pathout = "/home/lmtruong/Videos/save_img1"
        num_save+=1
        cv.imwrite(os.path.join(pathout, str(num_save)+".jpg"), img_save)
        cv.rectangle(frame, (startX, startY), (endX, endY),	(0, 0, 255), 2)
        
        
        
        # faceROI = frame_gray[y:y+h,x:x+w]
        # #-- In each face, detect eyes
        # eyes = eyes_cascade.detectMultiScale(faceROI)
        # for (x2,y2,w2,h2) in eyes:
        #     eye_center = (x + x2 + w2//2, y + y2 + h2//2)
        #     radius = int(round((w2 + h2)*0.25))
        #     frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
    return num_save

while True:
	_, frame = cap.read()
	num_save = detectAndDisplay(frame, num_save)
	if cv.waitKey(10) == 27:
		break