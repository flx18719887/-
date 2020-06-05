import pandas as pd
import numpy as np
# Pandas 的 Series 对象是一个带索引数据构成的一维数组
data = pd.Series(["a", "b", "c"])
print(data)
print(data.values)
print(data.index)
print(data[:2])


print("=" * 50)
# NumPy 数组通过隐式定义的整数索引获取数值
# 而 Pandas 的 Series 对象用一种显式定义的索引与数值关联
data1 = pd.Series(np.arange(10, 15), index=list("ademn"))
print(data1)
print(data1["d"])

print("=" * 50)
# 用 Python 的字典创建一个 Series 对象
md = {"a":10, "b":100, "H":23, "Q":22}
data2 = pd.Series(md)
print(data2)
print(data2["b":"H"])

print("=" * 50)
data3 = pd.Series(10, index=list("WXYZ"))
print(data3)

print("=" * 50)
data4 = pd.Series({"m":1, "n":3, "u":5}, index=["m", "u"])
print(data4)










