# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:51:55 2020

@author: mourya
"""
""" minHeap function"""

# class MinHeap:
#     def __init__(self,arr=[]):
#         if len(arr)==0:
#             self.a=[]
#             self.size=0
#         else:
#             self.a=arr
#             size=len(arr)
#             self.size=size
        
            
            
#     def parent(self,i):
#         return (i-1)//2
#     def left(self,i):
#         return 2*i+1
#     def right(self,i):
#         return 2*i+2
#     def isLeaf(self,i):
#         if i<self.size and i>self.size//2:
#             return True
#         return False
#     def minHeapify(self,i):
#         smallest=i
#         #print(i)
#         if self.left(i)<self.size:
#             if self.a[self.left(i)]<self.a[smallest]:                
#                 smallest=self.left(i)
#         if self.right(i)<self.size :
#             if self.a[self.right(i)]<self.a[smallest]:
#                 smallest=self.right(i)
#         if smallest !=i:
#             self.a[i],self.a[smallest]=self.a[smallest],self.a[i]
#             self.minHeapify(smallest)
    
   
#     def insert(self,num):
#         if self.size==0:
#             self.a.append(num)
#             self.size+=1
#             #print (1)
#         else:
#             self.a.append(num)
#             self.size+=1
#             current=self.size-1
#             while self.a[self.parent(current)]>self.a[current] and current>0:
                
#                 self.a[self.parent(current)],self.a[current]=self.a[current],self.a[self.parent(current)]
                
#                 current = self.parent(current)
                
#         #print (self.a,self.size)

#     def minHeap(self):
#         for i in range(self.size//2,-1,-1):
#             #print (1)
#             self.minHeapify(i)
#     def remove(self):
#         pop=self.a[0]
#         self.a[0],self.a[self.size-1]=self.a[self.size-1],self.a[0]
#         del(self.a[self.size-1])
#         self.size -=1
#         self.minHeapify(0)
        
#         return pop
#     def extract_min(self):
#         return self.a[0]
#     def build_min_Heap(self):
#         for i in range((self.size//2)-1,-1,-1):
#             #print (i)
#             self.minHeapify(i)
#     def get_Heap(self):
#         return self.a
#     def get_size(self):
#         return self.size

# # if __name__=="__main__":
# #     minHeap = MinHeap() 
# #     minHeap.insert(5) 
# #     minHeap.insert(3) 
# #     minHeap.insert(17) 
# # #     minHeap.insert(10) 
# # #     minHeap.insert(84) 
# # #     minHeap.insert(19) 
# # #     minHeap.insert(6) 
# # #     minHeap.insert(22) 
# # #     minHeap.insert(9) 
# # #     #minHeap.insert(1)
# # #     print (minHeap.get_Heap())
# #     print (minHeap.remove())
# #     print (minHeap.get_Heap())
# #     minHeap.minHeap()
# #     a=[17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
# #     minHeap1=MinHeap(a)
# #     minHeap1.build_min_Heap()
# #     print (minHeap1.get_Heap())

# class MaxHeap:
#     def __init__(self,arr=[]):
#         if len(arr)==0:
#             self.a=[]
#             self.size=0
#         else:
#             self.a=arr
#             size=len(arr)
#             self.size=size
        
            
            
#     def parent(self,i):
#         return (i-1)//2
#     def left(self,i):
#         return 2*i+1
#     def right(self,i):
#         return 2*i+2
#     def isLeaf(self,i):
#         if i<self.size and i>self.size//2:
#             return True
#         return False
#     def maxHeapify(self,i):
#         largest=i
#         #print(i)
#         if self.left(i)<self.size:
#             if self.a[self.left(i)]>self.a[largest]:                
#                 largest=self.left(i)
#         if self.right(i)<self.size :
#             if self.a[self.right(i)]>self.a[largest]:
#                 largest=self.right(i)
#         if largest !=i:
#             self.a[i],self.a[largest]=self.a[largest],self.a[i]
#             self.maxHeapify(largest)
    
   
#     def insert(self,num):
#         if self.size==0:
#             self.a.append(num)
#             self.size+=1
#             #print (1)
#         else:
#             self.a.append(num)
#             self.size+=1
#             current=self.size-1
#             while self.a[self.parent(current)]<self.a[current] and current>0:
                
#                 self.a[self.parent(current)],self.a[current]=self.a[current],self.a[self.parent(current)]
                
#                 current = self.parent(current)
                
#         #print (self.a,self.size)

#     def maxHeap(self):
#         for i in range(self.size//2,-1,-1):
#             #print (1)
#             self.maxHeapify(i)
#     def remove(self):
#         pop=self.a[0]
#         self.a[0],self.a[self.size-1]=self.a[self.size-1],self.a[0]
#         del(self.a[self.size-1])
#         self.size -=1
#         self.maxHeapify(0)
        
#         return pop
#     def extract_max(self):
#         return self.a[0]
#     def build_max_Heap(self):
#         for i in range((self.size//2)-1,-1,-1):
#             #print (i)
#             self.maxHeapify(i)
#     def get_Heap(self):
#         return self.a
#     def get_size(self):
#         return self.size
    
# # if __name__=="__main__":
# #     minHeap = MaxHeap() 
# #     minHeap.insert([5,0]) 
# #     minHeap.insert([3,1]) 
# # #     # minHeap.insert(17) 
# # #     # minHeap.insert(10) 
# # #     # minHeap.insert(84) 
# # #     # minHeap.insert(19) 
# # #     # minHeap.insert(6) 
# # #     # minHeap.insert(22) 
# # #     # minHeap.insert(9) 
# # #     # minHeap.insert(1)
# # #     # print (minHeap.get_Heap())
# #     print (minHeap.remove())
# #     print (minHeap.get_size())
#     # print (minHeap.get_Heap())
#     #minHeap.maxHeap()
#     # a=[17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
#     # a=sorted(a)
#     # #print (a)
#     # minHeap1=MaxHeap(a)
#     # minHeap1.build_max_Heap()
#     # print (minHeap1.get_Heap())
    
    
""""continous median"""
# def continous_median():
#     minHeap=MinHeap()
#     maxHeap=MaxHeap()
    
#     count =0
#     while True:
#         newNum=int(input("enter a number: "))
#         if newNum == -1:
#             print ("sequence ended")
#             break
#         count+=1
#         if count<2:
#             med=newNum
        
#         elif count ==2:
#             x=max(med,newNum)
#             y=min(med,newNum)
#             minHeap.insert(x)
#             maxHeap.insert(y)
#         else:
#             if (minHeap.get_size()==maxHeap.get_size()):
#                 if newNum>maxHeap.extract_max():
#                     minHeap.insert(newNum)
#                 else:
#                     maxHeap.insert(newNum)
#             elif (minHeap.get_size()>maxHeap.get_size()):
#                 if newNum<=minHeap.extract_min():
#                     maxHeap.insert(newNum)
#                 else:
#                     x=minHeap.extract_min()
#                     minHeap.remove()
#                     maxHeap.insert(x)
#                     minHeap.insert(newNum)
#             else:
#                 if newNum>=maxHeap.extract_max():
#                     minHeap.insert(newNum)
#                 else:
#                     x=maxHeap.extract_max()
#                     maxHeap.remove()
#                     minHeap.insert(x)
#                     maxHeap.insert(newNum)
             
#         # @print (maxHeap.get_Heap())
#         # print (minHeap.get_Heap())
#         if count%2==1:
#             if count==1:
#                 print ("median of "+str(count)+" entries is "+str(med))
#             else:
#                 maxHeapSize=maxHeap.get_size()
#                 minHeapSize=minHeap.get_size()
#                 if minHeapSize>maxHeapSize:
#                     print ("median of "+str(count)+" entries is "+str(minHeap.extract_min()))
#                 else:
#                     print ("median of "+str(count)+" entries is "+str(maxHeap.extract_max()))
                    
#         elif count%2==0 and count >1:
#             median= (minHeap.extract_min()+maxHeap.extract_max())/2
#             print ("median of "+str(count)+" entries is "+str(median))
            
                
"""merging k sorted arrays"""       
        
        
# def merging(a,k,n):
#     minHeap=MinHeap()
#     for i in range(n):        
#         for j in range(k):            
#             minHeap.insert(a[j][i])    
#     for l in range(n*k):
#         print (minHeap.remove(),end=" ")
#         #print (minHeap.get_size())
# # #a=[[1, 5, 6, 8],[2, 4, 10, 12],[3, 7, 9, 11]]
# a=[[1, 3, 5, 7],[2, 4, 6, 8],[0, 9, 10, 11]]
# k=len(a)
# n=len(a[0])
# print (k)
# print (n)
# merging(a, k, n)

import sys  
# from typing import list
# matrix=list[list[int]]  
class minHeapNode:
    def __init__(self,ele,i,j):
        self.element=ele     #value of element in the array        
        self.i=i             #array index where elemnt is
        self.j=j             #index of next element in the array to be picked
    def __str__(self):
        return str(self.element)
class minHeap:
    def __init__(self,a,size:int):
        self.size=size
        self.a=a
        i=(self.size-1)//2
        while (i>=0):
            self.minHeapify(i)
            i-=1
        
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def minHeapify(self,i):
        smallest=i
        #print(i)
        if self.left(i)<self.size:
            
            if self.a[self.left(i)].element<self.a[i].element:                
                smallest=self.left(i)
        if self.right(i)<self.size :
            if self.a[self.right(i)].element<self.a[smallest].element:
                smallest=self.right(i)
        if smallest !=i:
            self.a[i],self.a[smallest]=self.a[smallest],self.a[i]
            self.minHeapify(smallest)

    def get_min(self): 
        if self.size <= 0: 
            print('Heap underflow') 
            return None
        return self.a[0]     
    def replace_min(self,root):
        self.a[0]=root
        self.minHeapify(0)
    def get_arr(self):
        for ele in self.a:
            print (ele,end=" ")
        print ()

def merge_k_sorted(b,k:int):
    h_arr=[]
    result_size=0
    for i in range(k):
        node=minHeapNode(b[i][0], i, 1)
        #print(node)                    #"""creating heap array with k nodes"""
        h_arr.append(node)
        result_size+=len(a[i])
    
    minheap=minHeap(h_arr, k)
    #result=[0]*result_size
    for i in range(result_size):
        (minheap.get_arr())
        root=minheap.get_min()
        #print (root.element,end=" ")
        #result[i]=root.element
        if root.j<len(b[root.i]):
            root.element=a[root.i][root.j]
            root.j+=1
        else:
            root.element=sys.maxsize
        minheap.replace_min(root)
    #print (result)
    print ()
    print ("end")    

a=[[1, 3, 5, 12],[2, 4, 6, 8],[0, 0.5, 10, 11]]
k=len(a)
n=len(a[0])

merge_k_sorted(a, k)