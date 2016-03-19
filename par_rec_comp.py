#!/usr/bin/python

#import sys
import os
import zipfile
from multiprocessing import Pool

op = os.path

# Python pseudocode
def rec_comp(file, new_root,pool, limit=5):
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

        pool.map(rec_comp, [(f,new_file,pool,limit) for f in sub_iter]) 
#        for f in sub_iter:
#           rec_comp(f,new_file,limit)

    else:
        os.system('robocopy "%s" "%s" "%s"' %(old_root, new_root, file_name))



if __name__ == '__main__':
    #rec_comp(str(sys.argv[1]), str(sys.argv[2]))
    source = r"C:\Users\Vincent\Documents\mess"
    destination = r"C:\Users\Vincent\Documents\new"
    pool = Pool()
    pool.map(rec_comp, (source,destination,pool,5))
    pool.close()
    pool.join()


# Other idea : n workers ; put the sub-folders in the queue 
# loop: take one file from the queue, treat it, put the sub-files in the queue
# no need for recursion anymore