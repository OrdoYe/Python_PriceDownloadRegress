#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas_datareader


# In[45]:


import pandas_datareader.data as dtr


# In[46]:


tickers = ['fb','aapl','amzn','nflx','goog','^gspc']


# In[47]:


D = dtr.DataReader(tickers,'yahoo')


# In[48]:


type(D)


# In[49]:


D.tail()


# In[50]:


P = D['Adj Close']


# In[51]:


P.tail()


# In[52]:


Returns = P / P.shift(1) - 1


# In[53]:


Returns.head()


# In[54]:


R = P.pct_change()


# In[55]:


R.tail()


# In[56]:


R.head()


# In[57]:


R2 = R.tail(100)


# In[58]:


R2.columns


# In[59]:


R2.rename(columns = {'^gspc':'SnP'},inplace=True)


# In[60]:


R2.tail()


# In[61]:


import numpy as np


# In[62]:


import matplotlib.pyplot as plt


# In[37]:


pip install --upgrade --no-deps statsmodels


# In[39]:


pip install patsy


# In[68]:


import statsmodels.formula.api as sm


# In[71]:


results = sm.ols(formula = 'fb ~ SnP', data=R2).fit()


# In[72]:


results.params


# In[76]:


mystocks = R.columns[:5]


# In[77]:


mystocks


# In[78]:


type(mystocks)


# In[83]:


betalist = []

for mystock in mystocks:
    myformula = mystock + " ~ SnP"
    print(myformula)
    results = sm.ols(formula = myformula, data=R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])


# In[85]:


betalist


# In[86]:


betavec = np.array(betalist)


# In[87]:


notional = 100
notional * betavec


# In[88]:


sum(notional + betavec)


# In[ ]:




