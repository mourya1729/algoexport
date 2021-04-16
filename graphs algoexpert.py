# # -*- coding: utf-8 -*-
# """
# Created on Sat Sep  5 17:33:50 2020

# @author: mourya
# """
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Graph:
#     def __init__(self,vertices):
#         self.V=vertices
#         self.graph_list=[None]*self.V
#         self.size=0
#     def insertAtEnd(self,node,v):
#         curr=node
#         while curr:            
#             if curr.data==v:
#                 break
#             elif curr.next is None:
#                 curr.next=Node(v)
#                 break
#             curr=curr.next
            
#     def add_edge(self,u,v):
#         if self.size>self.V:
#             return "overflow"
#         a=None
#         b=None
#         for i in range(self.size):
#             if self.graph_list[i].data==u:
#                 a=i
#             if self.graph_list[i].data==v:
#                 b=i
#         if a is None and b is None:
#             x=Node(u)
#             y=Node(v)
#             if self.size>self.V:
#                 return "overflow"
#             self.graph_list[self.size]=x
#             self.insertAtEnd(x, v)
#             self.size+=1
#             if self.size>self.V:
#                 return "overflow"
#             self.graph_list[self.size]=y
#             self.insertAtEnd(y, u)
#             self.size+=1
#         elif a is None:
#             x=Node(u)
#             self.insertAtEnd(self.graph_list[b], u)
#             self.graph_list[self.size]=x
#             self.size+=1
#             self.insertAtEnd(x, v)
#         elif b is None:
#             y=Node(v)
#             self.insertAtEnd(self.graph_list[a], v)
#             self.graph_list[self.size]=y
#             self.size+=1
#             self.insertAtEnd(y, u)
#         else:
#             self.insertAtEnd(self.graph_list[a], v)
#             self.insertAtEnd(self.graph_list[b], u)
#     def print_graph(self):
#         for i in range(self.V):
#             print ("adjacency list of vertex {}\n ".format(i),end=" ")
#             temp=self.graph_list[i]
#             while temp:
#                 print("-> {}".format(temp.data),end=" ")
#                 temp=temp.next
#             print("\n")
# # if __name__ == "__main__": 
# # 	V = 5
# # 	graph = Graph(V) 
# # 	graph.add_edge(10, 11) 
# # 	graph.add_edge(10,14) 
# # 	graph.add_edge(11,12) 
# # 	graph.add_edge(11,13) 
# # 	graph.add_edge(11,14) 
# # 	graph.add_edge(12,13) 
# # 	graph.add_edge(13,14) 

# # 	graph.print_graph() 
            
"""directed graph"""                        
from collections import defaultdict           
class graph:
    def __init__(self):
        self.graph_dict=defaultdict(list)
    def addEdge(self,u,v):
        self.graph_dict[u].append(v)
        # self.graph_dict[v].append(u)
    def is_edge(self,u,v):
        if v in self.graph_dict:
            return True
        return False
    def is_vertex(self,v):
        if v in self.graph_dict:
            return True
        return False
    def print_graph(self):
        for key in self.graph_dict:
            print ("{} -> ".format(key),end=" ")
            for i in range(len(self.graph_dict[key])):
                # print ("{} -> {}".format(key,self.graph_dict[key][i]),end=" ")
                print ("{}".format(self.graph_dict[key][i]),end=" ")
                
            print("\n")
    def dfs(self,v):
        # visited=[False]*(max(self.graph_dict)+1)
        visited={}
        # print(visited)
        return self.dfsutil(v,visited)
    def dfsutil(self,v,visited):
        visited[v]=True
        print (v,end=" ")
        for i in self.graph_dict[v]:
            if i not in visited:
            # if visited[i] is False:
                self.dfsutil(i,visited)
"""dfs search"""
def dfs(graph,v):
    # print (max(graph.graph_dict))
    visited=[False]*(max(graph.graph_dict)+1)
        # print(visited)
    return dfsutil(graph,v,visited)
def dfsutil(graph,v,visited):
    
    visited[v]=True
    print (v,end=" ")
    for i in graph.graph_dict[v]:
        if visited[i] is False:
            dfsutil(graph,i,visited)
g = graph() 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0) 
g.addEdge(4, 1) 
g.addEdge(2, 3) 
g.addEdge(3, 1) 
print (g.graph_dict)
g.dfs(5)

class queue:
    def __init__(self,n):
        self.maxsize=n
        self.a=[None]*n
        self.front=0
        self.rear=0
        self.size=0
    def insert(self,num):
        if self.size==self.maxsize:
            print ( "overflow")
            return            
        if self.size<self.maxsize:
            self.a[self.rear]=num
            self.rear=(self.rear+1)%self.maxsize
            self.size+=1
    def delete(self):
        num=self.a[self.front]
        self.a[self.front]=None
        self.front=(self.front+1)%self.maxsize
        self.size-=1
        return num
    def prints(self):
        i=self.front
        count=0
        while count<self.size:
            print (self.a[i])
            i=(i+1)%self.maxsize
            count+=1
    def get_size(self):
        return self.size
    


def bfs(graph,v):
    visited={v:True}
    q=queue(10)
    q.insert(v)
    while q.get_size()>0:
        u=q.delete()
        print(u,end=" ")
        for w in graph.graph_dict[u]:
            if w not in visited:
                visited[w]=True
                q.insert(w)
    
"""detect cycle"""
def detect_cycle(graph,v):
    visited=[False]*(max(graph.graph_dict)+1)
    if detect(graph,v,visited,-1) is True:
        return "cycle detected"
    else:
        return "cycle not detected"
def detect(graph,v,visited,parent):
    visited[v]=True
    for i in graph.graph_dict[v]:
        if visited[i]!= True:
            return detect(graph, i, visited, v)
        else:
            if i!=parent and i!=v:
                return True
    return False
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
"""lowest common ancestor"""
def lowcomancestor(g,a,b):
    new_graph=graph()
    def reverse_graph(g):            
        a=g.graph_dict
        for x in a:
            for i in a[x]:
                new_graph.graph_dict[i].append(x)
    reverse_graph(g)    
    def dfs(graph,v):
        lis=[]
        visited=[False]*(max(graph.graph_dict)+1)        
        def dfsutil(graph,v,visited):    
            visited[v]=True
            lis.append(v)
            for i in graph.graph_dict[v]:
                if visited[i] is False:
                    dfsutil(graph,i,visited)
        dfsutil(graph,v,visited)
        return lis
    a_list=dfs(new_graph, a)
    b_list=dfs(new_graph, b)
    for ele in a_list:
        if ele in b_list:
            return ele
    return -1

"""river sizes"""
def riverSizes(matrix,m,n):
    visited=[[False for value in row] for row in matrix]
    # visited=[[False]*n]*m
    size=[]
    for i in range(m):
        for j in range(n):
            if visited[i][j]==True:
                continue
            sizes(i,j,visited,matrix,size,m,n)
    return size
def nodesadjacent(i,j,matrix,visited,m,n):
    unvisitedneighbours=[]
    if i>0 and not visited[i-1][j]:
        unvisitedneighbours.append([i-1,j])
    if i<m-1 and not visited[i+1][j]:
        unvisitedneighbours.append([i+1,j])
    if j<n-1 and not visited[i][j+1]:
        unvisitedneighbours.append([i,j+1])
    if j>0 and not visited[i][j-1]:
        unvisitedneighbours.append([i,j-1])
    return unvisitedneighbours
    
def sizes(x,y,visited,matrix,size,m,n):
    currriversize=0
    nodestoexplore=[[x,y]]
    while True:
        if len(nodestoexplore)==0:
            break
        current=nodestoexplore.pop()
        i=current[0]
        j=current[1]
        # if visited[i][j]:
        #     continue
        visited[i][j]=True
        if matrix[i][j]==0:
            continue
        currriversize+=1
        unvisited=nodesadjacent(i, j, matrix, visited, m, n)
        for neighbour in unvisited:
            nodestoexplore.append(neighbour)
        if len(nodestoexplore)==0:
            break
    if currriversize>0:
        size.append(currriversize)
        
matrix=[
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]  
# print (riverSizes(matrix, len(matrix), len(matrix[0])))      

# g = graph() 
# g.addEdge(3,5)
# g.addEdge(3,1)
# g.addEdge(5,6)
# g.addEdge(5,2)
# g.addEdge(2,7)
# g.addEdge(2,4)
# g.addEdge(1,8)
# g.addEdge(1,0)

# print (lowcomancestor(g,7,8))
"""boggle board"""
def isword(string,dic):
    if string in dic:
        
        return True
    return False

def findboggleutil(matrix,visited,dic,m,n,i,j,string):
    visited[i][j]=True
    string=string+matrix[i][j]
    print (string)
    # if isword(string,dic):
        # print (string)
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (x>=0 and x<m):
                if y>=0 and y<m:
                    
                    if not visited[x][y]:
                        print (matrix[x][y],end=" ")
                        findboggleutil(matrix, visited, dic, m, n, x, y, string)
    
    # string=""+string[len(string)-1]
    # print ("new string "+string)
    visited[i][j]=False
def findboggle(matrix,m,n,dic):
    visited=[[False for value in row] for row in matrix]
    string=""
    for i in range(m):
        for j in range(n):
            findboggleutil(matrix,visited,dic,m,n,i,j,string)        
matrix=[['G', 'I'],['U', 'E']]
dic=["GEEKS", "FOR", "QUIZ", "GIU", "EE"]    
m=len(matrix)
n=len(matrix[0])
findboggle(matrix, m, n, dic)