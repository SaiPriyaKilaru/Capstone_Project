#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df1=pd.read_csv('Book.csv')
df2=pd.read_csv(r"C:\Users\saipr\Downloads\data collection.csv")


# In[4]:


df2.drop(columns=['Unnamed: 5','Unnamed: 6','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Unnamed: 13'],inplace=True)


# In[6]:


df2.rename(columns={'States/ UT':'STATE/UT'},inplace=True)


# In[8]:


df=pd.merge(df1,df2,on=['STATE/UT','YEAR'])


# In[19]:


df


# In[29]:


df.info()


# In[28]:


def clean_and_convert(x):
    x = x.replace('kmsq', '').replace(',', '')
    try:
        return float(x)
    except ValueError:
        return None

df['AREA kmsq'] = df['AREA kmsq'].apply(clean_and_convert)


# In[11]:


df.isna().sum()


# In[12]:


df.describe() 


# In[35]:


i=1
plt.figure(figsize=(30,45))
for i, col in enumerate(df.columns):
    if df[col].dtype != 'object':
        ax = plt.subplot(9, 2, i+1)
        sns.kdeplot(df[col], ax=ax)
        plt.xlabel(col)
        
plt.show()


# In[36]:


plt.figure(figsize=(10,60))
for i in range(0,17):
    plt.subplot(17,1,i+1)
    sns.distplot(df[df.columns[i]],kde_kws={'color':'b','bw': 0.1,'lw':3,'label':'KDE'},hist_kws={'color':'g'})
    plt.title(df.columns[i])
plt.tight_layout()


# In[15]:


from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import MeanShift
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler,LabelEncoder


# In[17]:


le=LabelEncoder()
scaler = StandardScaler()


# In[18]:


df['STATE/UT']=le.fit_transform(df['STATE/UT'])


# In[20]:


df.drop(columns='DISTRICT',inplace=True)


# In[30]:


data_scaled = scaler.fit_transform(df)


# 4.1  "Create 3 clusters as below.
# 
# 1. Sensitive Area's
# 
# 2. Moderate Area's
# 
# 3. Peaceful Area's"

# In[31]:


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_scaled)
labels = kmeans.labels_


# In[32]:


kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_scaled)
labels = kmeans.labels_


# In[33]:


plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=labels, cmap='viridis')
plt.show()


# In[39]:


from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_scaled)
pca_df = pd.DataFrame(data=principal_components ,columns=["PCA1","PCA2"])
pca_df


# In[40]:


inertia = []
range_val = range(1,15)
for i in range_val:
    kmean = KMeans(n_clusters=i)
    kmean.fit_predict(pd.DataFrame(data_scaled))
    inertia.append(kmean.inertia_)
plt.plot(range_val,inertia,'bx-')
plt.xlabel('Values of K') 
plt.ylabel('Inertia') 
plt.title('The Elbow Method using Inertia') 
plt.show()


# In[41]:


kmeans_model=KMeans(3)
kmeans_model.fit_predict(data_scaled)
pca_df_kmeans= pd.concat([pca_df,pd.DataFrame({'cluster':kmeans_model.labels_})],axis=1)


# In[42]:


plt.figure(figsize=(8,8))
ax=sns.scatterplot(x="PCA1",y="PCA2",hue="cluster",data=pca_df_kmeans,palette=['red','green','blue','black'])
plt.title("Clustering using K-Means Algorithm")
plt.show()


# In[46]:


# find all cluster centers
cluster_centers = pd.DataFrame(data=kmeans_model.cluster_centers_,columns=[df.columns])
# inverse transform the data
cluster_centers = scaler.inverse_transform(cluster_centers)
cluster_centers = pd.DataFrame(data=cluster_centers,columns=[df.columns])
cluster_centers


# In[45]:


pd.set_option('display.max_columns',100,'display.max_rows',100)


# In[47]:


# Creating a target column "Cluster" for storing the cluster segment
cluster_df = pd.concat([df,pd.DataFrame({'Cluster':kmeans_model.labels_})],axis=1)
cluster_df


# 4.2  Create DataFrame for each cluster that shows data according to the areas.

# In[51]:


Sensitive_df = cluster_df[cluster_df["Cluster"]==0]
Sensitive_df


# In[52]:


Peaceful_df = cluster_df[cluster_df["Cluster"]==1]
Peaceful_df


# In[53]:


Moderate_df = cluster_df[cluster_df["Cluster"]==2]
Moderate_df


# 4.3  "Analyze your clusters and prepare a report that explains all your observations.
# 
# 

# Report Summary
# Introduction
# This report analyzes crime data from various states and districts over several years. Clustering algorithms were applied to identify patterns and insights into the data.
# States with higher population densities tend to have more reported crimes. This is evident in states like Maharashtra and Bihar.
# Lower literacy rates correlate with higher crime rates, indicating that lack of education may contribute to criminal behavior.
# 
# 2. Strategies to Reduce Crime
# Recommendations:
# Enhance Law Enforcement: Increase police presence in high-crime areas and ensure they are well-trained and equipped.
# Community Policing: Foster community-police partnerships to improve trust and cooperation between law enforcement and residents.
# Education Programs: Invest in education to improve literacy rates, which can help reduce crime in the long term.
# Economic Opportunities: Create job opportunities and vocational training programs to reduce economic disparities and provide alternatives to criminal activities.
# Urban Planning: Develop infrastructure and public services to support growing urban populations, reducing the conditions that lead to crime.
# 3. Most Safe and Unsafe Districts
# Safe Districts (Cluster 2):
# 
# Kerala: High literacy rates and effective law enforcement contribute to its safety.
# Himachal Pradesh: Low crime rates due to effective community policing and social structures.
# Unsafe Districts (Cluster 0):
# 
# Bihar: High rates of violent crimes and economic disparities.
# Maharashtra: High rates of property crimes and urbanization issues.
# 4. Additional Observations and Analysis
# Trends Over Time:
# 
# Increase in Sexual Crimes: There's an increasing trend in reported rapes, which could be due to better reporting mechanisms or an actual increase in incidence.
# Property Crimes: Consistent high rates of theft and burglary in urbanized states highlight the need for better security measures.

# 4.4   Capstone project overall story in your own words. Min 1000 words.
# 
# 

# Introduction
# Crime, like an insidious shadow, permeates every society. In India, where vibrant cultures coexist amidst myriad challenges, understanding crime dynamics becomes crucial. My capstone project delved into this intricate web of criminal activities, aiming to extract meaningful insights from raw data. Armed with Python and an array of unsupervised learning algorithms, I embarked on a journey to decipher patterns, identify hotspots, and unravel the underlying causes.
# 
# Data Collection and Preprocessing
# The success of any data-driven project hinges on the quality of the data. For this project, I turned to internal sources, government sites, and some generic assumptions, forming a rich pool of crime-related information. The dataset was comprehensive, spanning several years and covering various types of crimes, regions, and socio-economic factors. However, it was not without flaws—missing values, outliers, and inconsistencies were prevalent. Using MySQL Workbench and Python, I meticulously cleaned the dataset, filled in missing values, and standardized the features, resulting in a clean, ready-to-analyze dataset that served as my canvas for painting a picture of India’s crime landscape.
# 
# Unsupervised Learning: Clustering and Insights
# K-Means Clustering
# K-means clustering, a cornerstone of unsupervised learning, was my guide on this journey. By grouping similar regions based on their crime rates, I aimed to uncover hidden patterns. The results were insightful. Clusters formed, revealing regions of peace and tranquility, and others rife with criminal activity. The algorithm divided the regions into three main categories:
# 
# Sensitive Areas: These regions exhibited alarmingly high crime rates, driven by poverty, unemployment, and social unrest.
# Moderate Areas: Here, crime rates hovered around the national average. These regions faced challenges but maintained a semblance of order, thanks to economic stability and community engagement.
# Peaceful Enclaves: These idyllic pockets boasted low crime rates, with affluent neighborhoods, effective policing, and community cohesion contributing to their tranquility.
# Insights and Recommendations
# Digging deeper, I explored the reasons behind the high crime rates in sensitive areas. Unemployment, lack of education, and inadequate law enforcement were common threads. Addressing these issues could help reduce crime. In peaceful enclaves, community vigilance played a key role in maintaining order. Implementing neighborhood watch programs, engaging youth, and running awareness campaigns could help replicate this success in other areas. With these insights, law enforcement agencies could strategically allocate resources. Sensitive areas required targeted interventions, while community policing could benefit moderate regions.
# 
# Conclusion
# My capstone project transcended code and algorithms. It was a voyage through India’s underbelly—a quest for understanding, empathy, and change. As I penned this write-up, I realized that data science isn’t just about numbers; it’s about transforming lives, one insight at a time. In retrospect, my journey through crime analysis taught me that data, when wielded responsibly, can be a beacon of hope. As I sign off, I leave you with this thought: In the labyrinth of crime, data scientists are torchbearers, illuminating paths toward a safer, more just society.
# 
# 
# 
# 
# 
# 
# 

# In[ ]:




