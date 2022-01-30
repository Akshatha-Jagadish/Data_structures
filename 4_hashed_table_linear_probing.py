# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:39:00 2022

@author: Akshatha
"""

#dictionary is the inbuilt hashed table

class Hashed_Table():
    def __init__(self):
        self.arr_size = 100
        self.arr = [None for i in range(self.arr_size)]
    
    def hashed(self, key):
        hash_sum = 0
        for letter in key:
            hash_sum += ord(letter)
        return hash_sum % self.arr_size
        
    def __setitem__(self, key, value):
        hash_val = self.hashed(key)
        if self.arr[hash_val] == None:
            self.arr[hash_val] = [key, value]
        elif self.arr[hash_val][0] == key:
            self.arr[hash_val][1] = value
        else:
            arr_val = (hash_val+1) % self.arr_size
            while(self.arr[arr_val] != None):
                arr_val += 1
                arr_val = arr_val % self.arr_size
            self.arr[arr_val] = [key, value]
    
    def __getitem__(self, key):
        hash_val = self.hashed(key)
        if self.arr[hash_val] != None:
            if self.arr[hash_val][0] == key:
                return self.arr[hash_val][1]
            else:
                arr_val = (hash_val+1) % self.arr_size
                while(self.arr[arr_val][0] != key):
                    arr_val += 1
                    arr_val = arr_val % self.arr_size
                return self.arr[arr_val][1]
        else:
            # print('key does not exist')
            return None
            
    
if __name__ == '__main__':
    my_hash_table = Hashed_Table()
    my_hash_table['Akshatha'] = 150
    my_hash_table['Aditya'] = 180
    my_hash_table['Ankith'] = 200
    print(my_hash_table.arr)
    my_hash_table['Akshatha'] = 500
    print(my_hash_table.arr)
    my_hash_table['Akshatha D'] = 250
    print(my_hash_table.arr)
    print('Akshatha D', my_hash_table['Akshatha D'])
    print('Akshatha J', my_hash_table['Akshatha J'])
    print('Akshatha', my_hash_table['Akshatha'])