import pandas as pd


def test():
    d = {"b": 1, "a": 0, "c": 2}
    print("---字典构造数组---")
    d = pd.Series(d)
    print(d)

    print("---字典方式检查 index---")
    print("c" in d)

    print("---添加另一个数组---")
    b = pd.Series({"d": 3})
    f = d.append(b)
    print(f)

    print("---自定义索引---")
    s = pd.Series(5.0, index=["a", "b", "c", "d", "e"])
    print(s)

    print("---数组下标使用---")
    print(s[0])
    print(s[1])
    print(s["a"])

    print("---使用数学计算函数---")
    print(s.median())


if __name__ == '__main__':
    test()
