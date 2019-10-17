import numpy as np 
import os 
import cv2 as cv 


# /home/lmtruong/Videos/Count_Head_Video/merge_img_dataset2/g001_color.avi_100.bmp 1 146 186 124 111
path = "/home/lmtruong/Desktop/Head_Official1/head_data2_multi.txt"

with open(path) as f:
	line = f.readline()
	while line:
		line = line.strip()
		list = line.split(" ")
		path_img = list[0]
		img = cv.imread(path_img)
		for i in range(int(list[1])):
			img = cv.rectangle(img,(int(list[2+4*i]), int(list[3+4*i])) , (int(list[2+4*i])+int(list[4+4*i]), int(list[3+4*i])+int(list[5+4*i])), (255,0,0))
		cv.imshow("wd", img)
		cv.waitKey(500)
		line = f.readline()

