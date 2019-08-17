import os

for line in open("conversion.txt"):
	src_file = line[:-1]
	#print(src_file)
	dest_file = src_file.replace(".BMP",".PGM")
	#print(dest_file)	
	#command1 = "convert " + src_file + " " + dest_file
	command2 = "rm -vf" + " " + src_file
	#os.system(command1)
	os.system(command2) 
