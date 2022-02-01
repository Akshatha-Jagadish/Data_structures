# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:56:41 2022

@author: Akshatha
"""

class Binary_Tree_Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_Tree_Node(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_Tree_Node(data)
                
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()    
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
        
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        elements = self.in_order_traversal()
        return sum(elements)
    
    def delete(self,data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self
        
    def delete_try_1(self, data, parent = None, direction = 0):
        if not self.search(data):
            return False
        if self.data == data:
            if self.left:
                temp = self.left.find_max()
                self.data = temp
                return self.left.delete(temp, self, 0)
            if self.right:
                temp = self.right.find_min()
                self.data = temp
                return self.right.delete(temp, self, 1)
            if parent and direction:
                parent.right = None
                return True
            if parent and not direction:
                parent.left = None
                return True
            if not parent:
                self.data = None
                return True
        if data < self.data:
            return self.left.delete(data,self,0)
        if data > self.data:
            return self.right.delete(data,self,1)
            
def build_tree(node_vals):
    root = Binary_Tree_Node(node_vals[0])
    for value in node_vals:
        root.add_child(value)
    return root
        
if __name__ == '__main__':
    node_vals = [15,12,14,27,27,88,20,7,23,12]
    tree = build_tree(node_vals)
    print('in order traversal:',tree.in_order_traversal())
    print('pre order traversal:',tree.pre_order_traversal())
    print('post order traversal:',tree.post_order_traversal())
    print('Is 25 there in tree?',tree.search(25))
    print('Is 23 there in tree?',tree.search(23))
    print('minimum value in tree:',tree.find_min())
    print('maximum value in tree:',tree.find_max())
    print('sum of all elements in tree set:',tree.calculate_sum())
    tree.delete(23)
    print('in order traversal after deleting 23:',tree.in_order_traversal())
    