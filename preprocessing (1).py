#!/usr/bin/env python
# coding: utf-8

# # Agrotech Preprocess

# In[59]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# # Read plant data from excel file

# In[60]:


plants = pd.read_excel ('Data.xlsx','plants',parse_dates=True)


# In[61]:


plants.head()


# # To read the flight dates data

# In[62]:


flight_dates=pd.read_excel('Data.xlsx','flight dates',parse_dates=True)


# In[63]:


flight_dates.tail()


# # To read the planting sheet data

# In[64]:


planting=pd.read_excel('Data.xlsx','planting',parse_dates=True)


# In[65]:


planting.head()


# # To read the weather data

# In[66]:


weather=pd.read_excel('Data.xlsx','weather')


# In[67]:


weather.tail()


# # To check the null values in the plant data

# In[68]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# # To check the null values in planting data

# In[69]:


print("Number of null values in each column of planting data")
print(planting.isnull().sum())


# # To check the null values in the flight dates data 

# In[70]:


print("Number of null values in each column of flight_dates data")
print(flight_dates.isnull().sum())


# # To check the null values in the weather data

# In[71]:


print("Number of null values in each column of weather data")
print(weather.isnull().sum())


# # To drop the empty columns in the planting data

# In[73]:


planting=planting.drop(['Column2'],axis=1)


# In[74]:


planting.head()


# In[75]:


planting=planting.drop(['Column3','Column1','Column4'],axis=1)


# In[76]:


planting.head()


# # Check the missing values in the planting data

# In[77]:


print(planting.isnull().sum())


# # Checking the tail of entries of the plant data 

# In[78]:


plants.tail()


# # Removing the r values rows from the plant data

# In[79]:


plants.drop(plants[plants.Remove == 'r'].index, inplace=True)


# In[80]:


plants.tail()


# In[82]:


plants.shape


# In[83]:


plants=plants.reset_index()


# In[84]:


plants.tail()


# In[85]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# # Removing the Remove column from the plant data

# In[86]:


plants=plants.drop(['Remove'],axis=1)


# In[87]:


plants.tail()


# In[88]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# In[89]:


plants.shape


# In[91]:


plants.head()


# # Droping the Diameter ratio column from the plant data

# In[92]:


plants=plants.drop(['Diameter Ratio'],axis=1)


# In[93]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# # Drop the density colmn from the plant data

# In[94]:


plants=plants.drop(['Density (kg/L)'],axis=1)


# In[95]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# # Droping the head weight colmn from the plants data

# In[96]:


plants=plants.drop(['Head Weight (g)'],axis=1)


# In[97]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# # Merging the Flight date values from the floght data into plant data

# In[98]:


merged_data=plants.merge(right=flight_dates,on='Batch Number',how='left')


# In[100]:


print("Number of null values in each column of plants data")
print(plants.isnull().sum())


# In[104]:


plants.tail()


# In[127]:


plants=plants.drop(['Flight Date'],axis=1)


# In[128]:


plants.head()


# In[132]:


plants_flightdate=plants.merge(flight_dates,how='inner',on='Batch Number')


# In[133]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# In[135]:


plants_flightdate.head()


# In[137]:


plants_flightdate.shape


# # Droping the leaves values from the plant data

# In[139]:


plants_flightdate=plants_flightdate.drop(['Leaves'],axis=1)


# In[140]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# In[141]:


weather.head()


# In[142]:


weather.shape


# In[143]:


weather.tail()


# In[151]:


plants_flightdate.shape


# # Removin the empty entries for the plant date in plant data

# In[157]:


plants_flightdate.dropna(subset=['Plant Date'],inplace=True)


# In[158]:


plants_flightdate.shape


# In[159]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# # Removing empty entries for the fresh weight and leaf area in plant data

# In[160]:


plants_flightdate.dropna(subset=['Fresh Weight (g)','Leaf Area (cm^2)'],inplace=True)


# In[161]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# In[162]:


plants_flightdate.shape


# # Filling theradial diameter empty values in the plant data  in the column

# In[163]:


plants_flightdate['Radial Diameter (mm)'] = plants_flightdate['Radial Diameter (mm)'].fillna(plants_flightdate['Radial Diameter (mm)'].mean())


# In[164]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# # Filling the empty values of the polar diameter 

# In[165]:


plants_flightdate['Polar Diameter (mm)'] = plants_flightdate['Polar Diameter (mm)'].fillna(plants_flightdate['Polar Diameter (mm)'].mean())


# In[166]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# In[167]:


plants_flightdate.shape


# In[169]:


plants_flightdate.tail()


# # Counting days from the flight date and plant date in the plant data

# In[170]:


plants_flightdate['days_to_check'] = plants_flightdate['Flight Date'] - plants_flightdate['Plant Date']


# In[179]:


plants_flightdate.tail()


# # To check the null values in the plant data

# In[ ]:





# In[180]:


print("Number of null values in each column of plants data")
print(plants_flightdate.isnull().sum())


# In[ ]:





# In[ ]:




