import cv2 as cv 
import os
import numpy as np 


path = "/home/lmtruong/Desktop/raw"
pathout = "/home/lmtruong/Desktop/raw1"
listdir = os.listdir(path)
count = 0 
for filename in listdir:
	img = cv.imread(os.path.join(path, filename))
	width = int(img.shape[1]*0.5)
	height = int(img.shape[0]*0.5)
	img = cv.resize(img, (width, height))
	cv.imwrite(os.path.join(pathout, filename), img)
	count += 1
	print(count)
