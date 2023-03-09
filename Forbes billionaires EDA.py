#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')
import re


# In[11]:


df = pd.read_csv(r"C:\Users\91879\Downloads\2022_forbes_billionaires.csv")


# In[19]:


df.head()


# In[20]:


df.info()


# In[31]:


df['networth'].replace(to_replace = '$',value='',inplace=True)


# In[27]:


df['networth'].replace(to_replace = 'B',value='',inplace=True)


# In[34]:


df['networth']=df['networth'].astype(float)


# In[37]:


df.info()


# In[119]:


databb = df['country'].value_counts()
xbb = databb.index
ybb = databb.values
fig = px.bar(df,x=xbb,y=ybb,title='No of Billionaires by Countries',
            height=500)
fig.show()


# In[130]:


fig = px.line(df.head(10), x="name", y="networth", color="country",
             hover_data=['age'],markers=True)
fig.show()


# In[121]:


datafb = df['industry'].value_counts()
xfb = datafb.index
yfb = datafb.values
fig = px.bar(datafb,x=xfb,y=yfb,title='Most no of Billionaires by Industry',height=600,color='industry')
fig.update_layout
fig.show()


# In[124]:


def barLabel(x,y):
    for i in range(len(x)):
        text = str(y[i]) + ' Billion'
        position = y[i]+(y[i]*0.1)
        plt.text(i, position, text, ha = 'center') 

def createBar(text):
    data = df[['name','networth']].loc[df['industry'] == text].head().copy()
    data = data.reset_index(drop = True)
    plt.figure(figsize = (8,5))
    plt.bar(x = data['name'], height = data['networth'], color = 'orange')
    title = 'Top 5 Rich People From '
    title = title + text
    title = title + 'industry'
    plt.title(title)
    plt.xticks(rotation = 90)
    plt.ylim(0,(data['networth'][0])+(data['networth'][0]*0.25))
    barLabel(data['name'],data['networth'])
    plt.show()    


# In[125]:


for i in range(len(df['industry'].unique())):
    text = df['industry'].unique()[i]
    createBar(text)


# In[80]:


def createBar(text):
    data = df[['name','networth']].loc[df['country'] == text].head().copy()
    data = data.reset_index(drop = True)
    plt.figure(figsize = (8,5))
    plt.bar(x = data['name'], height = data['networth'], color = 'red')
    title = 'Top 5 Rich People From '
    title = title + text
    plt.title(title)
    plt.xticks(rotation = 90)
    plt.ylim(0,(data['networth'][0])+(data['networth'][0]*0.25))
    barLabel(data['name'],data['networth'])
    plt.show()    


# In[81]:


country = df['country'].value_counts().head().index
for i in range(len(country)):
        createBar(country[i])


# In[82]:


df_age = df.sort_values(by='age',ascending=False)


# In[108]:


fig = px.bar(df_age.head(10),x='name',y='networth',title='Top 10 oldest Billionaires',
             height=500,hover_data=['age'],color='country')
fig.show()


# In[94]:


df_age1 = df.sort_values(by = 'age',ascending=True)


# In[107]:


fig = px.bar(df_age1.head(10),x='name',y='networth',color='country',
                   title='Top 10 Youngest Billionaires',height=500,
                  hover_data=['name','age'])
fig.show()


# In[103]:


fig = px.sunburst(df,path=['industry','country','name'],
                  values='networth',color='country',
                  title = 'Overall Eda by Industries',
                 color_discrete_map={'(?)':'black', 'Lunch':'gold', 'Dinner':'darkblue'},width=800,height=800)
fig.show()


# In[ ]:




