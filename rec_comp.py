#!/usr/bin/python

#import sys
import os
import zipfile

op = os.path

# Python pseudocode
def rec_comp(file, new_root, limit=5):
    """Recursively copy a file tree, compresssing the files in the folder if it 
    has more than /limit/ non-folder files inside.
    """
    (old_root,file_name) = op.split(file)
    new_file = op.join(new_root,file_name)

    if op.isdir(file):
        os.mkdir(new_file)
        folder_content = [op.join(file,f) for f in os.listdir(file)]
        subfiles = [f for f in folder_content if not op.isdir(f)]
        subfolders = [f for f in folder_content if op.isdir(f)]    
        n = len(subfiles)
        if n > limit:
            archive_name = op.join(new_file, file_name) + ".zip"
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for f in subfiles:
                    zipf.write(f, op.split(f)[1]) #Name in archive is without directories
            sub_iter = subfolders
        else:
            sub_iter = folder_content            

        for f in sub_iter:
           rec_comp(f,new_file,limit)

    else:
        os.system('robocopy "%s" "%s" "%s"' %(old_root, new_root, file_name))



if __name__ == '__main__':
    #rec_comp(str(sys.argv[1]), str(sys.argv[2]))
    source = r"C:\Users\Vincent\Documents\mess"
    destination = r"C:\Users\Vincent\Documents\new"
    rec_comp(source,destination)

        #return 
#else:
#    return ""
####################################################################

### 
##!/usr/bin/env python
#import os
#import zipfile
#
#def zipdir(path, ziph):
#    # ziph is zipfile handle
#    for root, dirs, files in os.walk(path):
#        for file in files:
#            ziph.write(os.path.join(root, file))
#
#if __name__ == '__main__':
#    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
#    zipdir('tmp/', zipf)
#    zipf.close()

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
	
