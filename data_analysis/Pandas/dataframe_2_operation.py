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


columns_map = {"name": "Name", "id": "ID", "age": "Age"}

index_map = {0: 3, 1: 5}


def test(file_name):
    # sep: consider space on both side of ,
    df = pd.read_csv(file_name, sep="\s*,\s*")
    print("---row and column ---")
    print(df.shape)

    print("---output columns name ---")
    print(df.columns.tolist())

    print("---type of column ---")
    print(df.dtypes)

    print("---memory---")
    print(df.memory_usage())

    # type in python is object:
    print("---memory of 12 ---")
    print(sys.getsizeof(12))

    print("---get column age data---")
    print(df["age"])

    print("---output head and tail---")
    print(df.head(1))
    print(df.tail(1))

    print("---output line 1 by index---")
    print(df.loc[1])

    print("---get sub dataframe---")
    print(df.iloc[:, 0:2:])
    # ------------------------------------------------
    # 聚合：分割-应用-组合
    columns_mean_list = ["age", "salary"]
    print("---按照部门统计年龄和薪水的均值---")
    print(df.groupby("department")[columns_mean_list].mean())

    # value_counts() is Series 统计函数，应用到df要使用apply
    print("---按部门统计人数---")
    print(df["department"].value_counts())

    print("---几个部门---")
    print(df["department"].nunique())

    print("---列名变大写---")
    df.rename(mapper=columns_map, axis='columns', inplace=True)
    print(df)

    print("---改变索引值 0->3 1->5---")
    df.rename(index=index_map, inplace=True)
    print(df)
    # ------------------------------------------------------
    # 图 plot(x, y, ls='-', lw=2, label='cosine', color='purple')
    # print(df.groupby("age")["salary"].mean())
    # df.groupby("age")["salary"].mean().plot()
    # plt.show()
    return


if __name__ == '__main__':
    file = u"data.csv"
    if not Path(file).exists():
        print("input file error: " + file)
    test(file)
