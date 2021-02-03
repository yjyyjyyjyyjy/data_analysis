# df：任意的Pandas DataFrame对象【比如pd的返回值】
# s：任意的Pandas Series对象
#
# df.head(n)：查看DataFrame对象的前n行
# df.tail(n)：查看DataFrame对象的最后n行
# df.shape()：查看行数和列数
# df.info()：查看索引、数据类型和内存信息
# df.describe()：查看数值型列的汇总统计 s.
# s.value_counts(dropna=False)：查看Series对象的唯一值和计数
# df.apply(pd.Series.value_counts)：查看DataFrame对象中每一列的唯一值和计数