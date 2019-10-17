import numpy as np
import os 

filename = "/home/lmtruong/Desktop/Work_Space/shop_data/shop_img1_filter.txt"
collection_ = set()
count = 0
with open(filename) as f:
    line = f.readline()
    while line:
    	count += 1
    	line = f.readline()
    	collection_.add(line)
    	# print(count, line)
print(len(collection_))

# path = "/home/lmtruong/Documents/ANNOT_TH"
# listfile = os.listdir(path)
# numline  = 0
# for id, filename in enumerate(listfile):
#     abs_file = os.path.join(path, filename)
#     with open(abs_file) as f:
#     	content = f.readlines()
#     	print(id+1, len(content))
#     	if id == 15:
#     		print(content)
#     	numline+= len(content)
# print(numline)
   

    
   

