
class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

# 这比用类来实现更优雅，此外装饰器也是基于闭包的一中应用场景。
# 所有函数都有一个 __closure__属性，如果这个函数是一个闭包的话，
# 那么它返回的是一个由 cell 对象 组成的元组对象。
# cell 对象的cell_contents 属性就是闭包中的自由变量。

if __name__ == "__main__":
    avg = Averager()
    print(avg(10))
    print(avg(11))
    print(dir(avg))


    avg = make_averager()
    print(avg(10))
    print(avg(11))
    #函数内省
    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(dir(avg))

