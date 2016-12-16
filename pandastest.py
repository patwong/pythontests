import pandas as pd
import numpy as np

# testing numpy/pandas functionality
s = pd.Series([1,3,5,np.nan,6,8])
# print s   # prints 1d array, np.nan just like it is in matlab, also type float64

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
print type(x)   # type is 'numpy.ndarray'
# print x.shape # prints out (2L, 3L); 2x3 matrix

# unlike matlab, arrays/matrices indexed at 0
# print x[:,0]  # prints out [1 4]

dates = pd.date_range('20161130', periods=6)
#print dates     # print a datetimeindex (array, with 6 days with start date of 2016.11.30)

# index takes list as an input
# list can be initialized like:
#   a = list([1,2,...n]), b = [1, 2, ..., n]
df0 = pd.DataFrame(np.random.randn(6, 4), index=('hi','bye','why','rye','sty','shy'), columns=list('1234'))
df1 = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=('a','b','c','d'))
#print df1

df2 = pd.DataFrame({ 'A' : 1.,
                         'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
print df2

#end code
