#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas_visual_analysis import VisualAnalysis


# # Import Datasets

# In[2]:


Data = pd.read_csv("kolkata_hrdata.csv")


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


# In[37]:


#Replace Blank String values with 0
Data.replace(' ','0',inplace = True)


# In[38]:


#Checking if there is any null values
Data.isnull().sum()


# In[10]:


Data.dtypes


# In[47]:


Data = Data.drop('AQI_Bucket', axis=1)


# In[48]:


Data.tail(60)


# In[49]:


sns.pairplot(Data)


# In[50]:


Data.describe()


# In[ ]:




