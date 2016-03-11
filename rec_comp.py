#!/usr/bin/python
import os
import shutil

# Python pseudocode
def rec_comp(file,old_root,new_root):
	"Recursively copy a file tree, compresssing the folder if it has more than 10 files inside"
	file_name = os.trim(file,old_root)
	new_file = os.path.join(new_root,file_name)
	if os.path.isdir(file):
		os.mkdir(new_file)
		files = os.listdir(file)
		n = len(files)
		if n > 10:
			archive_name = os.path.join(new_file ,file_name)
			shutil.make_archive(archive_name, 'zip', ("\\" + file_name + ".zip"))
			# return 
		else:
			for f in files:
				rec_comp(f,file,new_file)
                         # return 
	else:
		os.system('robocopy "%s" "%s"' % (file, new_file))
            		#return 
####################################################################

# Random pseudocode
# file_name = trim(file,old_root)
# new_file = [new_root file_name]
# if file is directory
	# mkdir(new_file)
	# files = dir(file)
	# n = length(files)
	# if n > 5
		# compress files [new file '.zip']
	# else
		# for f in files
			# rec_comp f
# else
	# cp file new_file

# ML-like pseducode	
# let rec fun rec_comp file old_root new_root =	
	# file_name = trim(file,old_root)
	# new_file = [new_root file_name]
	# if  (is_directory file)
		# mkdir(new_file)
		# files = dir file
		# n = length files
		# if n > 5
			# compress file [new_file "\\" file_name ".zip"]
		# else
			# for f in files
				# rec_comp f old_root new_root
	# else
	# cp file new_file
	