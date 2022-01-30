# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:40:18 2022

@author: Akshatha
"""

class Queue():
    def __init__(self):
        self.arr = []
    
    def enqueue(self, value):
        self.arr.append(value)
    
    def dequeue(self):
        if self.length() == 0:
            print('Queue is empty')
            return None
        val = self.arr[0]
        self.arr = self.arr[1:]
        return val
    
    def length(self):
        return len(self.arr)
    
    def disp(self):
        print(self.arr)
    
if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue(5)
    my_queue.enqueue(10)
    my_queue.disp()
    print('dequeued element: ',my_queue.dequeue())
    my_queue.enqueue('ball')
    my_queue.enqueue('bat')
    my_queue.disp()
    print('queue length: ',my_queue.length())