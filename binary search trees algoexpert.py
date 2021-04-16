# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 20:46:16 2020

@author: mourya
"""
"""binary trees and bst's"""
class treeNode:
    def __init__(self,data):        
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)+" "+str(self.left)+" "+str(self.right)
class binarysearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def insert(self,data):
        if self.root is None:
            self.root=treeNode(data)
            self.size+=1
        else:
            temp=self.root
            while True:
                if data<temp.data:
                    if temp.left is None:
                        temp.left=treeNode(data)
                        break
                    else:
                        temp=temp.left
                elif data>temp.data:
                    if temp.right is None:
                        temp.right=treeNode(data)
                        break
                    else:
                        temp=temp.right
            
            self.size+=1
                    
    def search(self,data):
        temp=self.root
        def searchrec(temp,data):            
            if temp is None or temp.data==data:
                return temp
            elif data<temp.data:
                return searchrec(temp.left, data)
            else:
                return searchrec(temp.right, data)
        return searchrec(temp, data)
    def inorder(self):
        root=self.root
        def inordering(root):
            if root is None:
                return
            inordering(root.left)
            print (root.data)
            inordering(root.right)
        return inordering(root)
    def minvalueNode(self,node):
        if node is None:
            return
        mini=node
        while mini.left:
            mini=mini.left
        return mini
    
    def maxvalue(self,node):
        if node is None:
            return
        maxi=node
        while maxi.right:
            maxi=maxi.right
        return maxi
    def parent(self,data):
        if self.root is None:
            return None
        elif self.root.data==data:
            return self.root
        else:
            curr=self.root
            prev=None
            while curr.data!=data:
                if data<curr.data:
                    prev=curr
                    curr=curr.left
                elif data>curr.data:
                    prev=curr
                    curr=curr.right
                if curr is None:
                    print ("not found")
                    return
            return prev
    def pred(self,node):
        if node.left !=None:            
            return self.maxvalue(node.left)
        else:
            curr=node
            while curr.data<node.data:
                curr=self.parent(curr.data)
                if curr.data==self.root.data:
                    return 
            return curr
            
    def delete(self,data):
        prev=None
        curr=self.root
        while True:
            if data<curr.data:
                prev=curr
                curr=curr.left
                if curr==None:
                    return "not found"
            elif data>curr.data:
                prev=curr
                curr=curr.right
                if curr==None:
                    return "not found"
            else:
                if curr.left==None and curr.right==None:
                    if prev.left==curr:
                        prev.left=None
                        self.size-=1
                        return 
                    elif prev.right==curr:
                        prev.right=None
                        self.size-=1
                        return 
                elif curr.left==None:
                    if prev.right==curr:
                        prev.right=curr.right
                        curr.right=None
                        self.size-=1
                        return 
                    if prev.left==curr:
                        prev.left=curr.right
                        curr.right=None
                        self.size-=1
                        return
                elif curr.right==None:
                    if prev.right==curr:
                        prev.right=curr.left
                        curr.left=None
                        self.size-=1
                        return
                    if prev.left==curr:
                        prev.left=curr.left
                        curr.left=None
                        self.size-=1
                        return
                else:
                    pred=self.pred(curr)
                    data=pred.data
                    parent=self.parent(pred.data)
                    
                    curr.data=pred.data
                    bt_new=binarysearchTree()
                    bt_new.root=parent
                    
                    bt_new.delete(data)
                    
                    self.size-=1
                    return
    def get_root(self):
        return self.root
    def get_size(self):
        return self.size
# bt=binarysearchTree()
# bt.insert(10)            
# bt.insert(5)
# bt.insert(1)
# bt.insert(2)
# bt.insert(7)
# bt.insert(40)
# bt.insert(50)
# bt.insert(1.5)
# # bt.inorder() 
                
"""closest value in bst"""
import math
class newnode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def closestvalue(root,key):
    mindiff=math.inf
    prev=None
    def close(root,mindiff,prev):
        if root is None:
            return None
        else:
            if root.data ==key:
                return root.data
            elif key<root.data:
                diff=abs(key-root.data)
                
                if diff<mindiff:
                    prev=root.data
                    return close(root.left,diff,prev)
                else:
                    return prev
            elif key>root.data:
                diff=abs(key-root.data)
                
                if diff<mindiff:
                    prev=root.data
                    return close(root.right,diff,prev)
                else:
                    return prev
    return close(root,mindiff,prev)
                                    
# if __name__ == '__main__': 
#     root = newnode(9)  
#     root.left = newnode(4)  
#     root.right = newnode(17) 
#     root.left.left = newnode(3)  
#     root.left.right = newnode(6) 
#     root.left.right.left = newnode(5)  
#     root.left.right.right = newnode(7)  
#     root.right.right = newnode(22) 
#     root.right.right.left = newnode(20)  
#     k = 12
#     print (closestvalue(root, k))

"""validate bst"""
def isvalidate(root):
    if root is None:
        return
    else:
        def validate(root):
            if root.left and root.right:
                if root.left.data>root.data:
                    return False
                elif root.right.data<root.data:
                    return False
                else:
                    x= validate(root.left) 
                    y= validate(root.right)
                    return (x and y)
            elif root.left is None and root.right is None:
                return True
            elif root.left is None and root.right is not None:
                if root.right.data<root.data:
                    return False
                else:
                    return validate(root.right)
            elif root.right is None and root.left is not None:
                if root.left.data>root.data:
                    return False
                else:
                    return validate(root.left)
            
        if validate(root)==False:
            return "not a bst"
        else:
            return "is bst"
# if __name__ == '__main__': 
#     root = newNode(3)  
#     root.left = newNode(2)  
#     root.right = newNode(5)  
#     root.right.left = newNode(1)  
#     root.right.right = newNode(4)  
#     print (isvalidate(root))

"""bst traversal"""
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data)
        inorder(root.right)
def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
# if __name__ == '__main__': 
#     root = newnode(9)  
#     root.left = newnode(4)  
#     root.right = newnode(17) 
#     root.left.left = newnode(3)  
#     root.left.right = newnode(6) 
#     root.left.right.left = newnode(5)  
#     root.left.right.right = newnode(7)  
#     root.right.right = newnode(22) 
#     root.right.right.left = newnode(20)  
#     inorder(root)
#     print ("\n")
#     preorder(root)
#     print("\n")
#     postorder(root)
#     print("\n")

"""min heightb of a binary tree"""
def minheight(root,height):
    if root is None:
        return              
    if root.left is not None and root.right is  None:
        height +=1
        return minheight(root.left, height)
    elif root.right is not None and root.left is None:
        height +=1
        return minheight(root.right, height)
    elif root.left and root.right:
        height+=1
        h1=minheight(root.left, height)
        h2=minheight(root.right, height)
        height=min(h1,h2)
        return height
    else:
        height+=1
        return height
    # if root is None:
    #     return height
    # else:
    #     return 1+min(minheight(root.left, height),minheight(root.right, height))
        
    
    
if __name__ == '__main__': 
    root = newnode(9)  
    root.left = newnode(4)  
    root.right = newnode(17) 
    root.left.left = newnode(3)  
    root.left.right = newnode(6) 
    root.left.right.left = newnode(5)  
    root.left.right.right = newnode(7)  
    root.right.right = newnode(22) 
    root.right.right.left = newnode(20)  
    print (minheight(root, 0))

"""identical bsts"""
import sys
def issamebsts(a,b,n):
    if n==0:
        return True
    if a[0]!=b[0]:
        return False
    if n==1:
        return True
    def identical(a,b,i,j,mini,maxi):
        while i<n:
            if a[i]>mini and a[i]<maxi:
                break
            else:
                i+=1
        while j<n:
            if b[j]>mini and b[j]<maxi:
                break
            else:
                j+=1
        
        if i==n and j==n:
            return True
        if a[i]!=b[j]:
            return False
        return identical(a, b, i+1, j+1, a[i], maxi) and identical(a, b, i+1, j+1, mini, a[i])
        
    return identical(a, b, 1, 1, a[0], sys.maxsize) and identical(a, b, 1, 1,-sys.maxsize, a[0])
        
# a=[8, 3, 6, 1, 4, 7, 10, 14, 13]
# b=[8, 10, 14, 3, 6, 4, 1, 7, 13]
a=[2, 4, 1, 3]
b=[2, 4, 3, 1]
print (issamebsts(a, b, len(a)))