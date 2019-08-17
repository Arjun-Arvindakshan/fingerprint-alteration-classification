import os

for line in open("List.txt"): 
	src_file = line[:-1]
	#print(line)
	dst_file = line.replace(".BMP","_REAL_.BMP")
	#print(new_line)
	command = "mv -v " + src_file + " " + dst_file
	#print(command)
	os.system(command)
