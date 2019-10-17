import os 
from shutil import copyfile

#detect false vector 
path = "/home/lmtruong/Documents/data_cut/annot2_filter.txt"
pathout = "/home/lmtruong/Documents/data_cut/annot2_filter_final.txt"
count = 0
with open(path) as f:
	with open(pathout, "w" ) as s:
	    line = f.readline()

	    while line:
	    	line = line.strip()
	    	line += "\n"
	    	count+= 1
	    	if (count >=0 and count <=250)  :
	    		print(line)
	    		# break
	    	else:
	    		s.write(line)
	    	# if count >=0 and count <=300:
	    	# 	s.write(line)
	    	# else:
	    	# 	print(line)
	    	line = f.readline()	    	
	    	print(count)


#cut vector
# path = "/home/lmtruong/Desktop/Head_Detector_3/head_data_annot.txt"
# pathout = "/home/lmtruong/Desktop/Head_Detector_3/cut800_head_data_annot.txt"
# count = 0
# with open(path) as f:
# 	with open(pathout, "w" ) as s:
# 	    line = f.readline()

# 	    while line:
# 	    	line = line.strip()
# 	    	line += "\n"
# 	    	count+= 1
# 	    	if count >800:
# 	    		print(line)
# 	    		# break
# 	    	else:
# 	    		s.write(line)
# 	    	line = f.readline()	    	
# 	    	print(count)

	    	
	    		


