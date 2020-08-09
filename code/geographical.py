#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
#import plotly.plotly as py
import plotly.offline as po
import plotly.graph_objs as go
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


po.init_notebook_mode(connected= True)


# In[8]:


agri= pd.read_csv('214.agri.csv')


# In[9]:


agri


# In[12]:


data= dict(type='choropleth',
        locations= ['AL','AR','AZ','CA'],
         locationmode = 'USA-states',
        z = [1,2,30,40,50],
        text= ['alabana','alaska','arizona','pugger','califonia'] 
          )


# In[23]:


layout=dict(geo={'scope':'usa'})


# In[24]:


x= go.Figure(data=[data],layout=layout)


# In[18]:


po.plot(x)


# In[46]:


po.iplot(x)


# In[41]:


data= dict(type='choropleth',
        locations=agri['code'],
         locationmode = 'USA-states',
        z = agri['total exports'],
        text=agri['text'],
         colorscale='Greens',  
        colorbar={'title':'colorbar'} )


# In[42]:


layout=dict(geo=dict(scope='usa',showlakes=True))


# In[43]:


x= go.Figure(data=[data],layout=layout)


# In[45]:


po.iplot(x)


# In[6]:


gdp= pd.read_csv('215.gdp.csv')


# In[7]:


gdp.head()


# In[8]:


data= dict(type='choropleth',
        locations=gdp['CODE'],
        z = gdp['GDP (BILLIONS)'],
        text=gdp['COUNTRY']
         )


# In[9]:


layout=dict(geo=dict(projection={'type':'hammer'}))


# In[10]:


x= go.Figure(data=[data],layout=layout)


# In[59]:


po.plot(x)


# In[11]:


po.iplot(x)


# In[ ]:




