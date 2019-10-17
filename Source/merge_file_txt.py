import numpy as np 
import os 
import shutil 

# copy file into one folder
# path = "/home/lmtruong/Documents/datasheet"
# out_dir = os.path.join("/home/lmtruong/Documents", "ANNOT_TH")
# os.mkdir(out_dir)
# listdir = os.listdir(path)
# count = 0
# for dir_ in listdir:
# 	dir_name = os.path.join(path, dir_)
# 	print(dir_name)
# 	listfile = os.listdir(dir_name)
# 	file_name = listfile[0]
# 	abs_file = os.path.join(dir_name, file_name)
# 	abs_out = os.path.join(out_dir, file_name)
# 	print(abs_file)
# 	print(abs_out)
# 	shutil.copyfile(abs_file, abs_out)
# 	count+=1
# 	print(count)

#convert path in file annot.txt
path = "/home/lmtruong/Desktop/Head_Official/Orig_data"
path_out = "/home/lmtruong/Desktop/Head_Official/data_TH1_400"
if not os.path.isdir(path_out):
	os.mkdir(path_out)
count = 0
for filename in os.listdir(path):
	abs_file = os.path.join(path, filename)
	abs_out = os.path.join(path_out, filename)
	count_line = 0
	with open(abs_file) as f:
		with open(abs_out, "a") as a:
			line = f.readline()
			while line:
				line = line.strip()
				# line = line.replace("rawdata", "/home/lmtruong/Videos/Count_Head_Video/merge_img_dataset2")
				line += "\n"
				a.write(line)
				count_line += 1
				if count_line >= 400:
					break
				line = f.readline()
	count += 1
	print(count)



# merge file into one file .txt
# path = "/home/lmtruong/Desktop/Head_Official/Orig_data"
# path_out = os.path.join("/home/lmtruong/Desktop/Head_Official/data_TH1_400", "annot_merge_filter.txt")
# count = 0
# for filename in os.listdir(path):
# 	count_line = 0
# 	abs_file = os.path.join(path, filename)
# 	print(filename)
# 	with open(path_out, "a") as f:
# 		with open(abs_file) as h:
# 			line = h.readline()
# 			while line:
# 				line = line.strip()
# 				line += "\n"
# 				f.write(line)
# 				count_line += 1
# 				print(filename , count_line)
# 				if count_line >= 400:
# 					break
# 				line = h.readline()
# 	count+=1
# 	print(count)

