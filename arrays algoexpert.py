# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:37:02 2020

@author: mourya
"""
""" two sum"""
def twosum(a,num):
    dic={}
    for ele in a:
        dic[ele]=None
    print (dic)
    for ele in a:
        x=num-ele
        if x!=ele and x in dic.keys():
            return (ele,x)
    return -1
# a=[0, -1, 0, -3, 1]
# s=3
# print (twosum(a, s))

"""is subsequence"""
def issubsequence(str1,str2):
    a=list(str1)
    b=list(str2)
    i=0
    for char in b:
        if char==a[i]:
            i+=1
    if i==len(a):
        return True
    return False
# str1 = "AXY"
# str2 = "ADXCPY"
# print (issubsequence(str1, str2))

"""three sum"""
def threesum(a,num):
    if len(a)<3:
        return "not possible"
    dic={}
    for ele in a:
        if ele not in dic.keys():
            dic[ele]=1
        else:
            dic[ele]+=1
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            s=num-(a[i]+a[j])
            if a[i]==a[j]:
                if s==a[i]:
                    if dic[s]>=3:
                        return (a[i],a[j],s)
                else:
                    if s in dic.keys():
                        return (a[i],a[j],s)
            else:
                if s==a[i] or s==a[j]:
                    if dic[s]>=2:
                        return (a[i],a[j],s)
                else:
                    if s in dic.keys():
                        return (a[i],a[j],s)
    return -1

""" smallest difference"""
import sys
def smalldiff(a):
    if len(a)<2:
        return "nt possible"
    b=sorted(a)
    diff=sys.maxsize
    for i in range(0,len(a)-1):
        if abs(a[i+1]-a[i]) <diff:
            diff=abs(a[i+1]-a[i])
    return diff
# a=[1, 5, 3, 19, 18, 25]
# print (smalldiff(a))      

"""monotonic array"""
def monotonic(a):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            return False
    return True

"""spiral traverse"""
def spiraltraverse(a,k,n):
    x=k
    y=n
    for i in range(0,x):
        for j in range(i,y):
            print(a[i][j],end=" ")
        for l in range(i+1,x):
            print (a[l][y-1],end=" ")
        if i==k//2:
            break
        for m in range(y-2,i-1,-1):
            print (a[x-1][m],end=" ")
        
        for h in range(x-2,i,-1):
            print (a[h][i],end=" ")
        x=x-1
        y=y-1
    return       
            
# a=[ [1, 2, 3, 4], 
#       [5, 6, 7, 8], [ 9, 10, 11, 12],
#       [13, 14, 15, 16] ] 
# spiraltraverse(a, 4, 4)
"""longest peak"""
import math
def longestpeak(a):
    mini=-math.inf
    count=0
    peakrange=0
    i=0
    for i in range(i,len(a)):
        
        while (i<len(a) and a[i]>mini):
            count+=1
            mini=a[i]
            i+=1
        if i==len(a):
            count=0
            break
        while(i<len(a) and a[i]<mini):
            count+=1
            mini=a[i]
            i+=1
        if peakrange<count:
            if count>1:
                peakrange=count
        count=1
    return peakrange

# a=[1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]  
# a=[2,4,3]
# print(longestpeak(a))        
        
"""sorting suubarray"""
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
def sortsubarr(a):
    if len(a)==0:
        return "no array"
    st=stack()
    i=0
    start=len(a)-1 
    end=len(a)-1
    x=-math.inf
    while i<len(a):
        if a[i]>=x:            
            st.push(a[i])
            x=a[i]
            i+=1
        else:
            while not st.isempty() and st.peek()>a[i]:
                st.pop()
            if st.get_size()<start:
                start=st.get_size()
            end=i
            i+=1
    if start==end:
        return "perfect array"
    else:
        return (start,end)      
# a=[10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
# a=[0, 1, 15, 25, 6, 7, 30, 40, 50]
# print(sortsubarr(a))          
"""max range"""              
def maxrange(a):
    dic={}
    z=0
    for ele in a:
        dic[ele]=False
    for ele in a:
        if dic[ele]==True:
            continue
        while True:
            dic[ele]=True
            ele -=1
            if ele not in dic.keys():
                x=ele+1
                break                    
        while True:
            dic[ele]=True
            ele+=1
            if ele not in dic.keys():
                y=ele-1
                break
        if (y-x)>z:
            m=x
            n=y
            z=y-x
    return ([m,n])
# a=[1,11,3,3,0,15,5,2,4,10,7,12,6]
# print (maxrange(a))

"""zigzag traverse"""
def zigzag(a,k,n):
    i=0
    j=0
    result=[[] for i in range(k+n-1)]
    for i in range(k):
        for j in range(n):
            sum=i+j
            if sum%2==0:
                result[sum].insert(0, a[i][j])
            else:
                result[sum].append(a[i][j])
    for i in result:
        for j in i:
            print(j,end=" ")
                
# a=[[ 1, 2, 3,4], [ 5, 6 ,7,8], [ 9,10,11,12 ],[13,14,15,16] ]   
# zigzag(a, 4, 4)          
            
"""appartment nunting"""
# import math
def ab(a,b):
    return abs(a-b)
def apparthunt(a,ran):
    if len(a)<2:
        return a    
    a.sort()
    if a[0]==a[-1]:
        return a[-1]
    b=[]
    j=0
    prev=a[0]
    while j<len(a):
        while j<len(a):
            if ab(a[j],prev)<ran:
                j+=1

            elif ab(a[j],prev)==ran:
                if b==[]:                
                    b.append(a[j])
                    prev=a[j]
                    j+=1
                elif ab(a[j],b[-1])>ran:
                    b.append(a[j])
                    prev=a[j]
                    j+=1
                else:
                    j+=1
            else:
                if b==[]:
                    b.append(a[j-1])
                elif ab(a[j-1],b[-1])>ran:
                    b.append(a[j-1])
                prev=a[j]
                break
    if ab(a[-1],b[-1])>ran:
        b.append(a[-1])
            
    return b      
# a=[2,5,8]        
# a=[2,4,5,6,7,9,11,12]
# a=[1]
a=[3,]
print(apparthunt(a,2))   
        
        
                
        
            
            
            
            