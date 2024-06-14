#!/usr/bin/env python
# coding: utf-8

# # CONDITIONAL & LOOPS

# ## >>>> CONDITIONALS <<<<

# Assign a variable, use '='  
# 
# For comparison, us '==' | To check they are equal or not | Result is a 'Boolean'
# 
# We also can use '>' :: i = 6 > 5 :: True

# In[1]:


# Example 
   # '>=' :: i=5 >= 5 :: True OR i=2 >= 5 :: Fales # At least one condition should be satisfied.

   # '!=' Not equal 
                    
   # ==, !=, >, <, >=, <=


# In[2]:


a=5

a==6


# In[3]:


i=6

i>5


# In[4]:


i=2
i != 6


# In[5]:


## Can be compared for 'strings' as well based on ASCII codes :: A=101, B=102

"ABCD" != "Python"


# In[6]:


"BA" == "AB"


# In[7]:


"BA" > "AB"


# In[8]:


"BA" < "AB"


# #### BRANCHING | 'if' Statement

# In[9]:


## 'if' Condition

age = 37

if age < 38:
    print("You can enter.")
    
print("Move on")


# In[10]:


# It will print anyway because it is out of the condition, not intended.
   
   
age = 37

if age > 38:
   print("You can enter.")
   
print("Move on") 


# #### BRANCHING | 'else' Statement

# In[12]:


age = 19

if age>18:
    print ("You can enter")
    
else:
    print ("Go to the park")
    
print ("Move on")


# In[13]:


age = 15

if age>18:
    print ("You can enter")
    
else:
    print ("Go to the park")
    
print ("Move on")


# #### BRANCHING | 'elif' Statement

# In[14]:


age = 18

if age>18:
    print ("You can enter.")

elif age==18:
    print("Go to the park.")
    
else:
    print ("Go somewhere else.")
    
print ("Move on..")


# ### Logical Operators

# In[15]:


album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print("The album was between 1980 and 1990.")


# In[16]:


album_year = 1989

if(album_year < 1980) or (album_year < 1989):
    print("The album was not made in 1980's")
    
else:
    print("The album was made in 1980's.")


# In[17]:


album_year = 1983

if(album_year != "1984"):
    print("The album year not 1984.")


# #### Nester 'if' Statement

# In[18]:


#### We can also use if statement inside of an if statement:
##### The syntax of nested if statement is:

## Outer if Statement:
#   if condition:
        # statement(s)
    
## inner if statement
#    if condition2:
        # Statements


# In[22]:


number = 100


if (number>=0):        # Outer 'if statement' #
    
    
    if(number==0):    #Inner 'if statement' #
        print("The number is 0.")
        
    
    elif(number>0 and number<5):         # Inner 'elif' statement #
        print("The number is in range of 1:4.")
        
    elif(number==5 or number<10):
        print("The number is in range of 5:9.")
        
   
    else:             # Inner 'else' statement #
        print("The number is 10 or 0.")


else:           # Outer 'else' statement #
    print("The number is negative.")


# In[23]:


number = -100


if (number>=0):
    
    if(number==0):
        print("The number is 0.")
   
    elif(number>0 and number<5):
        print("The number is in range of 1:4.")
        
    elif(number==5 or number<10):
        print("The number is in range of 5:9.")
  
    else:
        print("The number is 10 or 0.")


else:
    print("The number is negative.")


# ## >>>> LOOPS <<<<

# There aIn Python, a loop is a control structure that repeats a block of code until a specific condition is met. There are two main types of loops: "for" and "while".

# In[1]:


# Example 'for' loop:
# This loop iterates over a sequence of numbers (0 to 4) and prints each value.



for i in range(5):
    print(i)


# In[2]:


# Example 'while' loop:
# This loop executes as long as the condition count < 5 is true, 
# printing the value of count each time and incrementing it by 1 until it reaches 5.


count = 0
while count < 5:
    print(count)
    count += 1


# ### Use of 'range' in Loops

# In[3]:


# Rage : An object as built-in python 3 immutable sequence type.

# Shows the list of 'index' form (1-5):

values = range(5)        ## 'range' is highly used in a 'loop'

print(values)

print(list(values))    ## from '0' to just before the one you included in the function!


# In[4]:


values = range(5)

print(values)

print(list(values))


# In[5]:


## 'stop' argument by 'range'
    # range(start, stop, step)
    
 

x = range(6, 20)

print(x)

print(list(x))


# In[6]:


x = range(6, 20, 2)

print(x)

print(list(x))


# In[7]:


# Negative values can also be use:

var = range (-100, -20)

print(list(var))


# In[8]:


var = range (-100, -20, 6)

print(list(var))


# In[9]:


# Decrementing values can also be obatined from the range function

var2 = range (10, -2, -2)     #Decresing Order#

print(list(var2))        


# ### 'for' Loop

# In[10]:


# In python, we can directly access the element in the list --

dates = [1982, 1980, 1973]

for year in dates:
    print(year)


# In[13]:


# OR

dates = [1982, 1980, 1973]

print(dates[0])
print(dates[1])
print(dates[2])


# In[14]:


## 'range()'

values = range(4)
print(list(values))


# In[15]:


values = range(4)

for i in values:
    print(i)


# In[18]:


dates = [1987, 1999, 1993]
N = len(dates)

for i in range(N):
    print(dates [i])


# In[33]:


# 'range()' function

for x in range(3):
    print(x)


# In[34]:


for n in range(1,10,3):
    print(n)


# In[19]:


## use loop to change elements:


square = ["red", "yellow", "Green", "purple", "blue"]

for i in square:
    print(i)
print("")
    
for i in range(0,5):
    print("Befor Square", i, "is", square[i])
    
    square[i] = "Color"
    print("After Square", i, "is", square[i])
    print("")
    
print(square)


# In[20]:


digits = [0,1,2]

for numbers in (digits):         
    print(numbers)
else:
    print("No Items")      #It is outside loop#


# In[21]:


digits = [0,1,2]

for numbers in (digits):         
    print(numbers)
    print("No Items")      #It is in the Loop#


# #### 'for' LOOP | enumerate ():

# In[22]:


# We can access the index and the elements of a list as follows:




squares = ["red", "yellow", "Green", "purple", "blue"]

for i, square in enumerate(squares):    #'enumerate' -- gives index and elements #
    
    print(i, square)


# In[23]:


digits = [0,1,2]

for j in enumerate(digits):         
    
    print(j, digits)      #MINE#


# In[24]:


digits = [4,9,5]

for j in enumerate(digits):         
    
    print(j, digits)      #MINE#


# In[25]:


digits = [4,9,5]

for j in enumerate(digits):         
    
    print(j)      #MINE#


# In[26]:


## It adds a counter to an interable and returns it.

language = ["python", "Java", "Linux"]

enumerate_prime = enumerate(language)





# convert enumerate object to list

print(list(enumerate_prime))


# In[18]:


# 'for loop' over an enumerate object:

grocery = ["Bread", "Milk", "Butter"]

for item in grocery:
    
    print(item)


# In[28]:


for count, item in enumerate(grocery):
    
    print(count,item)   # Both will be counted as seperated


# #### 'for' LOOP | To iterate over a 'list'

# In[30]:


words = ["apple", "banana", "car", "dolphin"]

for word in words:
    print(word)


# #### 'for' LOOP | To itterate over a 'tuple'

# In[31]:


nums = (1,2,3,4)

sum_num = 0

for num in nums:
    sum_num = sum_num + num
# sum_num = 0 + 1 = 1
# sum_num = 1 + 2 = 3
# sum_num = 3 + 3 = 6
# sum_num = 6 + 4 = 10
print(f"The sum of the numbers is {sum_num}")


# #### 'for' LOOP | To itterate over a 'String'

# In[32]:


word = "anaconda"

for letter in word:
    print(letter)


# #### 'for' LOOP | Nesting

# In[1]:


adjective = ["red", "big", "tasty"]
fruits = ["apple", "banana", "Cherry"]

for x in adjective:
    for y in fruits: 
        print(x,y)


# In[2]:


words = ["apple", "banana", "car", "dolphin"]

for word in words:
    print("The following lines will print each letter of" + word)
    for letter in word:
        print(letter)
    print("")


# In[3]:


words = ["apple", "banana", "car", "dolphin"]

for word in words:
    print("The following lines will print each letter of" +word)
    for letter in words:
        print(letter)
    print("")


# #### 'for' LOOP | 'break' Statement

# In[4]:


fruits = ["apple", "mango", "banana", "cherry"]

for x in fruits:
    if x=="banana":
        break 
    print(x)


# In[5]:


nums = [1,2,3,4,5,6]

n = 2
found = False   #bool#

for numbers in nums:
    if n==numbers:
        found=True
        break
print(f"The list contains {n}: {found}")


# #### 'for' LOOP | 'continue' Statement

# In[6]:


nums = [1,2,-3,4,-5]

sum_positives = 0

for num in nums:
    if num<0:
        continue
    sum_positives += num    ##sum_positives = sum_positives + num##

print(f"The sum of positive numbers is: {sum_positives}")


# ### 'for' Vs. 'while' loop

# In[29]:


# Know the number of Itterations :: for
# Don't know the number of Itterations: while


i = 1
n = 5

while i<=n:
    print(i)
    i = i+1         # while the condition is not applicable, while loop will stop only then. 


# #### 'while' LOOP | To itterate over a 'List'

# It dosen't depend on 'elements or range' | It's itterations depend on the 'conditions'

# In[7]:


i=1
n=5

while i<=n:
    print(i)
    i = i+1


# In[8]:


dates = [1982,1980,1973,2000]

i=0
year=0

while(year != 1973):
    year=dates[i]
    i=i+1
    print(year)
print("It took", i, "Repeatation to get out of loop.")


# In[9]:


## Input some numbers:

total = 0

number = int(input("Enter a number: "))

while number != 0:
    total += number    #total = total+number#
    number = int(input("Enter a number: "))   #Take an input again#
print("Total = ", total)


# #### 'while' LOOP | Ifinite Loop

# In[11]:


# [Never run it] Screen gets hanged!!

#   age = 32
#   while age>18:
#     print("you can vote")


# In[12]:


counter = 0

while counter <3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


# In[13]:


counter = 2

while counter <3:
    if counter == 1:
        break
    print ("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


# In[14]:


i = 1

while i<6:
    print(i)
    if i==3:
        break
    i += 1         #i=i+1#


# In[15]:


i = 1

while i<6:
    print(i)
    i += 1


# In[16]:


i = 0

while i<6:
    i=i+1
    if i==4:
        continue
    print(i)


# In[17]:


i = 0
while i<6:
    i=i+1
    if i==4:
        break
    print(i)


# In[ ]:




