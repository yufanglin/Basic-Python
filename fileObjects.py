'''
File Objects
Code from following this tutorial:
https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25
'''

# f = open('intro.py', 'r') 	# just reading

# # print the name of the file 
# print(f.name)
# # print out the mode of the file open
# print(f.mode)

# # close file
# f.close()

###### Content Manager ########
with open('intro.py', 'r') as rf:
	# auto closes files for us after block
	
	#f_contents = f.read()
	#print(f_contents)
	#f_contents_array = f.readlines()
	#print(f_contents_array)
	# f_contents_firstLine = f.readline()
	# print(f_contents_firstLine)
	# f_contents_firstLine = f.readline()
	# print(f_contents_firstLine)

	# print out the first 100 characters
	# f_contents = f.read(100)

	# print out the next 100 characters
	# f_contents = f.read(100)

	# when we reach the end of the file, read just returns an empty string

	# for line in f:
	# 	print(line, end=' ')



	# size_to_read = 10
	# f_contents = f.read(size_to_read)
	# print(f_contents, end='')

	# f.seek(0)	# reset position to 0

	# f_contents = f.read(size_to_read)
	# print(f_contents)

	# print(f.tell())



	# while len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents = f.read(size_to_read)
	with open('intro_copy_from_fileObjects.py', 'w') as wf:
		# loop through each line in original file
		for line in rf:
			# write that line to the copy
			wf.write(line)



with open('websiteicon.png', 'rb') as rf:
	with open('websiteicon.png', 'wb') as wf:
		# # loop through each line in original file
		# for line in rf:
		# 	# write that line to the copy
		# 	wf.write(line)

		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)


########### Write ##########
# with open('test2.txt', 'w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('R')




