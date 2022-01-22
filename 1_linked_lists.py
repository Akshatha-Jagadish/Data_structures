# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 11:11:09 2022

@author: Akshatha
"""
class Node():
    def __init__(self,value,next_node=None):
        self.value = value
        self.next = next_node
        
class Linked_list():
    def __init__(self):
        self.start_node = None
    
    def insert_element_at_beginning(self, value):
        if self.start_node == None:
            self.start_node = Node(value)    
        else:
            self.start_node = Node(value,self.start_node)
    
    def length(self):
        curr_node = self.start_node
        count = 0
        while (curr_node != None):
            curr_node = curr_node.next
            count+=1
        return count
    
    def change_element_at_loc(self, value, loc):
        if loc >= self.length():
            print('Location/ index does not exist')
            return False
        
        curr_node = self.start_node
        index = 0
        while (curr_node != None):
            if index==loc:
                curr_node.value = value
                return True
            curr_node = curr_node.next
            index+=1
            
    def insert_element_at_loc(self, value, loc):
        if loc >= self.length():
            print('Location/ index does not exist')
            return False
        
        if loc == 0:
            self.insert_element_at_beginning(value)
            return True
        
        prev_node = self.start_node
        index = 1
        while (prev_node.next != None):
            if index==loc:
                prev_node.next = Node(value,prev_node.next)
                return True
            prev_node = prev_node.next
            index+=1
        
    def disp(self):
        curr_node = self.start_node
        index = 0
        while (curr_node != None):
            if curr_node.next == None:
                print(curr_node.value)
            else:
                print(curr_node.value,'-->',end=' ')
            curr_node = curr_node.next
            index+=1
    
    def delete_element_from_loc(self,loc):
        if loc >= self.length():
            print('Location/ index does not exist')
            return False
        
        if loc == 0:
            self.start_node = self.start_node.next
            return True
        
        prev_node = self.start_node
        index = 1
        while (prev_node.next != None):
            if index==loc:
                prev_node.next = prev_node.next.next
                return True
            prev_node = prev_node.next
            index+=1
    
    
if __name__ == '__main__':
    my_ll = Linked_list()
    my_ll.insert_element_at_beginning(5)
    my_ll.insert_element_at_beginning(10)
    my_ll.insert_element_at_beginning('and')
    my_ll.insert_element_at_beginning('20')
    print('list length: ',my_ll.length())
    my_ll.disp()
    my_ll.insert_element_at_loc('new',2)
    my_ll.disp()
    print('list length: ',my_ll.length())
    my_ll.change_element_at_loc('changed',2)
    my_ll.disp()
    my_ll.delete_element_from_loc(1)
    my_ll.disp()
    print('list length: ',my_ll.length())