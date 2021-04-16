# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:19:52 2020

@author: mourya
"""
""" binary search"""
def binarySearch(a:list,ele:int):
    l=0
    h=len(a)-1
    
    def search(a,l,h):
        if l==h:
            if a[l]==ele:
                return ("index is "+str(l))
            else:
                return (str(ele)+" not in array")
        else:
            mid=(l+h)//2
            if a[mid]==ele:
                return ("index is "+str(mid))
            else:
                if a[mid]>ele:
                    return search(a,l,mid-1)
                else:
                    return search(a,mid+1,h)
    
    return search(a, l, h)
    
# a=[ 2, 3, 10, 10, 40 ] 
# x=40
# print(binarySearch(a, x))

"""find three largest numbers"""
import random
def partition(a,l,h):
    n=random.randint(l, h)
    a[n],a[l]=a[l],a[n]
    pivot=a[l]
    i=l
    for j in range(l+1,h+1):
        if a[j]<pivot:
            a[i+1],a[j]=a[j],a[i+1]
            i+=1
    a[i],a[l]=a[l],a[i]
    return i
def qselect(a,l,h,i):
    
    x=partition(a, l, h)
    if x==i:
        return a[i]
    elif x<i:
        return qselect(a, x+1, h, i)
    else:
        return qselect(a, l, x-1, i)  
def threelarge(a,l,h):
    i=len(a)-3
    qselect(a, l, h, i)
    
    if a[i+2]<a[i+1]:
        a[i+1],a[i+2]=a[i+2],a[i+1]
    for x in range(len(a)-1,len(a)-4,-1):
        print (a[x],end=" ")
    print ()
a=[10, 4, 3, 50, 23, 90]      
# threelarge(a, 0, len(a)-1)
# print (a)

import math
def threelargenumbers(a):
    first,second,third=-math.inf,-math.inf,-math.inf
    for ele in a:
        if ele>first:
            third=second
            second=first
            first=ele
        elif ele>second:
            third=second
            second=ele
        elif ele>third:
            third=ele
    print (first,second,third)

a=[10, 4, 3, 50, 23, 90]
# threelargenumbers(a)

"""search in a sorted matrix"""
def sortedsearchmatrix(a,ele,k):
    l=0
    h=k-1
    def binary_search(a,l,h):
        if l==h:
            return l
        else:
            mid=(l+h)//2
            if a[mid][0]<=ele and a[mid+1][0]>=ele:               
                return mid
            elif a[mid][0]<ele and a[mid+1][0]<ele:
                return binary_search(a, mid+1, h)
            else:
                return binary_search(a, l, mid-1)
                
    x=binary_search(a,l,h)  
    # print(len(a[x]))
    
    def search(a,l,h):
        if l==h:
            if a[l]==ele:
                
                return l
            else:
                return -1
        else:
            mid=(l+h)//2
            if a[mid]==ele:
                
                return mid
            else:
                if a[mid]>ele:
                    
                    return search(a,l,mid-1)
                else:
                    
                    return search(a,mid+1,h)    
    y=search(a[x],0,len(a[x])-1)
    
    if y<0:
        return -1
    return (x,y)

# a=[[1,5,9],[14,20,21],[21,34,43]]
# print (sortedsearchmatrix(a, 21, 3))

"""shifted binary search"""
def shiftbinarysearch(a,ele):
    l=0
    h=len(a)-1
    # def bsearch(a,l,h):
    #     if l==h:
    #         if a[l]==ele:
                
    #             return l
    #         else:
    #             return -1
    #     else:
    #         mid=(l+h)//2
    #         if a[mid]==ele:
                
    #             return mid
    #         else:
    #             if a[mid]>ele:
                    
    #                 return search(a,l,mid-1)
    #             else:
                    
    #                 return search(a,mid+1,h)
    def search(a,l,h):
        if l==h:
            if a[l]==ele:                
                return l
        else:
            mid=(l+h)//2
            if a[mid]==ele:                
                return mid
            else:
                if a[l]<=ele and a[mid]>=ele:
                    return search(a, l, mid)
                elif a[l]<ele and a[mid]<=ele:
                    return search(a, mid+1, h)
                elif a[l]>ele and a[mid]<=ele:
                    return search(a, mid+1, h)
                elif a[l]>ele and a[mid]>ele:
                    return search(a, mid+1, h)
    return search(a, l, h)

a=[3,5, 6, 7, 8, 9, 10, 1, 2]
# print (shiftbinarysearch(a,1))     

"""search range"""                    
def searchRange(a,n,k):
    l=0
    h=n-1
    def search(a,l,h):
        if l==h:
            if a[l][0]<=k and a[l][1]>=k:
                return l
            else:
                return -1
        else:
            mid=(l+h)//2
            if a[mid][0]<=k and a[mid][1]>=k:
                return mid
            elif a[mid][1]>k:
                return search(a, l, mid-1)
            else:
                return search(a, mid+1, h)
    return search(a, l, h)
a=[[1,3],[4,4],[8,11]]
print(searchRange(a, len(a), 7))
                
        
                    
                