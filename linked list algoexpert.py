# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:13:02 2020

@author: mourya
"""
"""linked list construction"""
class Node:
    def __init__(self,val,nextNode=None):
        self.data= val
        self.nextNode=nextNode
        # self.flag=False
    def __str__(self):
        return str(self.data)+" "+str(self.nextNode)
class linkedList:
    def __init__(self):
        self.root=None
        self.size=0
        self.head=None
        self.end=None
    def insert(self,num):
        if self.size==0:
            self.head=Node(num)
            # self.head.flag=True
            self.root=self.head.data
            self.size+=1
            self.end=self.head
            # print (self.head)
        else:
            temp=self.end
            
            
            # while temp.nextNode!=None:
            #     print(temp.data)
            #     temp=temp.nextNode  
                
            temp.nextNode=Node(num)
            # temp.nextNode.flag=True
            self.end=temp.nextNode
            self.size+=1
            # print(temp.nextNode)
    def delete(self,data):
        temp=self.head
        if temp.data==data:
            self.head=self.head.nextNode
            self.size-=1
            print(self.head.data)
        else:            
            while temp.data!=data:
                previous=temp                
                temp=temp.nextNode
                if temp.nextNode is None:
                    break
            if temp.data==data:
                previous.nextNode=temp.nextNode
                if temp.nextNode==None:
                    self.end=previous
                self.size-=1
            else:
                print ("data is not in the linked list")
   
    def search(self,data):
        temp=self.head
        found=False
        while temp.data!=data:
            temp=temp.nextNode
            if temp==None:
                break
            if temp.data==data:
                found = True
                break
        return found
   
    def removeKthnode(self,k):
        if k>=self.size:
            print ("not possible")
            return
        n=self.size-k
        if n==1:
            self.delete(self.head.data)
            return
        current=self.head
        for i in range(n-1):
            previous=current
            current=current.nextNode
        previous.nextNode=current.nextNode
    
    def detectloop(self):
        current=self.head
        
        while current:
            current.flag=True
            current=current.nextNode
            if current.nextNode.flag==True:
                print("loop is found")
                return
        print ("no loop found")
        return
   
    def __iter__(self):
        self.current=self.head
        return self
    
    def __next__(self):
        while self.current is not None:
            
            temp= (self.current)
            self.current=self.current.nextNode
            return temp.data
       
        else:
            raise StopIteration
    def get_head(self):
        return self.head
    def get_nextNode(self,node):
        return node.nextNode
    def get_end(self):
        return self.end
    def get_size(self):
        return self.size
    def reversing(self,curr,prev):
        if curr.nextNode == None:
            self.head=curr
            curr.nextNode=prev
            return
        next=curr.nextNode
        curr.nextNode=prev
        self.reversing(next,curr)
    def reverse(self):
        if self.head==None:
            return
        self.reversing(self.head, None)
    def prints(self):
        temp=self.head
        while temp:
            print (temp.data)
            temp=temp.nextNode
    def reversinwithoutrecursion(self,curr):
        left=None
        # curr=self.head
        # right=curr.nextNode
        while(curr):
            temp=curr.nextNode
            curr.nextNode=left
            left=curr
            curr=temp
        curr=left   
        return curr
           
    def merginglists(self,l):
        i=self.head
        j=l.head
        if i.data<=j.data:
            head=i
            current=head
            i=i.nextNode
            while True:
                if i!=None and j!=None:
                    if i.data<=j.data:                        
                        current.nextNode=i
                        i=i.nextNode
                        current=current.nextNode
                    else:
                        current.nextNode=j
                        j=j.nextNode
                        current=current.nextNode
                elif i==None:
                    current.nextNode=j
                    break
                elif j==None:
                    current.nextNode=i
                    break
        else:
            head=j
            current=head
            j=j.nextNode
            while True:
                if i!=None and j!=None:
                    if i.data<=j.data:                        
                        current.nextNode=i
                        i=i.nextNode
                        current=current.nextNode
                    else:
                        current.nextNode=j
                        j=j.nextNode
                        current=current.nextNode
                elif i==None:
                    current.nextNode=j
                    break
                elif j==None:
                    current.nextNode=i
                    break
        return head
    
    def rotateList(self,k:int):
        if k>=self.size:
            print("k is greater than list size")
            return
        current=self.head
        temp=self.head
        for i in range(k-1):
            current=current.nextNode
        next=current.nextNode
        self.head=next
        current.nextNode=None
        while next.nextNode:
            next=next.nextNode
        next.nextNode=temp
        return self.head
    
    def rearrangelist(self):
        # if not self.head:
        #     return None 
        # if current.nextNode.nextNode is None:
        #     return 
        # else:            
        #     temp=current
        #     while temp.nextNode.nextNode is not None:
        #         temp=temp.nextNode
        #     middle=current.nextNode
        #     current.nextNode=temp.nextNode
        #     current.nextNode.nextNode=middle
        #     temp.nextNode=None
        #     # print (temp.data)
        #     return self.rearrangelist(middle)
        if not self.head:
            return None
        temp=self.head
        count=0
        while count<(self.size//2-1):
            temp=temp.nextNode
            count+=1
        current=temp.nextNode
        temp.nextNode=None
        curr=linkedList()
        curr.head=self.reversinwithoutrecursion(current)
        current=self.head
        current2=curr.head
        while True:
            if current.nextNode==None:
                current.nextNode=current2
                break
            
            temp=current.nextNode                
            temp2=current2.nextNode
            current.nextNode=current2
            current2.nextNode=temp
            current2=temp2
            current=temp
        return         
                
                
        
ll=linkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
    ll.insert(60)
# print (ll.reversinwithoutrecursion(ll.get_head()))
ll.rearrangelist()
ll.prints()
# ll.prints()
# l_rot=linkedList()
# l_rot.head=ll.rotateList(6)
# l_rot.prints()
# lt=linkedList()
# lt.insert(0)
# lt.insert(7)
# l_merge=linkedList()
# l_merge.head=ll.merginglists(lt)
# # ll.reverse()
# # ll.reversinwithoutrecursion()
# # print (ll.get_head())
# # ll.prints()
# l_merge.prints()
# for x in ll:
#     print(x)
# ll.insert(15)
# ll.insert(13)
# ll.insert(20)
# ll.insert(22)
# ll.delete(3)
# ll.delete(22)
# print (ll.search(40))
# for x in ll:
#     print (x)
"""remove kth node from end of the list"""
# ll.removeKthnode(3)
# for x in ll:
#     print (x.get_nextNode())
# ll.get_end().nextNode=ll.get_head().nextNode.nextNode
# ll.detectloop()

    