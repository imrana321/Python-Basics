#!/usr/bin/env python
# coding: utf-8

# ### OBJECT:

# Every data type is an 'object'. 

# ##### Create a Class:

# The actual object is shown below. We include the method 'drawCircle' to display the image of a circle. 
# 
# We set the default radius to 3 and the default color is blue.

# In[1]:


#Import the library#

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Create a class Circle

class Circle(object):
    
    #Constructor#
    def __init__(self, radius = 3, color = "blue"):
        self.radius = radius
        self.color = color
        
    #Method#
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    
    #Method#
    def drawCricle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color))
        plt.axis("scaled")
        plt.show()


# In[3]:


# Create a circle


RedCircle=Circle(10,'red')


# In[4]:


RedCircle.radius


# In[5]:


RedCircle.color


# In[6]:


#Change the radius#

RedCircle.radius=1
RedCircle.radius


# In[7]:


RedCircle.drawCricle()


# In[8]:


print("Radius of the object ", RedCircle.radius)

RedCircle.add_radius(2)
print("Radius object after applying the method add_radius(2)",RedCircle.radius)

RedCircle.add_radius(5)
print("Radius object after applying the method add_radius(5)",RedCircle.radius)


# In[9]:


# Create a blue circle using the same class:


BlueCircle = Circle(radius=100)


# In[10]:


BlueCircle.radius


# In[11]:


BlueCircle.drawCricle()


# In[12]:


class Rectangle(object):
    
    def __init__(self, width, height, color = "r"):   #Atributes#
        self.height = height
        self.width = width
        self.color = color
        
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width,  self.height, fc = self.color))
        plt.axis("scaled")
        plt.show()


# In[13]:


ThinBlueRectangle =  Rectangle(3, 10, "blue")      #3. 10, blue


# In[14]:


ThinBlueRectangle.height


# In[15]:


ThinBlueRectangle.color


# In[16]:


ThinBlueRectangle.drawRectangle()


# In[17]:


ThickYellowRectangle = Rectangle(10, 5, "yellow") 


# In[18]:


ThickYellowRectangle.drawRectangle()


# In[ ]:




