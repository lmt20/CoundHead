import os
# /home/lmtruong/Videos/Count_Head_Video/merge_img_dataset2/g002_color.avi_470.bmp 1 87 165 115 134
#check multiple file .txt
# path = "/home/lmtruong/Documents/ANNOT_TH"
# path_out = os.path.join("/home/lmtruong/Documents", "ANNOT_CONVERT_FILTER")
# if not os.path.isdir(path_out):
# 	os.mkdir(path_out)
# count = 0
# for filename in os.listdir(path):
# 	abs_file = os.path.join(path, filename)
# 	abs_out = os.path.join(path_out, filename)
# 	with open(abs_file) as f:
# 		with open(abs_out, "a") as a:
# 			line = f.readline()
# 			while line:
# 				line = line.strip()

# 				string = line.split(" ")
# 				length = len(string)
# 				check = 1
# 				x = 2
# 				y = 3

# 				while x<length:
# 					if int(string[x]) < 0 or int(string[x])+int(string[x+2]) > 960:
# 						check = 0
# 						break
# 					if int(string[y]) < 0 or int(string[y])+int(string[y+2]) > 540:
# 						check = 9
# 						break
# 					x += 4
# 				if check == 1:
# 					line = line.replace("rawdata", "/home/lmtruong/Videos/Count_Head_Video/merge_img_dataset2")
# 					line += "\n"
# 					a.write(line)
# 				line = f.readline()
# 	count += 1
# 	print(count)



#filter 1 file .txt
abs_file = "/home/lmtruong/Documents/data_cut/annot2.txt"
abs_out = "/home/lmtruong/Documents/data_cut/annot2_filter.txt"
with open(abs_file) as f:
	with open(abs_out, "a") as a:
		line = f.readline()
		count_line = 0
		count_write = 0
		while line:
			line = line.strip()

			string = line.split(" ")
			length = len(string)
			check = 1
			x = 2
			y = 3
			try:
				while x<length:
					if int(string[x]) <= 0 or int(string[x])+int(string[x+2]) >= 960:
						check = 0
						break
					if int(string[y]) <= 0 or int(string[y])+int(string[y+2]) >= 540:
						check = 9
						break
					x += 4
					y+=4
				if check == 1:
					# line = line.replace("rawdata", "/home/lmtruong/Videos/Count_Head_Video/merge_img_dataset2")
					line += "\n"
					a.write(line)
					count_write+=1
			except:
				print(line)
			count_line+=1
			line = f.readline()
		print(count_line)
		print(count_write)
			
