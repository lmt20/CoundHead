import os
import shutil
import random

in_path = "/home/lmtruong/Videos/Split_Data/save_img5"
out_path = "/home/lmtruong/Videos/Split_Data/save_5"
num = 0
for filename in  os.listdir(in_path):
	abs_file = os.path.join(in_path, filename)
	out_file = os.path.join(out_path, "save_5"+filename)
	shutil.copyfile(abs_file, out_file)
	num+= 1
	print(num)

	if num > 2000:
		break

