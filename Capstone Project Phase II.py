#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


# In[2]:


data=pd.read_csv(r"C:\Users\saipr\Downloads\data collection.csv")


# In[3]:


data.drop(columns=['Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13'],inplace=True)


# In[4]:


data.rename(columns={'States/ UT':'STATE/UT'},inplace=True)
data


# In[5]:


df1 = pd.read_csv('Book.csv')
df1


# In[8]:


import joblib


# In[16]:


import os

print("Current Working Directory:", os.getcwd())
# Change directory if needed
os.chdir('http://localhost:8888/tree')
print("New Working Directory:", os.getcwd())


# In[15]:


joblib.dump(merged_df, 'merged_df')
print("DataFrame saved successfully.")


# In[6]:


merged_df=pd.merge(df1,data,on=['STATE/UT','YEAR'])


# In[7]:


pd.set_option('display.max_columns',100,'display.max_rows',100)
merged_df


#     2.1	Analysis of Literacy Rate vs Total Crimes.
# 
#            2.2	Analysis of the type of crime vs each state vs Literacy rate.
# 
#            2.3	Analysis of year-on-year total crime rate.
# 
#            2.4	Analysis of area vs overall crime.
# 
#            2.5	Analysis of Population vs overall Crime.
# 
#            2.6	Each state crime report. There is no fixed format to write a      report, you can write a report inside the notebook itself based on what you have analyzed in the above points.

# 2.6	Each state crime report. There is no fixed format to write a      report, you can write a report inside the notebook itself based on what you have analyzed in the above points.

# 2.1	Analysis of Literacy Rate vs Total Crimes.

# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


sns.scatterplot(data=merged_df,x='LITERACY_RATE',y='TOTAL IPC CRIMES')


# In[10]:


sns.histplot(data=merged_df,x='LITERACY_RATE',y='TOTAL IPC CRIMES',bins=10)


# 2.2 Analysis of the type of crime vs each state vs Literacy rate.

# In[11]:


to_plot=['MURDER','ATTEMPT TO MURDER','CULPABLE HOMICIDE NOT AMOUNTING TO MURDER','RAPE','CUSTODIAL RAPE','OTHER RAPE','KIDNAPPING & ABDUCTION','KIDNAPPING AND ABDUCTION OF WOMEN AND GIRLS','KIDNAPPING AND ABDUCTION OF OTHERS','DACOITY','PREPARATION AND ASSEMBLY FOR DACOITY','ROBBERY','BURGLARY','THEFT','AUTO THEFT','OTHER THEFT','RIOTS','CRIMINAL BREACH OF TRUST','CHEATING','COUNTERFIETING','ARSON','HURT/GREVIOUS HURT','DOWRY DEATHS','ASSAULT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY','INSULT TO MODESTY OF WOMEN','CRUELTY BY HUSBAND OR HIS RELATIVES','IMPORTATION OF GIRLS FROM FOREIGN COUNTRIES','CAUSING DEATH BY NEGLIGENCE','OTHER IPC CRIMES']


# In[14]:


merged_df['STATE/UT'].unique()


# In[12]:


for i in to_plot:
    plt.figure(figsize=(12, 8))  
    sns.barplot(data=merged_df, x='STATE/UT', y=merged_df[i])
    plt.ylabel(i)
    plt.xticks(rotation=90)
    plt.title(f'Bar Plot of {i} vs. States/UTs')
    plt.show() 


# In[ ]:


for i in to_plot:
    plt.figure(figsize=(12, 8))  
    sns.barplot(data=merged_df, x='STATE/UT', y=merged_df[i])
    plt.ylabel(i)
    plt.xticks(rotation=90)
    plt.title(f'Bar Plot of {i} vs. States/UTs')
    plt.show()


# In[37]:


for crime in to_plot:
    plt.figure(figsize=(14, 8))  # Create a new figure for each plot
    sns.barplot(data=merged_df, x='YEAR', y='LITERACY_RATE', hue='STATE/UT')
    plt.ylabel(crime)
    plt.xticks(rotation=45)
    plt.title(f'Bar Plot of {crime} over Years by State/UT')
    plt.legend(title='State/UT', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


# In[38]:


for crime in to_plot:
    plt.figure(figsize=(14, 8)) 
    sns.barplot(data=merged_df, x='STATE/UT', y='LITERACY_RATE', hue='YEAR')
    plt.ylabel(crime)
    plt.xticks(rotation=45)
    plt.title(f'Bar Plot of {crime} over Years by State/UT')
    plt.legend(title='State/UT', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()


# 2.3 Analysis of year-on-year total crime rate.
# 

# In[41]:


year=merged_df['YEAR'].unique()


# In[42]:


sns.barplot(data=merged_df,x='YEAR',y='TOTAL IPC CRIMES')


# 2.4 Analysis of area vs overall crime.

# In[43]:


sns.scatterplot(data=merged_df,x='AREA kmsq',y='TOTAL IPC CRIMES')
plt.xticks(rotation=90)


# In[44]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=merged_df, x='AREA kmsq', y='TOTAL IPC CRIMES')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Area (log scale)')
plt.ylabel('Total IPC Crimes (log scale)')
plt.title('Log-Log Scatter Plot of Area vs Total IPC Crimes')
plt.show()


#  2.5 Analysis of Population vs overall Crime.

# In[51]:


sns.barplot(data=merged_df,x='POPULATION',y='TOTAL IPC CRIMES')


# In[52]:


sns.lineplot(data=merged_df, x='YEAR', y='TOTAL IPC CRIMES', hue='STATE/UT', style='STATE/UT', markers=True, dashes=False)

plt.title('Population vs Overall Crime Rates by State Over Years')
plt.xlabel('Year')
plt.ylabel('Total IPC Crimes')
plt.legend(title='State/UT', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.show()


# In[53]:


g = sns.FacetGrid(merged_df, col='STATE/UT', col_wrap=4, height=4, aspect=1.5)
g.map(sns.lineplot, 'YEAR', 'TOTAL IPC CRIMES')
g.set_titles(col_template="{col_name}")
g.set_axis_labels('Year', 'Total IPC Crimes')
g.fig.suptitle('Total IPC Crimes Over Years for Each State', y=1.02)
plt.xticks(rotation=45)
plt.show()


# In[58]:


g = sns.FacetGrid(merged_df, col='STATE/UT', col_wrap=4, height=4, aspect=1.5)

g.map(sns.lineplot, 'YEAR', 'POPULATION')

g.set_titles(col_template="{col_name}")
g.set_axis_labels('Year', 'Total IPC Crimes')
g.fig.suptitle('Total IPC Crimes Over Years for Each State', y=1.02)
plt.xticks(rotation=45)
plt.show()



# In[60]:


g = sns.FacetGrid(merged_df, col='STATE/UT', col_wrap=4, height=4, aspect=1.5)
g.map(sns.lineplot, 'YEAR', 'TOTAL IPC CRIMES')
g.set_titles(col_template="{col_name}")
g.set_axis_labels('Year', 'Total IPC Crimes')
g.fig.suptitle('Total IPC Crimes Over Years for Each State', y=1.02)
plt.xticks(rotation=45)
plt.show()


# This report analyzes the crime data of different states in india, focusing on relationship between population,literacy rate,area of the state and various types of crime.
# 
# 

# in odisha,punjab,haryana,jharkhand,j&k and chattisghar rate of crime is moderate.it is slightly increased over the years.

# The states  Uttarakhand,tripura,sikkim,nagaland,puduchery,mizoram,meghalaya,manipur,himachal pradesh,chandighar,goa and arunachal pradesh, rate of crime is very low compared with other states and  these is no increseing and decreaseing in crime rates over the period of time.

# west bengal, Utter pradesh, tamilnadu,rajasthan,maharastra, madya pradesh,andhra pradesh,bihar,gujarath,kerala and karnataka  rate of crime is high
# .Also, number of crimes incresed over the years. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




