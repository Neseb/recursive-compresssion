# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 18:25:42 2016

@author: Vincent
"""

from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()