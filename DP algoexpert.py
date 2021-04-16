# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:33:54 2020

@author: mourya
"""
"""max paths sum"""
def maxpathsum(a):
    maxpath_arr=[None]*len(a)
    maxpath_arr[0]=0
    maxpath_arr[1]=a[1]
    for i in range(2,len(a)):
        maxpath_arr[i]=max(maxpath_arr[i-1],maxpath_arr[i-2]+a[i])
    return maxpath_arr,maxpath_arr[i]
def reconstruction_array(max_array,a):
    s=[]
    i=len(max_array)-1
    while i>=1:
        if max_array[i-1]>=max_array[i-2]+a[i]:
            i-=1
        else:
            s.append(a[i])
            i-=2
    return s
# a=[5, 5, 10, 100, 10, 5]
# print (maxpathsum(a))
# print (reconstruction_array(maxpathsum(a)[0], a))

"""no of ways to make coin change"""
def count(S,m,N):
    count_arr=[0]*(N+1)
    count_arr[0]=1
    for i in range(m):
        for j in range(1,N+1):
            if j>=S[i]:
                count_arr[j]+=count_arr[j-S[i]]
    return count_arr[N]
S=[1,5,10]
# print (count(S, len(S), 12))

"""min coins to use : recursive solution"""
import sys
# def mincoins(coins,m,V):
#     if V==0:
#         return 0
#     res=sys.maxsize
#     for i in range(m):
#         if coins[i]<=V:
#             mini=mincoins(coins, m, V-coins[i])
#             if mini!=sys.maxsize and mini+1<res:
#                 res=mini+1
#     return res
def mincoins(coins,m,V):
    if V==0:
        return 0
    table=[sys.maxsize]*(V+1)
    table[0]=0
    for i in range(1,V+1):
        for j in range(m):
            if coins[j]<=i:
                mini=table[i-coins[j]]
                if mini!=sys.maxsize and mini+1<table[i] :
                    table[i]=mini+1
    return table[V] if table[V]!=sys.maxsize else -1
            
# coins = [9, 6, 5] 
# m = len(coins) 
# V = 4
# print (mincoins(coins, m, V))
# def minNumberOfCoinsForChange(n, denoms):
#     numOfCoins = [float("inf") for amount in range(n + 1)]
#     numOfCoins[0] = 0
#     for denom in denoms:
#         for amount in range(n + 1):
#             if denom <= amount:
#                 numOfCoins[amount] = min(
#                     numOfCoins[amount], 1 + numOfCoins[amount - denom])
#     return numOfCoins[n] if numOfCoins[n] != float("inf") else -1


# print(minNumberOfCoinsForChange(7, [ 2, 4]))
"""levenshtein distance"""
def distance(str1,str2,m,n):
    arr=[[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                arr[i][j]= j
            elif j==0:
                arr[i][j]= i
            elif str1[i-1]==str2[j-1]:
                arr[i][j]=arr[i-1][j-1]
            else:
                arr[i][j]= 1 +min(arr[i][j-1],
                                arr[i-1][j],
                                arr[i-1][j-1])
            
    return arr[m][n]
str1 = "geek"
str2 = "gesek"
  
# print(distance(str1, str2, len(str1), len(str2))) 
# A Dynamic Programming based Python program for edit 
# distance problem 
# def editDistDP(str1, str2, m, n): 
# 	dp=[[0 for x in range(n+1)] for x in range(m+1)]

# 	for i in range(m + 1): 
#     		for j in range(n + 1): 

# 			if i == 0: 
# 				dp[i][j] = j # Min. operations = j 


# 			elif j == 0: 
# 				dp[i][j] = i # Min. operations = i 


# 			elif str1[i-1] == str2[j-1]: 
# 				dp[i][j] = dp[i-1][j-1] 


# 			else: 
# 				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert 
# 								dp[i-1][j],	 # Remove 
# 								dp[i-1][j-1]) # Replace 

# 	return dp[m][n] 

# # Driver program 
# str1 = "geek"
# str2 = "gesek"

# print(editDistDP(str1, str2, len(str1), len(str2))) 

"""longest increaing subsequence"""
def lsi(a):
    lis=[0]*(len(a))
    lis[0]=1
    for i in range(1,len(lis)):
        maxi=lis[0]
        count=0
        for j in range(0,i):
            if a[j]<=a[i]:
                count+=1
                maxi=max(maxi,lis[j])
        if count==0:
            lis[i]=1
        else:
            lis[i]=1+maxi
    
    return max(lis)
# a=[10, 22, 9, 33, 21, 50, 41, 60, 80]
# print (lsi(a))
"""max sum increasing sequence"""
# Dynamic programming Python implementation 
# of LIS problem 

# lis returns length of the longest 
# increasing subsequence in arr of size n 
def maxi(arr): 
    n=len(arr)
    lis=[0]*n
    lis[0]=arr[0]
    for i in range(1,n):
        
        for j in range(0,i):
            if arr[j]<=arr[i] and lis[i]<lis[j]+arr[i]:
                lis[i]=lis[j]+arr[i]
    return max(lis)


# Driver program to test above function 
# arr = [1, 101, 2, 3, 100, 4, 5] 
# print (maxi(arr))
# print "Length of lis is", lis(arr) 
# This code is contributed by Nikhil Kumar Singh 
"""longest common subsequence: recursion"""
# def lcs(str1,str2):
#     m=len(str1)
#     n=len(str2)
#     def lcs_rec(str1,str2,m,n):
#         if m==0:
#             return 0
#         elif n==0:
#             return 0
#         elif str1[m-1]==str2[n-1]:
#             return 1+lcs_rec(str1, str2, m-1, n-1)
#         else:
#             (x,y)=(lcs_rec(str1, str2, m, n-1),lcs_rec(str1, str2, m-1, n))
#             return max(x,y)
            
#     return lcs_rec(str1, str2, m, n)

"""longest common subsequence: dp"""
def lcs(str1,str2):
    m=len(str1)
    n=len(str2)
    lcs_arr=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                lcs_arr[i][j]=0
            elif j==0:
                lcs_arr[i][j]=0
            elif str1[i-1]==str2[j-1]:
                lcs_arr[i][j]=1+lcs_arr[i-1][j-1]
            else:
                lcs_arr[i][j]=max(lcs_arr[i][j-1],lcs_arr[i-1][j])
    return lcs_arr[m][n]
                    
# str1="AGGTA"
# str2="GXTXAYB"
# print (lcs(str1,str2))

"""min jumps to reach end: recusive way"""
# import math
# def minjumps(arr,start,end):
#     if start>end:
#         return 0
#     if start==end:
#         return 1
#     elif arr[start]==0:
#         return math.inf
#     else:
#         mini=math.inf
#         for i in range(1,arr[start]+1):
#             x=1+minjumps(arr, start+i, end)
#             if x<mini:
#                 mini=x
#         return mini
# # arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
"""min jumps to reach end: dp"""
import math
def minjumps(arr):
    n=len(arr)
    dp=[0 for i in range(n)]
    if n==0 or arr[0]==0:
        return math.inf
    dp[0]=0
    for i in range(1,n):
        dp[i]=math.inf
        for j in range(i):
            if (i<=j+arr[j]) and dp[j]!=math.inf:
                dp[i]=min(dp[i],dp[j]+1)
                break
    return dp[n-1]
        
"""water area: dp"""
# import math
def water_area(arr,n):
    left=[0]*n
    right=[0]*n
    left[0]=arr[0]
    water=0
    for i in range(1,n):
        left[i]=max(left[i-1],arr[i])
    right[n-1]=arr[n-1]        
    for j in range(n-2,-1,-1):
        right[i]=max(right[i+1],arr[i])
    for i in range(1,n-1):
        water+=min(left[i],right[i])-arr[i]
    return water
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];  
# n = len(arr);
# print (water_area(arr, n))

"""knapsack problem: dp"""
def knapsack(w,val,wt,n):
    sack=[[0 for row in range(0,w+1)] for row in range(n+1)]
    for x in range(w+1):
        sack[0][x]=0
    for i in range(1,n+1):
        for x in range(w+1):
            if x<wt[i-1]:
                sack[i][x]=sack[i-1][x]
            else:
                sack[i][x]=max(sack[i-1][x],sack[i-1][x-wt[i-1]]+val[i-1])
    return sack[n][w]
# val = [10,15,40] 
# wt = [1, 2, 3] 
# w = 5
# n = len(val) 
# print (knapsack(w, val, wt, n))

# """nth stair: dp"""
# def countWays(n):
#     if n==0:
#         return 0
#     dp=[0]*(n+1)
#     dp[1]=1
#     for i in range(1,n+1):
#         dp[i]+=dp[i-1]
#     for i in range(2,n+1):
#         dp[i] +=dp[i-2]        
#     return dp[n]      

# n=4
# print (countWays(n))

"""box stacking :dp"""

def maxHeight(height, width, length, n):
    class box:
        def __init__(self,h,w,l):
            self.h=h
            self.w=w
            self.l=l
        def __lt__(self,other):
            return self.w*self.l<other.w*other.l
    
    arr=[]
    for i in range(n):
        arr.append(box(height[i],width[i],length[i]))
    def maxstack(arr,n):
        rot=[box(0,0,0) for x in range(3*n)]
        index=0
        for i in range(n):
            rot[index].h=arr[i].h
            rot[index].w=min(arr[i].w,arr[i].l)
            rot[index].l=max(arr[i].w,arr[i].l)
            index+=1
            
            rot[index].h=arr[i].w
            rot[index].w=min(arr[i].h,arr[i].l)
            rot[index].l=max(arr[i].h,arr[i].l)
            index+=1
            
            rot[index].h=arr[i].l
            rot[index].w=min(arr[i].h,arr[i].w)
            rot[index].l=max(arr[i].w,arr[i].h)
            index+=1
        rot.sort(reverse=True)
        dp=[0 for i in range(3*n)]
        n=3*n
        for i in range(n):
            dp[i]=rot[i].h
        for i in range(1,n):
            for j in range(0,i):
                if (rot[j].w>rot[i].w and rot[j].l>rot[i].l):
                    if dp[i]<dp[j]+rot[i].h:
                        dp[i]=dp[j]+rot[i].h
        maxi=-1
        for i in range(n):
            maxi=max(maxi,dp[i])
        return maxi
    return maxstack(arr, n)
n = 4
height=[4,1,4,10] 
width=[6,2,5,12] 
length=[7,3,6,32]
print (maxHeight(height, width, length, n))
    
            
# Dynamic Programming implementation 
# of Box Stacking problem 
class Box: 
	
	# Representation of a box 
	def __init__(self, h, w, d): 
		self.h = h 
		self.w = w 
		self.d = d 

	def __lt__(self, other): 
		return self.d * self.w < other.d * other.w 

def maxStackHeight(arr, n): 

	# Create an array of all rotations of 
	# given boxes. For example, for a box {1, 2, 3}, 
	# we consider three instances{{1, 2, 3}, 
	# {2, 1, 3}, {3, 1, 2}} 
	rot = [Box(0, 0, 0) for _ in range(3 * n)] 
	index = 0

	for i in range(n): 

		# Copy the original box 
		rot[index].h = arr[i].h 
		rot[index].d = max(arr[i].d, arr[i].w) 
		rot[index].w = min(arr[i].d, arr[i].w) 
		index += 1

		# First rotation of the box 
		rot[index].h = arr[i].w 
		rot[index].d = max(arr[i].h, arr[i].d) 
		rot[index].w = min(arr[i].h, arr[i].d) 
		index += 1

		# Second rotation of the box 
		rot[index].h = arr[i].d 
		rot[index].d = max(arr[i].h, arr[i].w) 
		rot[index].w = min(arr[i].h, arr[i].w) 
		index += 1

	# Now the number of boxes is 3n 
	n *= 3

	# Sort the array 'rot[]' in non-increasing 
	# order of base area 
	rot.sort(reverse = True) 

	# Uncomment following two lines to print 
	# all rotations 
	# for i in range(n): 
	#	 print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d) 

	# Initialize msh values for all indexes 
	# msh[i] --> Maximum possible Stack Height 
	# with box i on top 
	msh = [0] * n 

	for i in range(n): 
		msh[i] = rot[i].h 

	# Compute optimized msh values 
	# in bottom up manner 
	for i in range(1, n): 
		for j in range(0, i): 
			if (rot[i].w < rot[j].w and
				rot[i].d < rot[j].d): 
				if msh[i] < msh[j] + rot[i].h: 
					msh[i] = msh[j] + rot[i].h 

	maxm = -1
	for i in range(n): 
		maxm = max(maxm, msh[i]) 

	return maxm 

# Driver Code 
# if __name__ == "__main__": 
# 	arr = [Box(4, 6, 7), Box(1, 2, 3), 
# 		Box(4, 5, 6), Box(10, 12, 32)] 
# 	n = len(arr) 
# 	print("The maximum possible height of stack is", 
# 		maxStackHeight(arr, n)) 

# This code is contributed by vibhu4agarwal 

"""spacing in a string"""
# import math
# def wordbreak(string,lis):
#     dic={}
#     for ele in lis:
#         dic[ele]=True
#     mini=math.inf
#     def word(string,dic,mini):
#         if string in dic:
#             return 0
#         else:
#             for i in range(len(string)):
#                 if string[:i+1] in dic:
#                     x=word(string[i+1:], dic,mini) 
#                     mini=min(mini,1+x)
#             return mini
#     t=word(string, dic, mini)
#     if t!=math.inf:
#         return t
#     else:
#         return -1
# string="ab"
# lis=["a","abgaw","bg","ed","w","awed"] 
# print (wordbreak(string, lis))        
import math
def wordbreak(string,lis):
    dic={}
    for ele in lis:
        dic[ele]=True
    mini=math.inf
    def word(string,dic,mini):
        if string in dic:
            # dic[string]=False
            return 0
        else:
            for i in range(len(string)):
                if string[:i+1] in dic:
                    # dic[string[:i+1]]==True
                    x=word(string[i+1:], dic,mini) 
                    mini=min(mini,1+x)
            return mini
    t=word(string, dic, mini)
    if t!=math.inf:
        return t
    else:
        return -1
# string="aw"
# lis=["a","abgaw","bg","ed","w","awed"] 
# print (wordbreak(string, lis))                

"""max profit with k transactions: dp"""
# def maxProfitWithKTransactions(prices, k):
#     n=len(prices)
#     if n==1 and k==0:
#         return 0
#     else:
#         maxp=0
#         max_arr=[]
#         buy=prices[0]
#         i=1
#         while i<len(prices):
#             while prices[i]>prices[i-1]:
#                 maxp=max(maxp,prices[i]-buy)
#                 if i==len(prices)-1:
#                     break
#                 i+=1
#             max_arr.append(maxp)
#             maxp=0
#             buy=prices[i]
#             i+=1
#         max_arr.sort(reverse=True) 
#         # print(max_arr)
#         sum=0
#         for i in range(k):
#             if i==len(max_arr):
#                 break
#             sum+=max_arr[i]
#         return sum
            
# prices=[1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5]

# k=2
# print (maxProfitWithKTransactions(prices, k))

def maxProfitWithKTransactions(prices, k):
    n=len(prices)
    dp=[[0 for i in range(k+1)] for j in range(n)]
    for i in range(1,n):
        for j in range(1,k+1):
            maxnow=0
            for l in range(i):
                maxnow=max(maxnow,prices[i]-prices[l]+dp[l][j-1])
            dp[i][j]=max(maxnow,dp[i-1][j])
    return dp[n-1][k]
# k = 2
# prices = [10, 22, 5, 75, 65, 80] 

# print (maxProfitWithKTransactions(prices, k)) 

                
            
    
# Python program to maximize the profit 
# by doing at most k transactions 
# given stock prices for n days 

# Function to find out maximum profit by 
# buying & selling a share atmost k times 
# given stock price of n days 
def maxProfit(prices, n, k): 
	
	# Bottom-up DP approach 
	profit = [[0 for i in range(k + 1)] 
				for j in range(n)] 
	
	# Profit is zero for the first 
	# day and for zero transactions 
	for i in range(1, n): 
		
		for j in range(1, k + 1): 
			max_so_far = 0
			
			for l in range(i): 
				max_so_far = max(max_so_far, prices[i] -
							prices[l] + profit[l][j - 1]) 
							
			profit[i][j] = max(profit[i - 1][j], max_so_far) 
	
	return profit[n - 1][k] 

# Driver code 
# k = 2
# prices = [10, 22, 5, 75, 65, 80] 
# n = len(prices) 

# print("Maximum profit is:", 
# 	maxProfit(prices, n, k)) 

# This code is contributed by vaibhav29498 
import math
def minpalpart(string,i,j):
    if i==j:
        print (string[i])
        return 0
    elif ispalindrome(string,i,j):
        print (string[i:j+1])
        return 0
    else:
        mini=math.inf
        for k in range(i,j):
            x=minpalpart(string,i,k)
            y=minpalpart(string, k+1, j)
            z=x+1+y
            mini=min(z,mini)
        return mini
            

def ispalindrome(string,l,h):
    # l=0
    # h=len(string)-1
    while l<=h:
        if string[l]==string[h]:
            l+=1
            h-=1
        else:
            return False
    return True
string="geek"
print(minpalpart(string, 0, len(string)-1))
            