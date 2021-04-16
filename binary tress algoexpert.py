# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:53:44 2020

@author: mourya
"""
"""binary trees"""
class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def branchsum(root,sume):
    if root is None:
        return sume
    else:
        return root.data+branchsum(root.left, sume)+branchsum(root.right, sume)
        
    return sume
def nodedepth(root,key,depth):
    if root is None:
        return 
    else:
        if root.data==key:
            return (depth)
        else:
            depth+=1
            h=nodedepth(root.left,key,depth)
            if h is not None:
                return h
            return nodedepth(root.right, key, depth)
# if __name__ == '__main__': 
#     root = newnode(93)  
#     root.left = newnode(2)  
#     root.right = newnode(5) 
#     root.left.left = newnode(1)  
#     root.left.right = newnode(4) 
#     # root.left.right.left = newnode(5)  
#     # root.left.right.right = newnode(7)  
#     # root.right.right = newnode(22) 
#     # root.right.right.left = newnode(20)  
#     print(nodedepth(root, 93, 1))
    # print(branchsum(root, 0))
    
"""inverting a binary tree"""
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data)
        inorder(root.right)
def swap(root):
    temp=root.left
    root.left=root.right
    root.right=temp
def invert(root):
    if root is None:
        return
    else:
       
        invert(root.left)
        invert(root.right)
        swap(root)
            
# if __name__ =="__main__":  
  
#     root = newNode(1)  
#     root.left = newNode(2)  
#     root.right = newNode(3)  
#     root.left.left = newNode(4)  
#     root.left.right = newNode(5)  
  
#     invert(root)
#     inorder(root)

"""max path usm in abinary tree"""
# import math
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
# def maxpathsum(root,sume,a):
#     def pathsum(root,sume):
#         if root.left is None and root.right is None:
#             if root.data<0:
#                 a.append(root.data)
#                 return 0
#             return root.data
#         elif root.left and root.right is None:
#             m=pathsum(root.left, sume)
#             if root.data<0:
#                 a.append(m)
#                 s=root.data+m
#                 if (s)>=0:
#                     return s
#                 else:
#                     return 0
#             else:
#                 return root.data+m
#         elif root.right and root.left is None:
#             m=pathsum(root.right, sume)
#             if root.data<0:
#                 a.append(m)
#                 s=root.data+m
#                 if (s)>=0:
#                     return s
#                 else:
#                     return 0
#             else:
#                 return root.data+m
#         else:
#             m=pathsum(root.left, sume)
#             n=pathsum(root.right, sume)
#             if root.data<0:
#                 s=m+n+root.data
#                 if s<0:
#                     a.append(max(m,n))
#                     return 0
#                 else:
#                     a.append(s)
#                     return root.data+max(m,n)
                
#             else:
#                 a.append(root.data+m+n)
#                 return root.data+max(m,n)
#     x=pathsum(root, sume)
#     y=max(a)
#     if y<0:
#         return y
#     return max(x,y)
# Python program to find maximum path sum in Binary Tree 

# A Binary Tree Node 
# 1

# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 
# Python program to find maximum path sum in Binary Tree 

# A Binary Tree Node 
# class Node: 
# 	
# 	# Contructor to create a new node 
# 	def __init__(self, data): 
# 		self.data = data 
# 		self.left = None
# 		self.right = None

# This function returns overall maximum path sum in 'res' 
# And returns max path sum going through root 
def findMaxUtil(root): 
	
	# Base Case 
	if root is None: 
		return 0

	# l and r store maximum path sum going through left 
	# and right child of root respetively 
	l = findMaxUtil(root.left) 
	r = findMaxUtil(root.right) 
	
	# Max path for parent call of root. This path 
	# must include at most one child of root 
	max_single = max(max(l, r) + root.data, root.data) 
	
	# Max top represents the sum when the node under 
	# consideration is the root of the maxSum path and 
	# no ancestor of root are there in max sum path 
	max_top = max(max_single, l+r+ root.data) 

	# Static variable to store the changes 
	# Store the maximum result 
	findMaxUtil.res = max(findMaxUtil.res, max_top) 

	return max_single 

# Return maximum path sum in tree with given root 
def findMaxSum(root): 
	
	# Initialize result 
	findMaxUtil.res = float("-inf") 
	
	# Compute and return result 
	findMaxUtil(root) 
	return findMaxUtil.res 

# Driver program 
# root = Node(10) 
# root.left = Node(2) 
# root.right = Node(10); 
# root.left.left = Node(20); 
# root.left.right = Node(1); 
# root.right.right = Node(-25); 
# root.right.right.left = Node(3); 
# root.right.right.right = Node(4); 
# print ("Max path sum is " ,findMaxSum(root))

"""iterative inorder traversal"""
class stack:
    def __init__(self):
        self.stack=[]
        self.size=0
    def push(self,x):
        self.stack.append(x)
        self.size+=1
    def pop(self):
        data=self.stack[-1]
        del(self.stack[-1])
        self.size-=1
        return data
    def peek(self):
        return self.stack[-1]
    def isempty(self):
        if self.size==0:
            return "True"
        return False
    def get_stack(self):
        return self.stack
    def get_size(self):
        return self.size
def iterativeoredrtraversal(root):
    st=stack()
    curr=root
    while curr:
        st.push(curr)
        if curr.left:
            curr=curr.left
        else:
            while True:
                if st.isempty():
                    break
                pop=st.pop()
                print(pop.data)
                if pop.right:
                    break
                
            curr=pop.right
        
        
# root = Node(10) 
# root.left = Node(2) 
# root.right = Node(10); 
# root.left.left = Node(20); 
# root.left.right = Node(1); 
# root.left.right.right=Node(0)
# root.right.right = Node(-25); 
# root.right.right.left = Node(3); 
# root.right.right.right = Node(4); 
  
# iterativeoredrtraversal(root) 
"""flatten binary tree"""
def flattentree(root):
    if root is not None:
        # print(root.data)
        temp=root.left
        root.left=None
        flattentree(temp)
        temp2=root.right
        root.right=temp
        while temp:
            if temp.right is None:
                break
            temp=temp.right
        if temp:
            temp.right=temp2
        else:
            root.right=temp2
        flattentree(temp2)
        
# root = Node(1) 
# root.left      = Node(2) 
# root.right     = Node(3) 
# root.left.left  = Node(4) 
# root.left.right  = Node(5) 
# flattentree(root)
# print (inorder(root))            
    
"""right sibling tree"""
def findRightSibling(node):
    if node is None:
        return
    if node.parent is None:
        return
    level=0
    def findsibling(node,level):
        
        while node.parent.right==node or (node.parent.right==None and node.parent.left==node):
            
            if node.parent==None:
                return None
            node=node.parent
            level -=1
        node=node.parent.right
        
        while level<0:
            if node.left!=None:
                node=node.left
            elif node.left is None:
                node=node.right
            else:
                break
            level+=1
        if level==0:
            return node
        else:
            return findsibling(node, level)
    return findsibling(node, level)
from collections import defaultdict
class Node:
    def __init__(self,val,parent):
        self.data=val
        self.left=None
        self.right=None
        self.parent=parent
class Tree:
    def __init__(self):
        self.root=None
        self.map_nodes=defaultdict(Node)
        self.size=0
    def Insert(self,parent,child,dir):
        if self.root is None:
            root_node=Node(parent, None)
            child_node=Node(child,root_node)
            if dir=='L':
                root_node.left=child_node
            else:
                root_node.right=child_node
            self.root=root_node
            self.map_nodes[parent]=root_node
            self.map_nodes[child]=child_node
            
            return
        parent_node=self.map_nodes[parent]
        child_node=Node(child,parent_node)
        self.map_nodes[child]=child_node
        if dir=='L':
            parent_node.left=child_node
        else:
            parent_node.right=child_node
        return

def getNode(root,k):
    global keyNode
    if not root:
        return
    getNode(root.left,k)
    if k==root.data:
        keyNode=root
        return keyNode
    getNode(root.right,k)

# if __name__=='__main__':
#     test_cases=int(input())
#     for cases in range(test_cases):
#         n=int(input())
#         a=list(map(str,input().strip().split()))
#         print(a)
        
#     tree=Tree()
#     i=0
#     while i<len(a):
#         parent=int(a[i])
#         child=int(a[i+1])
#         dir=a[i+2]
#         i+=3
#         tree.Insert(parent, child, dir)
#     # for key in (tree.map_nodes):
#     #     print (tree.map_nodes[key].data)
#     k=int(input())
#     keyNode=None
#     print (getNode(tree.root, k)   )
#     print (keyNode)
#     ans=findRightSibling(keyNode)
#     if ans:
#         print(ans.data)
#     else:
#         print(-1)
class newNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data)
        inorder(root.right)    
def allnodesdepths(root,depth):
    if root is None:
        return
    else:
        root.data=depth
        allnodesdepths(root.left, depth+1)
        allnodesdepths(root.right, depth+1)
if __name__=='__main__':
    
    root = newNode(3)  
    root.left = newNode(2)  
    root.right = newNode(5)  
    root.left.left = newNode(1)  
    root.left.right = newNode(4)  
    allnodesdepths(root, 0)
    inorder(root)

    