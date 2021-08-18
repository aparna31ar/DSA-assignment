#!/usr/bin/env python
# coding: utf-8

# ## Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# ## Using simple for loop

# In[9]:


from array import *
arr=array('i',[8, 7, 2, 5, 3, 1])
n=len(arr)
s=int(input("Enter the sum:"))
for i in range(n):
    for j in range(i+1,n):
        #print(j)
        if arr[i]+arr[j]==s:
            print("Pair found", (arr[i], arr[j]))


# ## Using hash table

# In[6]:


def Pairs(arr, n, sum):
    mydict = dict()                      #to store the count of the numbers in array
    for i in range(n):
        temp = sum - arr[i]               #to serach if any pair is present or not
         
        if temp in mydict:
            count = mydict[temp]
            for j in range(0,count):
                print("(", temp, ", ", arr[i],")", sep = " ", end = '\n')
        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1


# In[7]:


if __name__ == '__main__':
     
    arr = [ 1, 5, 7, -1, 5 ]
    n = len(arr)
    sum = 6
    Pairs(arr, n, sum)


# ## Q2. Write a program to reverse an array in place? 
# ## In place means you cannot create a new array. You have to update the original array.

# In[21]:


from array import *
arr=array('i',[1,2,3,4,5,6])
arr.reverse()
print(*arr)


# ## Q3. Write a program to check if two strings are a rotation of each other?

# In[13]:


def areRotations(s1, s2):
    size1 = len(s1)
    size2 = len(s2)
    temp = ' '
 
    if size1 != size2:
        return 0
    temp = s1 + s1
    print(temp)
 
    if (temp.count(s2)> 0):
        return 1
    else:
        return 0
 


# In[16]:



s1 = "AACD"
s2 = "ACDA"
 
if areRotations(s1, s2):
    print ("Strings are rotations of each other",s2)
else:
    print ("Strings are not rotations of each other")


# ## Q4. Write a program to print the first non-repeated character from a string?

# In[41]:


NO_OF_CHARS = 256

def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 
def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 


# In[46]:


string = "tabcdefghabcdxefghj"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is " + string[index])
 


# ## Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# ### Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. 
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
# 1) Only one disk can be moved at a time. 
# 2) Each move consists of taking the upper disk from one of the stacks 
# and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
# 3) No disk may be placed on top of a smaller disk.
# Note: Transferring the top n-1 disks from source rod to Auxiliary rod can again be thought of as a fresh problem 
#     and can be solved in the same manner.

# In[23]:


def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          


# In[24]:



n = 4
TowerOfHanoi(n,'A','B','C') 


# ## Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# ### Postfix: An expression is called the postfix expression if the operator appears in the expression after the operands. 
# Simply of the form (operand1 operand2 operator). 
# Example : AB+CD-* (Infix : (A+B) * (C-D) )
# 
# ### Prefix : An expression is called the prefix expression if the operator appears in the expression before the operands. 
# Simply of the form (operator operand1 operand2). 
# Example : *+AB-CD (Infix : (A+B) * (C-D) )

# ## Prefix to postfix

# In[14]:


s = "*-A/BC-/AKL"
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]

for i in s:
    if i in operators:
        a = stack.pop()
        b = stack.pop()
        temp = a+b+i
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)


# ## Postfix to prefix

# In[17]:


s = "ABC/-AK/L-*"
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
for i in s:
    if i in operators:
        a = stack.pop()
        b = stack.pop()
        temp = i+b+a
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)


# ## Q7. Write a program to convert prefix expression to infix expression.

# In[19]:


s = "*+A/BC-/ADL"
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]

for i in s:
    if i in operators:
        a = stack.pop()
        b = stack.pop()
        temp = a+i+b
        stack.append(temp)
    else:
        stack.append(i)
print(*stack)


# ## Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[2]:


def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True


# In[3]:


if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
 


# ## Q9. Write a program to reverse a stack.

# In[4]:


class Stack:
    def __init__(self):
        self.Elements = []
        
    def push(self, value):
        self.Elements.append(value)
       
    def pop(self):
        return self.Elements.pop()
     
    def empty(self):
        return self.Elements == []
     
    def show(self):
        for value in reversed(self.Elements):
            print(value)

def BottomInsert(s, value):
    if s.empty():
        s.push(value)
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
        
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
 


# In[5]:


stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[ ]:





# In[ ]:




