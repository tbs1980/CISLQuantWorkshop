# example taken from http://connor-johnson.com/2014/02/18/linear-regression-with-python/
#
import numpy as np
import pandas
from pandas import DataFrame, Series
import statsmodels.formula.api as sm
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats
import matplotlib.pyplot as plt

# copy the data from http://lib.stat.cmu.edu/DASL/Stories/AlcoholandTobacco.html
#
data_str = '''Region Alcohol Tobacco
North 6.47 4.03
Yorkshire 6.13 3.76
Northeast 6.19 3.77
East-Midlands 4.89 3.34
West-Midlands 5.63 3.47
East-Anglia 4.52 2.92
Southeast 5.89 3.20
Southwest 4.79 2.71
Wales 5.27 3.53
Scotland 6.08 4.51
Northern-Ireland 4.02 4.56'''

# Each line ends in a newline, and each datum is delimited by a tab,
# so we first split the string over the newlines, and then split each new
# datum using the tabs, like this
#
d = data_str.split('\n')
d = [ i.split(' ') for i in d ]
for i in range( len( d ) ):
    for j in range( len( d[0] ) ):
        try:
            d[i][j] = float( d[i][j] )
        except:
            pass

# Finally, we wrap this data in a pandas DataFram
#
df = DataFrame( d[1:], columns=d[0] )

# save data
#df.to_csv("./alcohol_v_tobacco.csv")

# We give the DataFrame two arguments, the data, and then labels for the columns,
# taken from the first row of our list, d. This will allow us to refer to the column
# containing alcohol data as df.Alcohol.
#
plt.scatter( df.Tobacco, df.Alcohol,
         marker='o',
         edgecolor='b',
         facecolor='none',
         alpha=0.5 )
plt.xlabel('Tobacco')
plt.ylabel('Alcohol')
# save plot
#plt.savefig('alcohol_v_tobacco.png', fmt='png', dpi=100)

# To perform ordinary least squares regression on the alcohol consumption as a function of
# tobacco consumption, we enter the following code. Note that we are excluding the last datum,
# which refers to the outlying North Ireland data. We'll give an example of the data with that
# outlier later; for now, we will focus on the "cleaner" data.
#
# Since we want a linear model that looks like y = b1x+ b0 we need to add an extra array
# or vector of ones to our independent variable df.Tobacco because the statsmodels OLS()
# function does not assume that we would like a constant or intercept intercept term b0.
# This is not so uncommon as it would seem; several regression packages make this
# requirement. The summary() method produces the following human-readable output.
#
#
df['Eins'] = np.ones(( len(df), ))
Y = df.Alcohol[:-1]
X = df[['Tobacco','Eins']][:-1]
result = sm.OLS( Y, X ).fit()
print result.summary()
