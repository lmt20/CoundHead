import os
import shutil
import random

in_path = "/home/lmtruong/Videos/Count_Head_Video/Img_dataset2_bf"
out_path = "/home/lmtruong/Videos/Count_Head_Video/Img_dataset2"

list_dir = os.listdir(in_path)
count = 0

for i in list_dir:
	path_dir = os.path.join(in_path,i)
	out_dir =os.path.join(out_path,i) 
	os.mkdir(out_dir)
	img_file = os.listdir(path_dir)
	num_copy = 0
	for filename in img_file:
		abs_img = os.path.join(path_dir, filename)
		out_img = os.path.join(out_dir, i+"_"+filename)
		shutil.copyfile(abs_img, out_img)
		num_copy += 1
		count += 1	
		print(count, num_copy)


# for file in list_dir:	
# 	path_file = os.path.join(in_path, file)
# 	# if random.random() < 0.2:
# 	# 	shutil.copyfile(path_file, os.path.join(out_path, file))
# 	# 	num_copy += 1
# 	shutil.copyfile(path_file, os.path.join(out_path,"_"+ file))
# 	num_copy += 1
# 	count += 1
# 	print(count, num_copy)

