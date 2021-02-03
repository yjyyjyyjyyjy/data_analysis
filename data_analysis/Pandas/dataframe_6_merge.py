import pandas as pd

# merge
if __name__ == "__main__":
    #
    # left = pd.DataFrame(
    #      {
    #          "key": ["K0", "K1", "K2", "K3"],
    #          "A": ["A0", "A1", "A2", "A3"],
    #          "B": ["B0", "B1", "B2", "B3"],
    #      }
    # )
    # right = pd.DataFrame(
    #      {
    #          "key": ["K0", "K1", "K2", "K3"],
    #          "C": ["C0", "C1", "C2", "C3"],
    #          "D": ["D0", "D1", "D2", "D3"],
    #      }
    #  )
    # print("---left---")
    # print(left)
    # print("---right---")
    # print(right)
    # print("---inner merge on one column key---")
    # result = pd.merge(left, right, on="key")
    # print(result)

    left = pd.DataFrame(
         {
            "key1": ["K0", "K0", "K1", "K2"],
            "key2": ["K0", "K1", "K0", "K1"],
            "A": ["A0", "A1", "A2", "A3"],
            "B": ["B0", "B1", "B2", "B3"],
        }
    )
    right = pd.DataFrame(
        {
            "key1": ["K0", "K1", "K1", "K2"],
            "key2": ["K0", "K0", "K0", "K0"],
            "C": ["C0", "C1", "C2", "C3"],
            "D": ["D0", "D1", "D2", "D3"],
        }
    )

    print("---left---")
    print(left)

    print("---right---")
    print(right)

    print("---inner merge on one two keys---")
    result = pd.merge(left, right, on=["key1", "key2"])
    print(result)

    print("---outer merge on one two keys---")
    result = pd.merge(left, right, how="outer", on=["key1", "key2"])
    print(result)

    print("---left merge on one two keys---")
    result = pd.merge(left, right,  how="left", on=["key1", "key2"])
    print(result)

    print("---right merge on one two keys---")
    result = pd.merge(left, right,  how="right", on=["key1", "key2"])
    print(result)

    print("---inner merge on one two keys---")
    result = pd.merge(left, right, validate="one_to_many", on=["key1", "key2"], indicator=True)
    print(result)