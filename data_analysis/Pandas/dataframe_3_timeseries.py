import pandas as pd
import numpy as np

# 时间序列
if __name__ == "__main__":
    index = pd.date_range("1/1/2000", periods=8)
    df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
    print(df)
    print("---切片前两行---")
    print(df[:2])

    print("---列A（包含index）---")
    print(df["A"])
    print(df.loc[:, "A"])  # 使用了索引

    print("---都减掉第一行数据---")
    row = df.iloc[1]
    r = df.sub(row, axis="columns")
    print(r)

    print("---都减掉第二列数据---")
    column = df["B"]
    r = df.sub(column, axis="index")
    print(r)
    print(r.describe())