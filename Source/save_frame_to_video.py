import cv2 as cv
import os 
import shutil


pathOut = "/home/lmtruong/Desktop/test_cap1.avi"
# frame_width = int( vs.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height =int( vs.get( cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = 960
frame_height = 540
size = (frame_width, frame_height)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(pathOut, fourcc, 8.0, size)

path = "/home/lmtruong/Documents/data_cut/annot2.txt"

with open(path) as f:
	line = f.readline()
	while line:
		line = line.strip()
		list = line.split(" ")
		path_img = list[0]
		img = cv.imread(path_img)
		print(img.size)
		for i in range(int(list[1])):
			img = cv.rectangle(img,(int(list[2+4*i]), int(list[3+4*i])) , (int(list[2+4*i])+int(list[4+4*i]), int(list[3+4*i])+int(list[5+4*i])), (255,0,0))
		cv.imshow("wd", img)
		cv.waitKey(10)
		out.write(img)
		line = f.readline()
	out.release()
	print("DOne")
