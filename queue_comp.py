#!/usr/bin/python

#import sys
import os
import zipfile
from multiprocessing import Queue#,Process

op = os.path

# Python pseudocode
def queue_comp(queue,lock,limit=5):
    """Recursively copy a file tree, compresssing the files in the folder if it 
    has more than /limit/ non-folder files inside.
    """
    while not queue.empty():
    # Since we push the subfolders if there are some, the queue being 
    # empty means this branch of the tree does not have any 
        lock.acquire
        (file, new_root) = queue.get()
#        print(file, new_root)
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
                queue.put((f,new_file)) 
            # sig.put(wake_up)

        else:
            os.system('robocopy "%s" "%s" "%s"' %(old_root, new_root, file_name))
        lock.release
        
if __name__ == '__main__':
    #rec_comp(str(sys.argv[1]), str(sys.argv[2]))
    source = r"C:\Users\Vincent\Documents\projects"
    destination = r"C:\Users\Vincent\Documents\new"

#    rec_comp(source,destination,pool,5)
    lock = Lock()

    queue = Queue()
    queue.put((source, destination))
    
    for num in range(8):
        Process(target=queue_comp, args=(queue,lock,5)).start()
#    queue_comp(queue,5)
#    p = Process(target=rec_comp, args=(q,5))
#    p.start()
#    p.join()


# Other idea : n workers ; put the sub-folders in the queue 
# loop: take one file from the queue, treat it, put the sub-files in the queue
# no need for recursion anymore

# While there is directories to be explored, there will always be at least one 
# worker awake
# variable all_asleep :

# while not all_asleep