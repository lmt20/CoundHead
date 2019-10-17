import numpy as np 
import cv2 as cv
import shutil 
import os
import argparse

# ap = argparse.ArgumentParser()
# ap.add_argument("-v","--video")
# ap.add_argument("-o","--dirout")
# args = vars(ap.parse_args())

# path_video = args["video"]
# path_out = args["dirout"]
path = "/home/lmtruong/Videos/shop3_CUT4.mp4"
path_out = "/home/lmtruong/Videos/shop_img3"
if not os.path.isdir(path_out):
	os.mkdir(path_out)
cap = cv.VideoCapture(path)
count = 0
num_img = 0
while True:
	ret, frame = cap.read()
	if ret == False:
		break
	if count % 10 == 0:
		pathout = os.path.join(path_out,"shop_img3_cut4" + str(count)+".bmp")
		frame = cv.resize(frame, (640, 360))
		cv.imwrite(pathout, frame)
		num_img += 1
	count += 1
	print(count)
print(num_img)



#cut dir videos --> dir folder images
# path_dirvideo = "/home/lmtruong/Videos/Count_Head_Video/Dataset_2"
# path_out = "/home/lmtruong/Videos/Count_Head_Video/Img_dataset2"
# listdir = os.listdir(path_dirvideo)
# for video in listdir:
# 	os.mkdir(os.path.join(path_out,video))
# 	path_video = os.path.join(path_dirvideo, video)

# 	cap = cv.VideoCapture(path_video)

# 	count = 0
# 	while True:
# 		ret , frame = cap.read()
# 		if ret == False:
# 			break
# 		if count % 5 == 0:
# 			pathout = os.path.join(path_out,video,str(count)+".bmp")
# 			cv.imwrite(pathout, frame)
# 		count += 1 
# 		print(count)

#use: python /home/lmtruong/Desktop/Work_space/deep-learning-opencv/cutframe.py -v /home/lmtruong/Desktop/Count_Head_Data/g001_color.avi -o /home/lmtruong/Desktop/Img_Head_Data/1


# index_video = ['g010','g011','g012','g013','g014','g015','g016','g017','g018','g019','g020','g021','g022','g023']
# name_video = [i + "_color.avi" for i in index_video]
# name_dir = [10,11, 12,13,14,15,16,17,18,19,20,21,22,23]

# for i in range(len(index_video)):

# 	path_out = "/home/lmtruong/Desktop/Img_Head_Data"+"/"+str(name_dir[i]) 
# 	path_video = "/home/lmtruong/Desktop/Count_Head_Data"+"/"+name_video[i]

# 	print(path_out)
# 	print(path_video)
# 	cap = cv.VideoCapture(path_video)

# 	count = 0
# 	while True:
# 		ret , frame = cap.read()
# 		if ret == False:
# 			break
# 		if count % 5 == 0:
# 			pathout = os.path.join(path_out,str(count)+".jpg")
# 			cv.imwrite(pathout, frame)
# 		count += 1 
# 		print(count)
