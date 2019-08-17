import os

count = 100

for img in range(1,count+1):
	#src_file = "Real/" + str(img) + "__" + "*.BMP"
	#print(src_file)
	#dest_file = "samplefile/"
	#command = "cp -v"+ " " + src_file + " " +dest_file
	#print(command)
	#os.system(command)

	src_file = "Altered/Altered-Easy/" + str(img) + "__" + "*.BMP"
	#print(src_file)
	dest_file = "samplefile/"
	command = "cp -v"+ " " + src_file + " " +dest_file
	os.system(command)
	
	 
