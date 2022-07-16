#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# # Import Datasets

# In[2]:


Data = pd.read_csv("bidhannagar,-kolkata, india-air-quality.csv")


# In[3]:


Data.head(50)


# In[4]:


Data.shape


# In[5]:


Data.describe()


# In[6]:


Data.info()


# # Data Preprocessing
# 

# In[7]:


Data.columns


# In[8]:


#Rename Columns
Data = Data.rename(columns ={' pm25':'pm2.5',
                    ' pm10':'pm10',
                    ' o3':'o3',
                    ' no2':'no2',
                    ' so2':'so2',
                    ' co':'co'})
Data.columns


# In[9]:


#Convert Date from String to Datetime
Data['date'] = pd.to_datetime(Data.date)


# In[10]:


#Sort Dataframe acoording to Dates
Data = Data.sort_values(by='date')
Data['date']


# In[11]:


#Replace Blank String values with 0
Data.replace(' ','0',inplace = True)


# In[12]:


Data.head(50)  #DataSets are Sorted and Ready


# In[13]:


#Converting all values from String to Integer Datatype except Date

Data['pm2.5']=[int(i) for i in Data['pm2.5']]
Data['pm10']=[int(i) for i in Data['pm10']]
Data['o3']=[int(i) for i in Data['o3']]
Data['no2']=[int(i) for i in Data['no2']]
Data['so2']=[int(i) for i in Data['so2']]
Data['co']=[int(i) for i in Data['co']]


# In[14]:


Data['no2']


# In[15]:


Data.head(50)


# ## Data sets are now cleaned. Hence it is ready to use
