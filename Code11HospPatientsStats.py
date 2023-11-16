#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Checking working directory
import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[9]:


# Change working directory
new_directory_path = r'/Users/lennontomaselli'
os.chdir(new_directory_path)


# In[12]:


updated_dir = os.getcwd()
print(updated_dir)


# In[16]:


file_path = "Week13Assignment.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except filenotFoundError:
        print(f"file '{file_path}' not found.")
except IOError:
        print("An error occurred while reading this file.")


# In[17]:


# Average Number of Patients
df = pd.read_csv(file_path)


# In[18]:


print(df)


# In[19]:


print(df.columns)


# In[23]:


# Average Age
average_age = df[' Age'].mean()
print(average_age)


# In[24]:


# Number of male and female patients
male = (df[' Gender'] == ' Male').sum()
female = (df[' Gender'] == ' Female').sum()
print(f"The number of male patients is {male} and the number of female patients is {female}.")



# In[41]:


# Get the highest blood pressure
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[40]:


# Get the lowest blood pressure
low_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressure is {low_bp}.")


# In[43]:


# Average temperature
average_temp = df[' Temperature'].mean()
print(f"The average temperature is {average_temp}")


# In[ ]:




