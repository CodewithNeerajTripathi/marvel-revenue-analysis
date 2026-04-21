#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv("../data/marvel.csv", encoding='latin1')
df.head()



# 

# In[4]:


df.info()
df.isnull().sum()


# In[5]:


money_cols = ['Bud­get (mil­lions)', 'Opening weekend(North America)', 
              'North America', 'Other territories', 'Worldwide']

for col in money_cols:
    df[col] = pd.to_numeric(df[col].replace(r'[\$,]', '', regex=True), errors='coerce')

df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df['Bud­get (mil­lions)'] = df['Bud­get (mil­lions)'].fillna(
    df['Bud­get (mil­lions)'].mean()
)
df.isnull().sum()


# In[8]:


df['Release date(United States)'] = pd.to_datetime(
    df['Release date(United States)'], errors='coerce'
)
df.info()


# In[9]:


df = df.dropna(subset=['Release date(United States)'])
df.info()


# In[10]:


df['Profit'] = df['Worldwide'] - df['Bud­get (mil­lions)']
df['Year'] = df['Release date(United States)'].dt.year


# In[11]:


def category(x):
    if x < 300_000_000:
        return "Low"
    elif x <= 800_000_000:
        return "Medium"
    else:
        return "High"

df['Revenue_Category'] = df['Worldwide'].apply(category)


# In[12]:


df[['Worldwide', 'Revenue_Category', 'Profit', 'Year']].head()
df['Revenue_Category'].value_counts()
df.head()


# In[13]:


import matplotlib.pyplot as plt

df['Revenue_Category'].value_counts().plot(kind='bar')

plt.title("Movie Revenue Categories")
plt.xlabel("Category")
plt.ylabel("Number of Movies")

plt.show()


# In[ ]:





# In[14]:


df.sort_values(by='Worldwide', ascending=False).head(5)


# In[15]:


df.sort_values(by='Worldwide').head(5)


# In[ ]:


df.to_csv("../data/cleaned_marvel.csv", index=False)

