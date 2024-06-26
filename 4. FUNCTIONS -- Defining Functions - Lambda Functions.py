#!/usr/bin/env python
# coding: utf-8

# # FUNCTION | LAMBDA FUNCTION

# ## >>>> Function <<<<

# ### Writing Functions

# Functions in Python are defined using the 'def' keyword. A function is a block of reusable code that performs a specific task. 
# 
# Here's the basic syntax for defining a function:

# In[1]:


def function_name(parameters):
    """
    Docstring (optional): Describes the function.
    """
    # Function body
    statement(s)


# In[2]:


# Example 

def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")


# ### Function Parameters and Arguments

# Parameters are the variables listed inside the parentheses in the function definition.
# 
# Arguments are the values passed to the function when it is called.

# In[3]:


def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

result = add(3, 5)  # Here, 3 and 5 are arguments passed to the parameters 'a' and 'b'.
print(result)  # Outputs: 8


# ### Return Values

# A function can return a value using the 'return' statement. If no 'return' statement is specified, the function returns 'None.'

# In[4]:


# Example

def square(x):
    """This function returns the square of a number."""
    return x * x

result = square(4)
print(result)  # Outputs: 16


# ##### Function | Class Work

# In[6]:


# There are 2 types:
    # User-defined : Save code on f(x) function
    # Pre-defined
    

    
# Steps:
    # add ---Parameter (a)
    # Documentation: """__---__"""
    # Body: print, returen
    # add (2)


# In[7]:


def add(a):
    """
    add 1 to a and save it in b
    """
    b = a + 1
    print(a,"If you add 1, it becomes", b)
    return(b)


# In[8]:


add(2)


# In[9]:


help(add)


# In[10]:


def multiplication(a,b):
    c=a*b
    print("Multiplication")
    return(c)       ##If you write 'return()', nothing will be appeared


# In[11]:


multiplication(10,5)


# In[6]:


def MJ():
    print("python")
    
def MJ1():
    print("Python")
    return(None)


# In[7]:


MJ1()


# In[8]:


MJ()


# In[9]:


def MJ2():
    a=1+1
    return(a)


# In[10]:


MJ2()


# In[11]:


print(MJ())          #Call MJ and MJ1


# In[12]:


print(MJ2())


# Create a function that concatenates 2 trings using the addition operation:

# In[13]:


def con(a,b):
    return (a+b)


# In[14]:


con(2,5)


# In[15]:


con("Nisa ","Tehzeeb")


# Functions Make things simple:

# In[16]:


a1 = 4
b1 = 5
c1 = a1 + b1 + 2*a1*b1 - 1

if (c1<0):
    c1 = 0
else:
    c1 = 5
    
c1


# In[17]:


a1 = 0
b1 = 0
c1 = a1 + b1 + 2*a1*b1 - 1

if (c1<0):
    c1 = 0
else:
    c1 = 5
    
c1


# Creating BLOCK Function:

# In[18]:


def Equation(a,b):
    c = a + b + 2*a*b - 1
    
    if (c<0):
        c=0
    else:
        c=5
    return(c)


# In[19]:


Equation(2,2)


# Using if/else Statement and Loops in Functions:

# In[20]:


## if/else in a Function:

def type_of_album(artist, album, year_released):
    print(artist, album, year_released)
    
    if year_released>1980:
        return "Modern"
    else:
        return "Oldie"


# In[21]:


x = type_of_album("Pop", "Thriller", 1970)
print(x)


# In[22]:


## Loop in a Function:


def printlist(the_list):
    for element in the_list:
        print(element)


# In[23]:


printlist(["1", 1, "The man", "abc"])


# Setting default argument values in your custom functions:

# In[24]:


def isGoodRating(rating=4):
    if (rating<7):
        print("This ablum is bad, its rating is",rating)
    else:
        print("This album is good with rating", rating)


# In[25]:


isGoodRating()


# In[26]:


isGoodRating(9)


# ### Scope of Variables | Global & Local Variable

# The scope of a variable determines where in the program a variable can be accessed. Python has two main scopes:
# 
# 
#     Local Scope: Variables defined within a function are in the local scope and can only be accessed within that function.
# 
#     Global Scope: Variables defined outside any function are in the global scope and can be accessed from anywhere in the code.

# In[5]:


# Example 

x = 10  # Global variable

def func():
    x = 5  # Local variable
    print("Local x:", x)

func()  # Outputs: Local x: 5
print("Global x:", x)  # Outputs: Global x: 10


# In[27]:


## Global

artist = "Imrana Yasmin"   #Global Variable: defined outside the functing#

def printer1(artist):
    interval_var = artist  #Local Variable: defined INside the functing#
    print(artist, "is an artist")
    
printer1(artist)           #Global Variables can be used anywhere
#print(interval_var)       #You cannot use internal var to print, Cannot use outside the function#


# In[28]:


artist = "Imrana Yasmin"  

def printer1(artist):
    interval_var = artist 
    
    print("Internal Variable: ", interval_var)
    print(artist, "is an artist")
    
printer1(artist)    


# In[30]:


artist = "Imrana Yasmin"

def printer(artist):
    global internal_var
    internal_var = "Rimi Khan"
    print(artist, "is an artist")

printer(artist)
printer(internal_var)

print(internal_var)


# In[31]:


myfavouriteBrand = "AC/DC"   #Global Variable#

def getBrandRating (brandname):
    if brandname == myfavouriteBrand:
        return 10.0
    else:
        return 0.0
    
print("AC/DC's rating is: ", getBrandRating("AC/DC"))

print("Deep Purple's rating is: ", getBrandRating("Deep Purple"))

print("My favourite Brand is: ", myfavouriteBrand)


# In[32]:


myfavouriteBrand = "AC/DC"   #Local Variable#

def getBrandRating (brandname):
    myfavouriteBrand = "Deep Purple"  #Local Variable#
    
    if brandname == myfavouriteBrand:
        return 10.0
    else:
        return 0.0
    
print("AC/DC's rating is: ", getBrandRating("AC/DC"))

print("Deep Purple's rating is: ", getBrandRating("Deep Purple"))

print("My favourite Brand is: ", myfavouriteBrand)


# ## >>>> Lambda Function <<<<

# Lambda functions are small anonymous functions defined with the 'lambda' keyword. They can have any number of arguments but only one expression.

# In[33]:


add = lambda x, y: x + y
print(add(2, 3))  


# Using Lambda with Built-in Functions:

# In[34]:


# map: Applies a function to all items in an input list.

numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers))

print(squared) 


# In[35]:


# filter: Filters items out of a list.

numbers = [1, 2, 3, 4]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)  


# In[36]:


# reduce: Applies a rolling computation to sequential pairs of values in a list.

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  


# In[ ]:




