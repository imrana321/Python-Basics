#!/usr/bin/env python
# coding: utf-8

# # Python Data Structure

# A data structure is a way of organizing, managing, and storing data in a computer so that it can be accessed and modified efficiently. In Python, data structures are used to store a collection of related data. They help in performing operations such as insertion, deletion, searching, and sorting of data effectively. Python provides several built-in data structures, each with its unique characteristics and usage scenarios.

# #### Built-in Python Data Structures:

# #### Lists || .................................. fruits = ['apple', 'banana', 'cherry']
# 
#     Description: Ordered collections of items. They are mutable, meaning you can change their contents.
#     Usage: Suitable for ordered data, maintaining a sequence, or when you need to access elements by index.
# 
# #### Tuples || ............................... coordinates = (10.0, 20.0)
#     Description: Ordered collections of items. They are immutable, meaning once created, their contents cannot be changed.
#     Usage: Useful for fixed collections of items that should not be modified, such as coordinates or configuration settings.
#     
# #### Dictionaries || ..................... student = {'name': 'Alice', 'age': 25, 'grade': 'A'}
#     Description: Unordered collections of key-value pairs. They are mutable and can store a dynamic number of values.
#     Usage: Ideal for associative arrays or mappings, where you need to store data that can be looked up by unique keys.
#     
# #### Sets || .................................. unique_numbers = {1, 2, 3, 4}
#     Description: Unordered collections of unique items. They are mutable and automatically eliminate duplicate elements.
#     Usage: Perfect for membership tests, removing duplicates from a sequence, and mathematical operations like union, intersection, and difference.

# ## >>>> Data Structure | LIST <<<<

# Lists are ordered sequence | Square Brackets | Mutable

# In a LIST, various structured/types elements can be put : String, Float, List, Tuple

# #### LIST | Indexing

# In[4]:


L=["Michael Jackson", 10.1, 1982]

L


# In[5]:


['Michael Jackson', 10.1, 1982]


print("The same element using negative and positive INDEXING:\n Positive: ", L[0],"\n Negative: ", L[-3])


# #### LIST | Contents

# In[6]:


### A Lists can contain: String, float, int, nested-tuple, nested-list


["python", 10.1, 1986, [1,2], ("A", 1)]


# #### LIST | Operations

# In[7]:


L=["Michael Jackson", 10.1, 1982, "MJ", 1]

L[3:5]


# #### LIST | Mutable

# In[10]:


### 'extend' - adds 2 separate elements to a LIST.

L=["Michael Jackson", 10.2]

L.extend(["pop", 10])     

L


# In[11]:


### 'append' - adds one nested element/list to a LIST.

L=["Michael Jackson", 10.2]

L.append(["pop", 10])           

L


# In[12]:


### The elements can be chnaged 

A = ["disco", 10, 1.2]
print("Before Change: ", A)

A[2]= "Python"
print("After Change: ", A)


# In[13]:


### The elements can be deleted

A = ["disco", 10, 1.2]
print("Before Change: ", A)

del(A[2])
print("After Change: ", A)


# #### LIST | String to List

# In[14]:


### split : using delimiter. Usually split() takes 'space' by default

"Hard Rock".split()


# In[15]:


### Use delimiter otherwise:
### Back Slash '\' doesn't work as delimiter - 

"A/B/C/D".split("/")


# #### LIST | Copy & Clone

# In[16]:


## Copy -- Changing one list will make the other one changed:

A = ["lolly", 10, 2.5]

B = A


# In[17]:


B


# In[18]:


B[1] = "Nisa"

B


# In[19]:


A


# In[20]:


## Copy -- Changing one list will NOT make the other one changed:

C = ["Urmi", "Rimi", "NIsa", "Runa"]
D = C[:]

D


# In[21]:


D[2] = "Nisa Moni"

D


# In[22]:


C


# ## >>>> Data Structure | TUPLE <<<<

# Tuple will be within parenthesis | elements will be seprated by "," commas | Immutable

# In[23]:


## In a TUPLE various structured/types elements can be put : String, Float, List, Tuple

Tuple1 = ("Table", 10, 2.1)

Tuple1


# In[24]:


type(Tuple1)


# #### TUPLE | Indexes

# In[26]:


Tuple1[0]


# In[27]:


Tuple1[2]


# In[28]:


# Negative Indexing

Tuple1[-3]


# #### TUPLE | Concatenate

# In[29]:


## We can concatenate or combine tuples by using "+" sign:


Tuple2 = ("chair" , 10)

Tuple = Tuple1 + Tuple2

Tuple


# #### TUPLE | Slicing

# In[30]:


## Each of the element is index no matter the element type

Trial =("Table" , 5, 2.23, "Chair", 63) 


# In[31]:


Trial [0:3]


# In[32]:


Trial[3:5]


# In[33]:


len(Trial)


# #### TUPLE | Sorting

# In[35]:


## We can sort the values in a tuple and save it to a new tuple using the code: sorted()
## Sorting cannpt be done for multiple data types


Ratings = (0, 9, 5, 6, 1, 10, 8, 2, 1)

RatingsSorted = sorted(Ratings)

RatingsSorted


# In[36]:


Ratings = (0, 9, 5, 6, 1, 10, 8, 2, 1)

RatingsSortedD = sorted(Ratings, reverse=True)

RatingsSortedD


# #### TUPLE | Immutable

# In[38]:


## A tuple's variables are immutable.
# It cannot be written as -- trial[0]=10

Ratings = (0, 9, 5, 6, 1, 10, 8, 2, 1)
Ratings[0]=10                             # Error will Occur


# #### TUPLE | Nested Tuple

# In[39]:


## Tuples (Nesting): Tuples inside a Tuple..
## A tuple can contain another tuple as well as other more complex data types. 


NestedT = (7, 9, ("table", "wall"), (1.1, 4), ("chair", (2,3)))


# In[40]:


print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# In[41]:


print("Element 4, 0 of the Tuple: ", NestedT[4][1][0])


# ## >>>> Data Structure | DICTIONARIES <<<<

# We can delete any key from a Dictionary | Keys are immutable but values are not. So, tuples can be used as a key.

# In[42]:


### Create Dictionary

dict_example = {"key1" : 1, 
                "movie" : "2",
                "key3" : [3,3,4],
               "example": (4,4,4), 
                ("key5"):5,
               (7,8):5,
               "example": (4,4,4),
               "table": 1}    ## Keys cannot be repeated. However, values can be repeated 

dict_example


# In[43]:


# The keys can be String

dict_example["key1"]


# In[44]:


dict_example["movie"]


# In[45]:


# Keys can be immutable like tuple.

dict_example[(7,8)]


# In[46]:


release_year_dict = {"Thriller": 1982,
                    "Back in Black": 1973,
                    "The Bodyguard": 1992,
                    "Bat Out of Hell": 1977,
                    "Their Greatest": 1980}
release_year_dict


# In[47]:


release_year_dict["Thriller"]


# In[48]:


release_year_dict.keys()


# In[49]:


release_year_dict.values()


# In[50]:


# add value to the dictionary

release_year_dict["Graduation"]="2007"
release_year_dict

release_year_dict["Python"]="2023"
release_year_dict


# In[51]:


# Delete element

del(release_year_dict["Python"])

release_year_dict


# In[52]:


release_year_dict["Graduation"]="2007"
release_year_dict


# In[53]:


"The Bodyguard" in release_year_dict


# In[54]:


"Programming" in release_year_dict


# ## >>>> Data Structure | SETS <<<<

# Do NOT records element's POSITIONs | Orderless | No Parenthesis | Curly Brackets | Use unique elements

# #### SETS | Content

# In[55]:


set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "dosco"}

set1


# #### SETS | Set From List

# In[72]:


album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19",              "Pop, Rock, R&B", 46.6, "3-Jan-86", None, 10.0]

album_list=set(album_list)

album_list


# In[57]:


### It can be written diractly with 'set'


album_list = set(["Michael Jackson", "Thriller", 1982, "00:42:19",              "Pop, Rock, R&B", 46.6, "3-Jan-86", None, 10.0])

album_list 


# #### SETS | Operations

# In[60]:


# Add elements to set:

A = set (["Thriller", "Black in back", "AC/DC"])   

A.add("Python")

A


# In[61]:


# Remove element from set:

A.remove("Thriller")

A


# In[62]:


# You cannot add a same element if it is already there:
    
A.add("AC/DC")

A


# In[63]:


A.add("AC/DC _")

A


# In[64]:


# Check if an element is there:

"Python" in A


# In[65]:


"Urmi" in A


# #### SETS | LOGIC Operations

# In[66]:


album_set1 = set(["Thriller", "Black in back", "AC/DC"])
album_set2 = set(["Thriller", "Black in back", "The dark Night"])

album_set1, album_set2


# In[68]:


# Intersection between 2 sets:

intersection = album_set1.intersection(album_set2)

intersection


# In[ ]:


intersection = album_set1 & album_set2

intersection


# In[69]:


# Find out the differences:

album_set1.difference(album_set2)


# In[70]:


album_set2 - (album_set1)


# In[71]:


# UNION:

album_set1.union(album_set2)


# In[ ]:




