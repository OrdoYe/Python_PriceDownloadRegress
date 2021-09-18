#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas_datareader


# In[2]:


pip install --upgrade --no-deps statsmodels


# In[3]:


pip install patsy


# In[4]:


import pandas_datareader.data as dtr


# In[5]:


import numpy as np


# In[6]:


import statsmodels.formula.api as sm


# In[7]:


tickers = ['msft','tsla','nvda','pypl','pep','^gspc']


# In[8]:


D = dtr.DataReader(tickers,'yahoo')


# In[9]:


type(D)


# In[10]:


D.tail()


# In[11]:


P = D['Adj Close']


# In[12]:


P.tail()


# In[13]:


Returns = P / P.shift(1) - 1


# In[14]:


Returns.tail()


# In[15]:


R = P.pct_change()


# In[16]:


R.tail()


# In[17]:


R2 = R.tail(100)


# In[18]:


R2.columns


# In[19]:


R2.rename(columns = {'^gspc':'SnP'},inplace=True)


# In[20]:


R2.tail()


# In[22]:


results = sm.ols(formula = 'msft ~ SnP', data=R2).fit()


# In[23]:


results.params


# In[24]:


mystocks = R.columns[:5]


# In[25]:


mystocks


# In[26]:


type(mystocks)


# In[27]:


betalist = []
for mystock in mystocks:
    myformula = mystock + " ~ SnP"
    print(myformula)
    results = sm.ols(formula = myformula, data=R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])


# In[28]:


betalist


# In[29]:


betavec = np.array(betalist)


# In[30]:


notional = 100
notional * betavec
sum(notional + betavec)


# In[ ]:




