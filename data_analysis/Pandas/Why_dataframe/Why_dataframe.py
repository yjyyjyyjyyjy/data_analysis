# coding = 'utf-8'
import numpy as np
import pandas as pd
import time
import functools
import random


# functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0  # 用时
        name = func.__name__

        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))

        arg_str = ', '.join(arg_lst)

        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


@clock
def use_dataframe(num):
    y = np.random.randint(2, size=(num, 1))
    pd.DataFrame(y).apply(lambda x: x * 2 + 7)


@clock
def use_loop(num):
    y = [random.randint(0, 2) for i in range(num)]
    for item in y:
        item * 2 + 7


def main():

    # count = 1000
    # use_loop(count)
    # use_dataframe(count)

    # count = 10000
    # use_loop(count)
    # use_dataframe(count)

    count = 1000000
    use_loop(count)
    use_dataframe(count)


if __name__ == '__main__':
    main()
