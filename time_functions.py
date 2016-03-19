# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:02:16 2016

@author: Vincent
"""

import timeit
import queue_comp
import os
from multiprocessing import Process, Queue

if __name__ == '__main__':
    #rec_comp(str(sys.argv[1]), str(sys.argv[2]))

    source = r"C:\Users\Vincent\Documents\projects\3rdpartypublic"

    t0 = timeit.default_timer()
    destination = r"C:\Users\Vincent\Documents\new"
    os.system('robocopy "%s" "%s" /E > nul' %(source, destination))

    t1 = timeit.default_timer()
    print('robocopy takes %f' %(t1-t0))
    destination = r"C:\Users\Vincent\Documents\new1"
    max_proc = 1
    q = Queue()
    q.put((source, destination))
    p = [Process(target=queue_comp, args=(q,num,5)) for num in range(max_proc)]
    for num in range(max_proc):
        p[num].start()
    for num in range(max_proc):
        p[num].join()

    t2 = timeit.default_timer()
    destination = r"C:\Users\Vincent\Documents\new2"
    max_proc = 4
    q = Queue()
    q.put((source, destination))
    p = [Process(target=queue_comp, args=(q,num,5)) for num in range(max_proc)]
    for num in range(max_proc):
        p[num].start()
    for num in range(max_proc):
        p[num].join()

    t3 = timeit.default_timer()
    destination = r"C:\Users\Vincent\Documents\new3"
    max_proc = 8
    q = Queue()
    q.put((source, destination))
    p = [Process(target=queue_comp, args=(q,num,5)) for num in range(max_proc)]
    for num in range(max_proc):
        p[num].start()
    for num in range(max_proc):
        p[num].join()

    t4 = timeit.default_timer()               
    print('1-cores takes %f' %(t2-t1))
    print('4-cores takes %f' %(t3-t2))
    print('8-cores takes %f' %(t4-t3))
