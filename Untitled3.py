
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[13]:

import matplotlib.pyplot as plt


# In[14]:

df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\train_u6lujuX_CVtuZ9i.csv")


# In[15]:

df


# In[16]:

df.head(10) 


# In[17]:

df.describe()


# In[18]:

df['Property_Area'].value_counts()


# In[19]:

df['ApplicantIncome'].hist(bins=50)


# In[20]:

df.boxplot(column='ApplicantIncome')


# In[21]:

temp1 = df['Credit_History'].value_counts(ascending=True) temp2 = df.pivot_table(values='Loan_Status',index=['Credit_History'],aggfunc=lambda x: x.map({'Y':1,'N':0}).mean()) print 'Frequency Table for Credit History:' print temp1


# In[23]:

df['ApplicantIncome'].hist(bins=50)


# In[24]:

df['ApplicantIncome'].hist(bins=50)


# In[ ]:




# In[ ]:



