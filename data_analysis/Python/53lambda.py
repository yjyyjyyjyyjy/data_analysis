# Press the green button in the gutter to run the script.
# list[param1:param2:param3]
#
# param1，相当于start_index，可以为空，默认是0
# param2，相当于end_index，可以为空，默认是list.size
# param3，步长，默认为1。步长为-1时，返回倒序原序列
if __name__ == '__main__':
    fruits=["apple", "cherry", "peal", "strawberry"]
    print(sorted(fruits, key=(lambda x: x[::-1])))
    print(fruits)
