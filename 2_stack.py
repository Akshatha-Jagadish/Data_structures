# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:31:32 2022

@author: Akshatha
"""

class Stack():
    def __init__(self):
        self.arr = []
    
    def push(self, value):
        self.arr.append(value)
    
    def pop(self):
        val = self.arr[-1]
        self.arr = self.arr[:-1]
        return val
    
    def length(self):
        return len(self.arr)
    
    def disp(self):
        print(self.arr)
    
if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(5)
    my_stack.disp()
    my_stack.push(10)
    my_stack.disp()
    my_stack.push('game')
    my_stack.disp()
    print('stack length: ',my_stack.length())
    print('popped element: ',my_stack.pop())
    my_stack.disp()
    print('stack length: ',my_stack.length())