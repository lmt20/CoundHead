# from skimage.measure import structural_similarity as ssim
from skimage import measure
import numpy as np
import cv2 as cv
import os
from shutil import copyfile

# path_img_orig = "/home/lmtruong/Desktop/40.jpg"
# path_list_img = "/home/lmtruong/Desktop/Real_head"
# # path_img_orig = "/home/lmtruong/Desktop/Img_Head_Data/460.jpg"
# # path_list_img = "/home/lmtruong/Desktop/Img_Head_Data/1"
# listdir = os.listdir(path_list_img)
# img_orig = cv.imread(path_img_orig, 0)
# num = 0
# sum = 0
# count = 0
# avg = 1
# for filename in listdir:
# 	abs_path = os.path.join(path_list_img, filename)
# 	img = cv.imread(abs_path, 0)
# 	# s = ssim(img_orig, img)
# 	s = measure.compare_ssim(img_orig, img)
# 	# if s > 0.952562639878664:
# 	# 	cv.imshow("wd",img )
# 	# 	cv.waitKey(1)
# 	# 	os.remove(abs_path)
# 	# 	count+=1
# 	# 	print(count)

# 	sum += s
# 	num += 1
# 	print(s)

# avg = sum/num
# # print("AVG:", sum/num)

# for filename in listdir:
# 	abs_path = os.path.join(path_list_img, filename)
# 	img = cv.imread(abs_path, 0)
# 	s = measure.compare_ssim(img_orig, img)
# 	if s > avg + 0.01 :
# 		# cv.imshow("wd",img )
# 		# cv.waitKey(1)
# 		os.remove(abs_path)
# 		count+=1
# 		print(count)

#ssim dir folder img
# path_img = "/home/lmtruong/Videos/Count_Head_Video/img_delete"
# name_img = [os.path.join(path_img, i) for i in os.listdir(path_img)]
# path = "/home/lmtruong/Videos/Count_Head_Video/Img_dataset2"
# listdir= os.listdir(path)
# name_list_img = [os.path.join(path, i) for i in listdir]
# dir_background = "/home/lmtruong/Videos/background"

# for i in range(len(name_img)):

# 	path_img_orig = name_img[i]
# 	path_list_img = name_list_img[i]
# 	# path_img_orig = "/home/lmtruong/Desktop/Img_Head_Data/460.jpg"
# 	# path_list_img = "/home/lmtruong/Desktop/Img_Head_Data/1"
# 	listdir = os.listdir(path_list_img)
# 	img_orig = cv.imread(path_img_orig, 0)
# 	num = 0
# 	sum = 0
# 	count = 0
# 	avg = 1

# 	arr_img = []
# 	arr_point = []
# 	for filename in listdir:
# 		abs_path = os.path.join(path_list_img, filename)
# 		img = cv.imread(abs_path, 0)
# 		# s = ssim(img_orig, img)
# 		s = measure.compare_ssim(img_orig, img)

# 		arr_img.append(abs_path)
# 		arr_point.append(s)
# 		# if s > 0.952562639878664:
# 		# 	cv.imshow("wd",img )
# 		# 	cv.waitKey(1)
# 		# 	os.remove(abs_path)
# 		# 	count+=1
# 		# 	print(count)

# 		sum += s
# 		num += 1
# 		print(s)

# 	avg = sum/num
# 	# print("AVG:", sum/num)

# 	# for filename in listdir:
# 	# 	abs_path = os.path.join(path_list_img, filename)
# 	# 	img = cv.imread(abs_path, 0)
# 	# 	s = measure.compare_ssim(img_orig, img)
# 	# 	if s > avg + 0.01 :
# 	# 		cv.imshow("wd",img )
# 	# 		cv.waitKey(1)
# 	# 		# os.remove(abs_path)
# 	# 		count+=1
# 	# 		print(count)			
# 	for i in range(len(arr_img)):
# 		if arr_point[i] > avg + 0.01 :
# 			img  = cv.imread(arr_img[i])
# 			# cv.imshow("wd",img )
# 			# cv.waitKey(1)
# 			# copyfile(arr_img[i], os.path.join(dir_background, str(i)))
# 			os.remove(arr_img[i])
# 			count+=1
# 			print(count)	

#ssim folder img

dir_background = "/home/lmtruong/Videos/shop2_background"


path_img_orig = "/home/lmtruong/Videos/filter/shop2/shop_img21210.bmp"
path_list_img = "/home/lmtruong/Videos/shop_img2"
# path_img_orig = "/home/lmtruong/Desktop/Img_Head_Data/460.jpg"
# path_list_img = "/home/lmtruong/Desktop/Img_Head_Data/1"
listdir = os.listdir(path_list_img)
img_orig = cv.imread(path_img_orig, 0)

img_orig = img_orig[0:360,80:420]

num = 0
sum = 0
count = 0
avg = 1

arr_img = []
arr_point = []	
for filename in listdir:
	abs_path = os.path.join(path_list_img, filename)
	img = cv.imread(abs_path, 0)
	# s = ssim(img_orig, img)
	img = img[0:360,80:420]
	s = measure.compare_ssim(img_orig, img)

	arr_img.append(abs_path)
	arr_point.append(s)
	# if s > 0.952562639878664:
	# 	cv.imshow("wd",img )
	# 	cv.waitKey(1)
	# 	os.remove(abs_path)
	# 	count+=1
	# 	print(count)

	sum += s
	num += 1
	print(s)

avg = sum/num
# print("AVG:", sum/num)

# for filename in listdir:
# 	abs_path = os.path.join(path_list_img, filename)
# 	img = cv.imread(abs_path, 0)
# 	s = measure.compare_ssim(img_orig, img)
# 	if s > avg + 0.01 :
# 		cv.imshow("wd",img )
# 		cv.waitKey(1)
# 		# os.remove(abs_path)
# 		count+=1
# 		print(count)			
for i in range(len(arr_img)):
	if arr_point[i] > avg + 0.05 :
		img  = cv.imread(arr_img[i])
		# cv.imshow("wd",img )
		# cv.waitKey(500)
		copyfile(arr_img[i], os.path.join(dir_background, str(i)))
		os.remove(arr_img[i])
		count+=1
		print(count)	

