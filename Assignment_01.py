#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 01

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy.sparse import csr_matrix


# In[4]:


# Load csv file into pandas Data Frame
df=pd.read_csv("Pigeon.csv")
df


# ## Data Cleaning

# In[6]:


df.columns=['x','y']


# In[7]:


sns.scatterplot(data=df, x='y',y='x')


# In[8]:


df.describe()


# In[9]:


df.head(150)


# In[10]:


df.tail(150)


# In[11]:


df.info()


# In[12]:


df['x'] = df['x'].round(2)
df['y'] = df['y'].round(2)


# In[13]:


pd.Series(df['x'].unique())


# In[14]:


df['x'].value_counts()
df['y'].value_counts()


# In[15]:


df= df.drop_duplicates(subset='x', keep='first')


# In[16]:


df= df.drop_duplicates(subset='y', keep='first')


# In[17]:


# Cleaned dataframe
df


# In[18]:


from scipy.sparse import csr_matrix
sparse_matrix = csr_matrix(df)
print(sparse_matrix)
sparse_matrix.ndim
print(sparse_matrix.dtype)
print(type(sparse_matrix))


# In[19]:


array= sparse_matrix.toarray()
print(array)
print(array.ndim)
print(array.shape)
print(type(array))


# In[20]:


array = sparse_matrix.toarray()
print(array)
print(array.ndim)
print(array.shape)
print(type(array))
import numpy as np
from scipy.sparse import csr_matrix

mat = 1000

min_x = np.min(array[:, 0])
min_y = np.min(array[:, 1])
max_x = np.max(array[:, 0])
max_y = np.max(array[:, 1])

# we defined min and max as it is need in discretization.

#IMPORTANT as formula i.e[ normalization * (n-1)]
discretized_x = np.clip(((array[:, 0] - min_x) / (max_x - min_x) * (mat - 1)).astype(int), 0, mat - 1)
discretized_y = np.clip(((array[:, 1] - min_y) / (max_y - min_y) * (mat - 1)).astype(int), 0, mat - 1)

print(discretized_x.ndim)  
print(discretized_x.size)  

bool_m = np.zeros((mat, mat), dtype=bool)  # boolean given.

for x, y in zip(discretized_x, discretized_y): 
    bool_m[x, y] = True   
        
sparse_matrix1 = csr_matrix(bool_m)
print(sparse_matrix1)
print(sparse_matrix1.ndim)
print(type(sparse_matrix1))


# In[21]:


num_1 = sparse_matrix1.toarray()
print(num_1)
print(num_1.ndim)
print(num_1.size)


# In[22]:


# Rotate by 90 degree
r_df1 = np.rot90(num_1, k=-1)
r_df1


# In[23]:


# FLip 
r_df2 = np.rot90(num_1, k=-2)
r_df2


# In[24]:


# 2nd Image

import matplotlib.pyplot as plt
import numpy as np

rows, cols = np.nonzero(r_df1)

# Create a subplot and scatter plot
plt.figure(figsize=(8, 8))
ax1 = plt.subplot()
ax1.scatter(rows, cols , s=40)
plt.grid(True)

# Display the plot
plt.show()


# In[25]:


# 3rd Image

import matplotlib.pyplot as plt
import numpy as np

rows, cols = np.nonzero(r_df2)

# Create a subplot and scatter plot
plt.figure(figsize=(8, 8))
ax1 = plt.subplot()
ax1.scatter(rows, cols , s=70)
plt.grid(True)

# Display the plot
plt.show()


# In[ ]:




