# Tablewise Function Application: pipe()

# Row or Column-wise Function Application: apply()
# DataFrame.apply
# Apply a function along input axis of DataFrame.
#
# DataFrame.applymap
# Apply a function elementwise on a whole DataFrame.
#
# Series.map
# Apply a mapping correspondence on a Series.

# Aggregation API: agg() and transform()

import pandas as pd
import sys
import logging
import numpy as np
import matplotlib.pyplot  as plt
from pathlib import Path


# logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
#                     level=logging.DEBUG)
# logger = logging.getLogger()


# def log(level):
#     logger.setLevel(level)
# logger.debug("debug")
# print("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical\n")
def pipe_test1(df):
    df["年薪"] = df.loc[:, "salary"] * 12
    return df


def pipe_test2(df):
    df["奖金"] = df.loc[:, "salary"] * 0.2
    return df


def test(file_name):
    # sep: consider space on both side of ,
    df = pd.read_csv(file_name, sep="\s*,\s*")
    print("---数据---")
    print(df)

    print("---过滤年龄大于30---")
    print(df[df.age > 30])

    print("---添加列表示性别使用 apply---")
    df["性别"] = df.loc[:, "name"].apply(lambda x: "男" if "andy" in x else "女")
    print(df)

    print("---添加两列使用pipe---")
    print(pipe_test1(pipe_test2(df)))

    print("--- 月薪和使用agg---")
    print(df["salary"].agg("sum"))

    print("--- 多个函数并用使用transform---")
    tf = df["salary"].transform([np.abs, lambda x: x * 0.5])
    print(tf)

    print("--- map元素基本apply---")
    print(df["name"].map(lambda x: len(x)))

    return


if __name__ == '__main__':
    file = u"data.csv"
    if not Path(file).exists():
        print("input file error: " + file)
    test(file)
