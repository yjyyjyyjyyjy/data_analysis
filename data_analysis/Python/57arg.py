# *arg and **kwarg
# *args：可以理解为长度不固定的列表。
# **kwarg：可以理解为长度不固定的字典
import collections


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    # **kwarg
    if attrs:
        attr_str = "".join('%s="%s"' % (attr, value) for attr, value in attrs.items())
    else:
        attr_str = ''
    # *arg
    if content:
        return '\n'.join('<%s %s>%s<%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    # only name
    print(tag('br'))
    print("----------------")
    # name and content
    print(tag('p', 'hello'))
    print("----------------")
    # name and content * arg
    print(tag('p', 'hello', 'world'))
    print("----------------")
    # name content
    # content = ('hello', 'id=33')
    print(tag('p', 'hello', 'id=33'))
    print(tag('p', 'hello', id=33))
    print("----------------")
    # name content and class attr
    attr = collections.OrderedDict()
    attr['id'] = 33
    attr['num'] = 55

    print(tag('p', 'hello', **attr))
    print("----------------")
    print(tag('p', 'hello', **{'id': 33, 'num': 55}, cls="sidebar"))
