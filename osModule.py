'''
Python Tutorial
code from following:
https://www.youtube.com/watch?v=tJxcKyFMTGo&index=23&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU
'''
import os
from datetime import datetime

#print(dir(os))

# get current working directory
print(os.getcwd())

# change current working directory
os.chdir('/Users/lin15556/Desktop/')
print(os.getcwd())

# print the files and folders in desktop
print(os.listdir())

# # make directory on current working directory
# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1') # allows deeper level creation
# print(os.listdir())

# # remove directorys
# os.rmdir('OS-Demo-2')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# print(os.listdir())

# rename file
# os.rename('test.txt', 'demo.txt')
# print out status of file
# print(os.listdir())

# get the time
# mode_time = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# traverse the directories
for dirpath, dirnames, filenames in os.walk('/Users/lin15556/Desktop/'):
	print('Current Path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)
	print()

print(os.environ.get('HOME'))

fire_path = os.path.join(os.environ.get('HOME'),'test.txt')
print(fire_path)

# get the name of the file we are trying to use (doesn't have to be real)
print(os.path.basename('/tmp/test.txt'))

# check if is file or directory
print(os.path.isfile('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))

# split file name with extension
print(os.path.splitext('/tmp/test.txt'))

# list of what is in os.path
print(dir(os.path))