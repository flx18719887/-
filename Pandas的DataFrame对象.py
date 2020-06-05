import numpy as np
import pandas as pd

# 如果将 Series 类比为带灵活索引的一维数组， 那么 DataFrame
# 就可以看作是一种既有灵活的行索引， 又有灵活列名的二维数组
sex = {'a':'M', 'b':'F', 'c':'F', 'd':'M'}
sex=pd.Series(sex)
mdict = {'a':10, 'b':20, 'c':30, 'd':40}
data = pd.Series(mdict)
print(data)
df = pd.DataFrame({'sex':sex, "data":data})
print(df)
print(df.index)
print(df.columns)



print("=" * 50)
data = [{'a':i, 'b':2 * i, 'c':3 * i} for i in range(3)]
df1 = pd.DataFrame(data)
print(df1)


print("=" * 50)
# 即使字典中有些键不存在， Pandas 也会用缺失值 NaN（不是数字，not a number） 来表示
df2 = pd.DataFrame([{"a":1, "b":2}, {"b":3, "c":4}])
print(df2)

print("=" * 50)
df3 = pd.DataFrame(np.random.rand(3,2))
print(df3)

print("\n")
df3_1 = pd.DataFrame(np.random.rand(4,3),
                     columns=['x', 'y', 'z'],
                     index=list('abcd'))
print(df3_1)


