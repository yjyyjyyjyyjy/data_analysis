# coding = 'utf-8'
import numpy as np
import pandas as pd
import time
import functools


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
# [1.52472639s]
def target_mean_v1(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    for i in range(data.shape[0]):
        groupby_result = data[data.index != i].groupby([x_name], as_index=False).agg(['mean', 'count'])
        result[i] = groupby_result.loc[groupby_result.index == data.loc[i, x_name], (y_name, 'mean')]
    return result

@clock
# [0.01883936s]
def target_mean_v2(data, y_name, x_name):
    result = np.zeros(data.shape[0])
    value_dict = dict()
    count_dict = dict()
    for i in range(data.shape[0]):
        if data.loc[i, x_name] not in value_dict.keys():
            value_dict[data.loc[i, x_name]] = data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] = 1
        else:
            value_dict[data.loc[i, x_name]] += data.loc[i, y_name]
            count_dict[data.loc[i, x_name]] += 1
    for i in range(data.shape[0]):
        result[i] = (value_dict[data.loc[i, x_name]] - data.loc[i, y_name]) / (count_dict[data.loc[i, x_name]] - 1)
    return result


def main():
    # [0,2) 范围的随机数 二维 5000,1
    y = np.random.randint(2, size=(500, 1))
    # [0,2) 范围的随机数 二维 5000,1
    x = np.random.randint(10, size=(500, 1))
    # data 5000 行 2 列
    data = pd.DataFrame(np.concatenate([y, x], axis=1), columns=['y', 'x'])
    result_1 = target_mean_v1(data, 'y', 'x')
    result_2 = target_mean_v2(data, 'y', 'x')
    # 线性代数函数
    diff = np.linalg.norm(result_1 - result_2)
    print(diff)


if __name__ == '__main__':
    main()