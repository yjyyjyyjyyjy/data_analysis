import pandas as pd

# concatenate
if __name__ == "__main__":
    df1 = pd.DataFrame(
        {
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        },
        index=[0, 1, 2, 3],
    )

    df2 = pd.DataFrame(
        {
            "A": ["A4", "A5", "A6", "A7"],
            "B": ["B4", "B5", "B6", "B7"],
            "C": ["C4", "C5", "C6", "C7"],
            "D": ["D4", "D5", "D6", "D7"],
        },
        index=[4, 5, 6, 7],
    )

    frames = [df1, df2]
    result = pd.concat(frames)
    print("---按行组合 1 和 2---")
    print(result)

    print("---按行组合 1 和 2 增加索引---")
    result = pd.concat(frames, keys=["x", "y"])

    print("---按列组合 1 和 2 index 不同---")
    result = pd.concat(frames, axis=1)
    print(result)
    df2.index = [0, 1, 2, 3]

    print("---按列组合 1 和 2 index 相同---")
    result = pd.concat(frames, axis=1)
    print(result)

    print("---按列组合 1 和 2 index 不同 交集组合---")
    df2.index = [1, 2, 3, 4]

    result = pd.concat(frames, axis=1, join="inner")
    print("---按列组合 1 和 2 index 不同 并集组合---")
    result = pd.concat(frames, axis=1, join="outer")
    print(result)

    print("---按行组合 1 和 2 index 不同 并集组合---")
    print(pd.concat(frames, axis=0, ignore_index=True, sort=False))
