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
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

# 这样一来，执行时间减半了，而且 n 的每个值只调用一次函数
@functools.lru_cache()
@clock
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n - 2) + fibonacci2(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
    print("remember")
    print(fibonacci2(6))
# 因为 lru_cache 使用字典存储结果，而且键根据调用时传 入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它 的所有参数都必须是可散列的。