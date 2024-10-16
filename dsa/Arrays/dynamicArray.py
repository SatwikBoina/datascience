# This file contains the implementation of the python arrays

import ctypes

class dynamicArray:
    def  __init__(self,capacity):
        self.size = capacity
        # length of the entire array is n
        self.n = 0
        self.A = self.__makeArray(capacity)

    def __makeArray(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize(self,new_capacity):

        # create the array with new capacity
        B = self.__makeArray(new_capacity)

        # copy the contents of previous array
        for i in range(self.n):
            B[i]  = self.A[i]

        # Assign the new array to the object
        self.A = B
        self.size = new_capacity
    
    def __len__(self):
        # magic function __len__
        return self.n
    
    def __str__(self):
        # magic function __str__
        return f"an array of size {self.size} filled with {self.n} elements"
    
    def append(self,value):
        # check if len of the array is equal to it's size
        if self.n>=self.size:
            self.__resize(new_capacity=2*self.size)
        
        # value assignment if the n < size
        self.A[self.n]=value
        self.n +=1
    def pop(self):

        # check if len(array) is empty
        if self.n == 0:
            return None
        
        # if Not empty
        value = self.A[self.n-1]
        self.n -=1
        return value
    def clear(self):
        self.n = 0

    def __getitem(self,index):
        if 0<= index< self.n:
            return self.A[index]
        else:
            return None

    def find(self,value):
        # returns the index of the value else None if not found
        # linear search for an unsorted array
        for i in range(self.n):
            if value==self.A[i]:
                return i
        return None
    
    def insert(self,value,index):

        if self.size == self.n:
            self.__resize(2*self.size)
        
        for i in range(self.n,index,-1):
            self.A[self.n] = self.A[self.n-1]
        self.A[index]=value
        self.n +=1
    def __delitem__(self,index):
        # delete the value found at the index
        if 0<=index<self.n:
            for i in range(index,self.n):
                self.A[i]=self.A[i+1]
            self.n -=1
    def remove(self,value):
        # find the item's index first
        index = self.find(value = value)
        # delete the value found at the index
        if index is not None:
            self.__delitem__(index = index)

    
# creating an array
arr = dynamicArray(capacity = 3)

# appending values 1, 3
arr.append(3)
arr.append(1)
print(arr.A[0],arr.A[1])

# inserting 2 at index 1
arr.insert(value = 2, index =1)
print(arr.A[1])

# Now, the size and length are same
print(f"size : {arr.size},length = {arr.n}")

# Now, Insert 7 at index 3
arr.insert(value = 7,index = 3)
print(arr.A[3])

# popping
print(arr.pop())

# removing at 0
arr.remove(1)
print(arr.A[0])