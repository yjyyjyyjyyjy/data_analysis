# 序列相关的函数：
# len(L) 返回序列的长度
# max(L) 返回序列中的最大值
# min(L) 返回序列中的最小值
# sum(L) 返回序列的元素的和（只有数字型才可以）
# any(L) 返回布尔值，序列中有一个为真就返回True，都为假的时候才返回False
# all(L) 返回布尔值，序列中全部为真时返回True，只要有一个假就返回False
# reversed(x) 返回反向顺序的可迭代对象
# reversed(x) 不能直接使用，可以在for中使用
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )

# 截取列表
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4])
list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]


# 读取第二位
print("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print("list[1:-2]: ", list[1:-2])
list = ['Google', 'Runoob', 1997, 2000]

# 更新列表
print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

# 删除列表元素

list = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)
#
# 1	len(list)
# 列表元素个数
# 2	max(list)
# 返回列表元素最大值
# 3	min(list)
# 返回列表元素最小值
# 4	list(seq)
# 将元组转换为列表
#
# 序号	方法
# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort( key=None, reverse=False)
# 对原列表进行排序
# 10	list.clear()
# 清空列表
# 11	list.copy()
# 复制列表