# # # -*- coding: utf-8 -*-
# # """
# # Created on Wed Aug 12 13:10:21 2020

# # @author: mourya
# # stack implementations on algoexpert
# # """
# # # class stack:
# # #     def __init__(self,maxsize=0):
        
# # #         if maxsize<0:
# # #             return "stack not possible"
# # #         else:
# # #             self.maxsize=maxsize
# # #             self.stac=[0]*maxsize
# # #             self.size=0
            
            
# # #     def push(self,num):
# # #         # if self.size>=self.maxsize:
# # #         #     raise "overflowError"
# # #         #     return
# # #         # else:
# # #         #     current=self.size
# # #         #     self.stac[current]=num
# # #         #     self.size+=1
# # #         try:
# # #             if self.size<self.maxsize:
# # #                 current=self.size
# # #                 self.stac[current]=num
# # #                 self.size+=1
# # #             else:
# # #                 print ("stackoverflow")
# # #         except:
# # #             print(None)
            
# # #             # raise "maxsize reached"
                
# # #     def peek(self):
# # #         return self.stack[self.size-1]
# # #     def pop(self):
# # #         val=self.stac[self.size-1]
# # #         self.size-=1
# # #         return val
# # #     def isempty(self):
# # #         if self.size==0:
# # #             return "True"
# # #     def get_stack(self):
# # #         return self.stac[:self.size]
# # #     def get_size(self):
# # #         return self.size
# # #     def __iter__(self):
# # #         self.start=0
# # #         return self
# # #     def __next__(self):
        
        
# # #         while self.start<(self.size):
# # #             temp=self.start
# # #             self.start+=1
            
# # #             return self.stac[temp]
        
# # #         raise StopIteration
            
# # # st=stack(5)
# # # st.push(2)
# # # st.push(3)  
# # # st.push(10)
# # # st.push(10)
# # # st.push(10)
# # # st.push(10)
# # # st.push(10)
# # # print (st.get_stack())
# # # print (st.get_size())  
# # # print (st.pop())       
# # # print (st.get_size())
# # # print (st.get_stack()) 
# # # for ele in st:
# # #     print (ele)
        
# # """min max stack"""
# # class stackNode:
# #     def __init__(self,num,mini,maxi):
# #         self.num=num
# #         self.mini=mini
# #         self.maxi=maxi
# # class minmaxstack:
# #     def __init__(self,maxsize=0):        
# #         if maxsize<0:
# #             print ("stack not possible")
# #             return
# #         else:
# #             self.maxsize=maxsize
# #             self.stac=[0]*maxsize
# #             self.size=0
# #             self.minimum=None
# #             self.maximum=None
# #     def push(self,num):
# #         try:
# #             if self.size==0:
# #                 current=self.size
# #                 self.minimum=num
# #                 self.maximum=num
# #                 self.stac[current]=stackNode(num,self.minimum,self.maximum)
# #                 self.size+=1
# #             elif self.size<self.maxsize:
# #                 current=self.size
# #                 if self.minimum>num:
# #                     self.minimum=num
# #                 if self.maximum<num:
# #                     self.maximum=num
# #                 self.stac[current]=stackNode(num,self.minimum,self.maximum)
# #                 self.size+=1
# #             else:
# #                 print ("stackoverflow")
# #         except:
# #             print(None)
# #     def peek(self):
# #          return self.stack[self.size-1].num
# #     def pop(self):
# #         val=self.stac[self.size-1]
# #         self.size-=1
# #         return val.num
# #     def isempty(self):
# #         if self.size==0:
# #             return "True"
# #     def get_min(self):
# #         return self.stac[self.size-1].mini
# #     def get_max(self):
# #         return self.stac[self.size-1].maxi
# #     def get_stack(self):
# #         return self.stac[:self.size]
# #     def get_size(self):
# #         return self.size
# # st=minmaxstack(5)
# # st.push(2)
# # st.push(3)  
# # st.push(10)
# # st.push(10)
# # st.push(13)
# # st.push(1)
# # st.pop()
# # print(st.get_max())
# # print(st.get_min())
# # # st.push(10)

# """balanced parenthesis"""
# def isbalencedParenthesis(exp):
#     stack=[]
#     def isempty(stack):
#         if len(stack)==0:
#             return True
#         return False
#     express=list(exp)
#     for char in express:
#         if isempty(stack):
#             if char in ['(','[','{']:
#                 stack.append(char)
#             else:
#                 return False
#         else:
#             if stack[-1]=='(':
#                 if char!=')':
#                     return False
#                 del(stack[-1])
#             elif stack[-1]=='[':
#                 if char in [')','{','}']:
#                     return False
#                 elif char==']':
#                     del(stack[-1])
#                 else:
#                     stack.append(char)
#             elif stack[-1]=='{':
#                 if char in [')',']']:
#                     return False
#                 elif char=='}':
#                     del(stack[-1])
#                 else:
#                     stack.append(char)
#     if isempty(stack):
#         return True
#     else:
#         return False
# print(isbalencedParenthesis("[()]{}{[()()]()}"))         

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
    
def shorten_path(exp):
    express=exp.split('/')
    st=stack()
    for char in express:
        if st.get_size()==0:
            st.push(char)
        else:
            current=st.peek()
            if current=='':
                if char not in ['.','..','']:
                    st.push(char)
            else:
                if char=='..':
                    if st.get_size()>1:
                        st.pop()
                elif char not in ['.','..','']:
                    st.push(char)
    if st.get_size()==1:
        return '/'
    return '/'.join(st.get_stack())

a='/a/./b/./c/./d/'
print (shorten_path(a))
                
                
                
        
