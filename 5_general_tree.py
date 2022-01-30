# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:11:59 2022

@author: Akshatha
"""

# recursive data structure
class TreeNode():
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self
    
    def print_tree(self,level=0):
        print(self.data)
        level += 1
        for child in self.children:
            print('\t'*level,end=' ')
            child.print_tree(level)
            
            
def build_tree():
    root = TreeNode('Books')
    
    category_1 = TreeNode('Mystery')
    category_1.add_child(TreeNode('Behind her eyes'))
    category_1.add_child(TreeNode('Black water lilies'))
    
    category_2 = TreeNode('Adventure')
    category_2.add_child(TreeNode('Secret seven series'))
    category_2.add_child(TreeNode('Famous five series'))
    
    category_3 = TreeNode('Science Fiction')
    category_3.add_child(TreeNode('Project Hail Mary'))
    category_3.add_child(TreeNode('Deception Point'))
    
    root.add_child(category_1)
    root.add_child(category_2)
    root.add_child(category_3)
    return root
    
if __name__ == '__main__':
    root =  build_tree()
    root.print_tree()
    
    