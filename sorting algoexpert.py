#sorting algorithms

#___bubble sort__

def bubble_sort(a):
    for i in range (len(a)):
        j=0
        while (a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
            j+=1
            if j==len(a)-1:
                break
    return a
            

# a=[5,4,3,2,-1,0]
# print (bubble_sort(a))

#___selection sort___

def selection_sort(a):
    #mini=a[0]
    for i in range(0,len(a)):
        mini=i
        for j in range(i,len(a)):
            if a[j]<a[i]:
                mini=j
        a[i],a[mini]=a[mini],a[i]
    return a
                
# a=[5,4,3,2,-1,0]
# print (selection_sort(a))  

#__insertion sort__

def insertion_sort(a):
    for i in range(0,len(a)):
        j=i-1
        while (j>=0):
            if a[j]>a[i]:
                a[j],a[i]=a[i],a[j]
            else:
                break
            i=j
            j-=1
        #print (a)
    return a
#a=[5,4,3,2,-1,0]
#print (insertion_sort(a))

#___merge sort_

def merge_sort(a):
    def merge(left,right):
    
        result=[]
        i=0
        j=0
        while i<len(left) and j<len(right):
        
            if left[i] <right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i==len(left):
            result= result+right[j:]
        if j==len(right):
            result+=(left[i:])
            
        return result

    
    
    if len(a)<2:
        return a[:]
    else:
        mid=len(a)//2
        left=merge_sort(a[:mid])
        right=merge_sort(a[mid:])
        return merge(left,right)
            
# a=[5,4,3,2,-1,0,5]  
# print (merge_sort(a))  
      
    

# a=[3,8,2,5,1,4,7,6]
# # print (partition(a))   
    
# def quick_sort(a,l,n):
#     def partition(a,pivot,n):
#     #n=len(a)
#     #pivot=a[0]
#         i=0
#         j=1
#         while j<=n :
#         #print (a)
        
#             if a[j]<=pivot:
#                 a[j],a[i+1]=a[i+1],a[j]
#                 j+=1
#                 i+=1            
#             elif a[j]>pivot:
#                 j+=1
#         a[i],a[0]=a[0],a[i]
#         return (a,i)
#     if len(a)==1:
#         return
#     else:
#         pivot=a[l]
#         x,y=partition(a,pivot,n)
#         quick_sort(a,0,y)
#         quick_sort(a, y, len(a)-1)
        
        
# print (quick_sort(a,0,len(a)-1))
    
def partition(a,l,h):
    
    #n=len(a)
    #pivot=a[0]
    pivot =a[l]
    i=l+1
    j=l+h
    for j in range(l+1,h+1):
        #print (pivot)
        #print (j)
        if a[j]<pivot:
            
            a[j],a[i]=a[i],a[j]
            i+=1
            #print (i)
    
    #return
    a[l],a[i-1]=a[i-1],a[l]
    return (i-1)

# a=[3,8,2,5,1,4,7,6]      
# h=partition(a,0,7) 
# print (h)
# print (a)
# x=partition(a,h+1,7)
# print (x)
# print(a)

def quick_sort(a,l,h):
    if l>=h:
        return 
    else:
        x=partition(a,l,h)
        quick_sort(a,l,x)
        quick_sort(a,x+1,h)
        return
# a=[3,3,3,2,5,1,4,7,6]
# quick_sort(a, 0, len(a)-1) 
# print (a)    

#__heap sort__


def heapify(a,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and a[left]>a[largest]:
        largest=left
    if right<n and a[right]>a[largest]:
        largest=right
    if largest !=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a, n, largest)
    

def buildmaxHeap(arr, n): 
  
    # Index of last non-leaf node 
    startIdx = n // 2 - 1
  
    # Perform reverse level order traversal 
    # from last non-leaf node and heapify 
    # each node 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)        
# a=[ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17 ]
# #a=[a.append(ele) for ele in reversed(a)]
# buildmaxHeap(a, len(a)) 
# print (a)     
        
# a=[8,7,6,5,4,3,2,1,0]  
# for x in range (len(a)//2,-1,-1):
#     heapify(a, len(a), x)
# print(a)     
# def heap_sort(a):
#     if len(a)==0:
#         return
#     for x in range (len(a)//2,-1,-1):
#         heapify(a, len(a), x)
    
#     result.append(a[0])
#     a[0],a[len(a)-1]=a[len(a)-1],a[0]
#     del(a[len(a)-1])
    
#     heapify(a, len(a), 0)
#     heap_sort(a)
# result=[]
# heap_sort(a)
# print (result)

def heapify(a,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and a[left]<a[largest]:
        largest=left
    if right<n and a[right]<a[largest]:
        largest=right
    if largest !=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a, n, largest)
        
def buildminHeap(arr, n): 
  
    # Index of last non-leaf node 
    startIdx = n // 2 - 1
  
    # Perform reverse level order traversal 
    # from last non-leaf node and heapify 
    # each node 
    for i in range(startIdx, -1, -1): 
        heapify(arr, n, i)       
        
a=[17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1] 
n=len(a)
buildminHeap(a, n)    
    
print (a)
def heap_sort(a):
    if len(a)==0:
        return
    
    
    result.append(a[0])
    a[0],a[len(a)-1]=a[len(a)-1],a[0]
    del(a[len(a)-1])
    
    heapify(a, len(a), 0)
    heap_sort(a)
result=[]
heap_sort(a)
print (result)

