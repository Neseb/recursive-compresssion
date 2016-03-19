#!/usr/bin/python

#import sys
import os
import zipfile
from queue import Empty

op = os.path

def queue_comp(q,num,limit=5):
    """Copy a file tree, compresssing the files in the folders if they 
    have more than /limit/ non-folder files inside.
    Multi-processing version, folders to be copied are passed on the
    queue q.
    """
    while True:
        try:
            if q.empty():
                print("je te l'avais bien dit")                
            (file, new_root) = q.get(True,5)
            (old_root,file_name) = op.split(file)
            new_file = op.join(new_root,file_name)        
            if op.isdir(file):
                os.mkdir(new_file)
                folder_content = [op.join(file,f) for f in os.listdir(file)]
                subfiles = [f for f in folder_content if not op.isdir(f)]
                subfolders = [f for f in folder_content if op.isdir(f)]    
                n = len(subfiles)
                if n > limit:
                    sub_iter = subfolders
                else:
                    sub_iter = folder_content            
                for f in sub_iter:
                    q.put((f,new_file)) 

                # We make two /if/ to put folders in the queue as soon as possible
                if n > limit:
                    archive_name = op.join(new_file, file_name) + ".zip"
                    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                        for f in subfiles:
                            zipf.write(f, op.split(f)[1]) #Name in archive is without directories
            else:
                os.system('robocopy "%s" "%s" "%s" > nul' %(old_root, new_root, file_name))
                    # shut up robocopy you're drunk go home
        except Empty:
            break
            
#    queue_comp(queue,5)
#    p = Process(target=rec_comp, args=(q,5))
#    p.start()
#    p.join()

# Other idea : n workers ; put the sub-folders in the queue 
# loop: take one file from the queue, treat it, put the sub-files in the queue
# no need for recursion anymore

#    while not queue.empty():
# Since we push the subfolders if there are some, the queue being 
# empty means this branch of the tree does not have any 

# While there are directories to be explored, there will always be at least one 
# worker awake
# variable all_asleep :
# while not all_asleep