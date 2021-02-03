from functools import singledispatch
from collections import abc
import numbers
import html

# 函数重载
# ❶ @singledispatch 标记处理 object 类型的基函数。
# ❷ 各个专门函数使用 @«base_function».register(«type») 装饰。
# ❸ 专门函数的名称无关紧要；_ 是个不错的选择，简单明了。
# ❹ 为每个需要特殊处理的类型注册一个函数。numbers.Integral 是 int 的虚拟超类。
# ❺ 可以叠放多个 register 装饰器，让同一个函数支持不同类型。

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n): return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'

if __name__ == "__main__":
    print(htmlize({1, 2, 3}))
    print(htmlize("hello"))
    print(htmlize(100))
    print(htmlize((1,2,3)))

# singledispatch 机制的一个显著特征是，你可以在系统的任何地方和 任何模块中注册专门函数。
# 如果后来在新的模块中定义了新的类型，可 以轻松地添加一个新的专门函数来处理那个类型。
# 此外，你还可以为不 是自己编写的或者不能修改的类添加自定义函数。