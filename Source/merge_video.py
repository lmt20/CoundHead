import numpy 
import os 
from shutil import copyfile


path = "/home/lmtruong/Videos/Count_Head_Video/Img_dataset2"
path_out = os.path.join("/home/lmtruong/Videos/Count_Head_Video", "merge_img_dataset2")
if not os.path.isdir(path_out):
	os.mkdir(path_out)

numfolder = 0
for dirname in os.listdir(path):
	abs_dir = os.path.join(path, dirname)
	numfolder += 1
	numfile = 0
	for filename in os.listdir(abs_dir):
		abs_file = os.path.join(abs_dir, filename)
		out_file = os.path.join(path_out, filename)
		copyfile(abs_file, out_file)
		numfile += 1
		print(numfolder, numfile)
