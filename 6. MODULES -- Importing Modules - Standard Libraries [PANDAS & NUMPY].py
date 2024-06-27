#!/usr/bin/env python
# coding: utf-8

# <h1>Introduction to Pandas Python</h1>

# <p><strong>Welcome!</strong> This notebook will teach you about using <code>Pandas</code> in the Python Programming Language. By the end of this lab, you'll know how to use <code>Pandas</code> package to view and access data.</p>

# <h2 id="dataset">About the Dataset</h2>

# The table has one row for each album and several columns:
# 
# - **artist**: Name of the artist
# - **album**: Name of the album
# - **released_year**: Year the album was released
# - **length_min_sec**: Length of the album (hours, minutes, seconds)
# - **genre**: Genre of the album
# - **music_recording_sales_millions**: Music recording sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **claimed_sales_millions**: Album's claimed sales (millions in USD) on [SONG://DATABASE](http://www.song-database.com/)
# - **date_released**: Date on which the album was released
# - **soundtrack**: Indicates if the album is the movie soundtrack (Y) or (N)
# - **rating_of_friends**: Indicates the rating from your friends from 1 to 10
# 
# You can see the dataset here:
# 
# | Artist           | Album                          | Released | Length   | Genre                          | Music recording sales (millions) | Claimed sales (millions) | Released    | Soundtrack | Rating (friends) |
# |------------------|--------------------------------|----------|----------|--------------------------------|----------------------------------|--------------------------|-------------|------------|------------------|
# | Michael Jackson  | Thriller                       | 1982     | 00:42:19 | Pop, rock, R&B                 | 46                               | 65                       | 30-Nov-82   |            | 10.0             |
# | AC/DC            | Back in Black                  | 1980     | 00:42:11 | Hard rock                      | 26.1                             | 50                       | 25-Jul-80   |            | 8.5              |
# | Pink Floyd       | The Dark Side of the Moon      | 1973     | 00:42:49 | Progressive rock               | 24.2                             | 45                       | 01-Mar-73   |            | 9.5              |
# | Whitney Houston  | The Bodyguard                  | 1992     | 00:57:44 | Soundtrack/R&B, soul, pop      | 26.1                             | 50                       | 25-Jul-80   | Y          | 7.0              |
# | Meat Loaf        | Bat Out of Hell                | 1977     | 00:46:33 | Hard rock, progressive rock     | 20.6                             | 43                       | 21-Oct-77   |            | 7.0              |
# | Eagles           | Their Greatest Hits (1971-1975)| 1976     | 00:43:08 | Rock, soft rock, folk rock     | 32.2                             | 42                       | 17-Feb-76   |            | 9.5              |
# | Bee Gees         | Saturday Night Fever           | 1977     | 1:15:54  | Disco                          | 20.6                             | 40                       | 15-Nov-77   | Y          | 9.0              |
# | Fleetwood Mac    | Rumours                        | 1977     | 00:40:01 | Soft rock                      | 27.9                             | 40                       | 04-Feb-77   |            | 9.5              |
# 

# <h2 id="pandas">Introduction of <code>Pandas</code></h2>

# In[3]:


# Dependency needed to install file 

get_ipython().system('pip install xlrd')


# In[4]:


pip install pandas


# In[5]:


# Import required library

import pandas as pd


# After the import command, we now have access to a large number of pre-built classes and functions. This assumes the library is installed; in our lab environment all the necessary libraries are installed. One way pandas allows you to work with data is a dataframe. Let's go through the process to go from a comma separated values (<b>.csv</b>) file to a dataframe. This variable <code>csv_path</code> stores the path of the <b>.csv</b>, that is  used as an argument to the <code>read_csv</code> function. The result is stored in the object <code>df</code>, this is a common short form used for a variable referring to a Pandas dataframe. 

# In[7]:


# Read data from CSV file

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# We can use the method <code>head()</code> to examine the first five rows of a dataframe: 

# In[9]:


# Print first five rows of the dataframe

df.head()


# We use the path of the excel file and the function <code>read_excel</code>. The result is a data frame as before:

# In[10]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)

df.head()


# We can access the column <b>Length</b> and assign it a new dataframe <b>x</b>:

# In[11]:


# Access to the column Length

x = df[['Length']]

x


#  The process is shown in the figure: 

# <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Images/DataEgOne.png" width="750" />

# <h2 id="data">Viewing Data and Accessing Data</h2>

# You can also get a column as a series. You can think of a Pandas series as a 1-D dataframe. Just use one bracket: 

# In[12]:


# Get the column as a series

x = df['Length']

x


# You can also get a column as a dataframe. For example, we can assign the column <b>Artist</b>:

# In[13]:


# Get the column as a dataframe

x = type(df[['Artist']])

x


# You can do the same thing for multiple columns; we just put the dataframe name, in this case, <code>df</code>, and the name of the multiple column headers enclosed in double brackets. The result is a new dataframe comprised of the specified columns:

# In[14]:


# Access to multiple columns

y = df[['Artist','Length','Genre']]

y


# The process is shown in the figure:

# <img src = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Images/DataEgTwo.png" width="1100" />

# One way to access unique elements is the <code>iloc</code> method, where you can access the 1st row and the 1st column as follows:

# In[16]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# You can access the 2nd row and the 1st column as follows:

# In[17]:


# Access the value on the second row and the first column

df.iloc[1,0]


# You can access the 1st row and the 3rd column as follows: 

# In[18]:


# Access the value on the first row and the third column

df.iloc[0,2]


# You can access the column using the name as well, the following are the same as above: 

# In[19]:


# Access the column using the name

df.loc[0, 'Artist']


# In[20]:


# Access the column using the name

df.loc[1, 'Artist']


# In[21]:


# Access the column using the name

df.loc[0, 'Released']


# In[22]:


# Access the column using the name

df.loc[1, 'Released']


# In[23]:


# Slicing the dataframe

df.iloc[0:2, 0:3]


# In[24]:


# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']


# #### More Excercise:

# Use a variable <code>q</code> to store the column <b>Rating</b> as a dataframe:

# In[25]:


q = df[['Rating']]

q


# Assign the variable <code>q</code> to the dataframe that is made up of the column <b>Released</b> and <b>Artist</b>:

# In[26]:


q = df[['Released', 'Artist']]

q


# Access the 2nd row and the 3rd column of <code>df</code>:

# In[27]:


df.iloc[1, 2]


# In[2]:


import pandas as pd


# In[3]:


excel_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(excel_path)


# In[4]:


df.head()


# In[5]:


#Column Length of the Dataframe#


x = df["Artist"]

x


# In[6]:


#Storing a copy of coulm in 'x'# Create a new data frame into 'x' 

x = df[["Artist"]]

type(x)


# In[7]:


x


# In[8]:


df.head()


# In[9]:


y = df["Artist"]

type(y)


# In[11]:


## Create sub-coulumns ##

y = df[["Artist", "Length", "Genre"]]

y


# ## INDEXES: iloc | loc 

# In[12]:


df.iloc[0,0]


# In[13]:


df.iloc[1,0]     ## Row:Column ##


# In[14]:


df.iloc[0,2]                 # iloc = Only 'indexes' #  'i : Index'


# In[15]:


df.loc[0,"Artist"]            # loc = Either the Index or the 'name' of the column #


# In[16]:


df.loc[0,"Released"] 


# In[17]:


df.iloc[1,0]


# In[19]:


# INDEXES | Slicing


df.iloc[0:2,0:3]


# In[20]:


#loc: we don't consider +1. They are asssuming the 'indexes' as names in the form of numbers.

df.loc[0:3,"Artist":"Released"]    


# In[21]:


with open("Example2.txt", "w") as writefile:
    writefile.write("This is line A")


# In[22]:


with open("Example2.txt", "r") as test_writefile:
    print(test_writefile.read())        ##Revise##


# In[23]:


with open("Example2.txt", "w") as writefile:
     writefile.write("This is line A\n")
     writefile.write("This is line B\n")


# In[24]:


with open("Example2.txt", "r") as test_writefile:
    print(test_writefile.read())


# ## >>>> NUMPY :: Array <<<<

# ### NUMPY | 1D

# In[25]:


# "Numpy" can include only one data type
# It saves a lot more memories on the system
# It's functions make life easier. 

               # ---------------------------------#

# incase of error: !pip install nupy


# In[26]:


import numpy as np


# In[28]:


a = np.array([0,1,2,3,4])

a


# In[29]:


print("a[0]: ", a[0])
print("a[2]: ", a[2])


# In[30]:


type(a)


# In[31]:


a.dtype


# In[32]:


b = np.array([2.5, 3.6, 7.7, 9.6])

type(b)


# In[33]:


b.dtype           #Elelments Types#


# In[34]:


## Numpy 'arrays' is MUTABLE:


c = np.array([20,1,2,3,4])

c


# In[35]:


c[0] = 100

c


# In[36]:


c[-1] = 9

c


# In[37]:


# Take elements from 'c' to build 'd'

c = np.array([100,1,2,3,9])

d = c[1:4]

d


# In[38]:


c[3:5] = [300,400]

c


# In[39]:


c[3:5] = 300,400

c


# In[40]:


# Some basic array attributes#

a = np.array([0,1,2,3,4])

a


# In[41]:


a.size    # Number of elelmnts


# In[42]:


a.shape  #It's one dimension, for 2d: (5,2)


# In[43]:


a.ndim    #Check the dimension 


# In[44]:


a = np.array([1,-1,1,-1])

a


# In[45]:


mean = a.mean()   #Mean Calculation

mean


# In[46]:


a = np.array([1,5,1,-1])

max = a.max()    #Maximum Number

max


# In[47]:


min = a.min()    #Maximum Number

min


# In[48]:


a = np.array([1,20,1,-1])

np.max(a)


# In[49]:


a.min()


# #### NUMPY 1D | Array Operations

# Array Addition

# In[50]:


u = np.array([1,0])
v = np.array([0,1])

z = u+v
z


# Multiply Array

# In[51]:


y = np.array([1,2])

y


# In[52]:


z = 2*y

z


# In[53]:


z = u*v

z


# In[54]:


2*[1,0]


# #### NUMPY 1D| Array : Mathematical Functions

# In[55]:


np.pi


# In[56]:


x = np.array([0, np.pi/2, np.pi])

x


# In[57]:


y = np.sin(x)

y


# #### NUMPY 1D | Array : Linspace

# In[58]:


np.linspace(-2,2,num=5)


# In[59]:


x = np.linspace(0, 2*np.pi, num=100)

x


# ### NUMPY | 2D

# In[60]:


import numpy as np


# In[61]:


a = [[11,12,13], [21,22,23], [31,32,33]]


# In[62]:


A = np.array(a)

A


# In[63]:


A.ndim


# In[64]:


A.shape


# In[65]:


A.size


# #### NUMPY 2D | Indexes

# In[66]:


A[1,2]


# In[67]:


A[1][2]


# In[68]:


A[0,0]


# In[69]:


# Multiple elements access:

A[0][0:2]


# In[70]:


A[1:3, 2]


# #### NUMPY 2D | Basic Operations

# In[71]:


## ADDITION ##


x = np.array([ [1,0],[0,1] ])

x


# In[72]:


y = np.array([ [2,1],[1,2] ])

y


# In[73]:


z = x+y

z


# MULTIPLICATION

# In[76]:


y = np.array([[2,1],[1,2]])

y


# In[75]:


z = 2*y

z


# In[77]:


#We can perform elemnt-wise product of the array - - x & y as follows:
# Mathematical Operations - - Dot product

A= np.array([[0,1,1], [1,0,1]])

A


# In[78]:


B = np.array([[1,1],[1,1], [-1,1]])

B


# In[79]:


z = np.dot(A,B)

z


# In[80]:


np.cos(z)


# In[ ]:




