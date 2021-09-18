pip install pandas_datareader
pip install --upgrade --no-deps statsmodels
pip install patsy

import pandas_datareader.data as dtr
import numpy as np
import statsmodels.formula.api as sm

tickers = ['msft','tsla','nvda','pypl','pep','^gspc']
D = dtr.DataReader(tickers,'yahoo')
type(D)
D.tail()

P = D['Adj Close']
P.tail()

Returns = P / P.shift(1) - 1
Returns.tail()

R = P.pct_change()
R.tail()

R2 = R.tail(100)
R2.columns
R2.rename(columns = {'^gspc':'SnP'},inplace=True)
R2.tail()

results1 = sm.ols(formula = 'msft ~ SnP', data=R2).fit()
results1.params
results2 = sm.ols(formula = 'tsla ~ SnP', data=R2).fit()
results2.params
results3 = sm.ols(formula = 'nvda ~ SnP', data=R2).fit()
results3.params
results4 = sm.ols(formula = 'pvpl ~ SnP', data=R2).fit()
results4.params
results5 = sm.ols(formula = 'pep ~ SnP', data=R2).fit()
results5.params

mystocks = R.columns[:5]
mystocks
type(mystocks)

betalist = []
for mystock in mystocks:
    myformula = mystock + " ~ SnP"
    print(myformula)
    results = sm.ols(formula = myformula, data=R2).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])
betalist

betavec = np.array(betalist)
notional = 100
notional * betavec
sum(notional + betavec)
