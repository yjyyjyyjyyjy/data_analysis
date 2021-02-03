# 不想写lambda 的时候可以用什么呢？
#
from functools import reduce

from operator import mul, itemgetter, attrgetter


def fact_lambda(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def fact(n):
    return reduce(mul, range(1, n + 1))


metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
              ]
if __name__ == "__main__":
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))

    print(fact_lambda(3))
    print(fact(3))
    # 函数内省
    # print(dir(fact))
