import pandas as pd

if __name__ == "__main__":
    print("--------------From Series-------------")
    d = {"one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
         "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"])}
    df = pd.DataFrame(d)
    print(df)

    print("--------------From dict-------------")
    d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
    df = pd.DataFrame(d)
    print(df)

    print("--------------Add index-------------")
    df = pd.DataFrame(d, index=["a", "b", "c", "d"])
    print(df)

    print("--------------From tuple 二级目录-------------")
    t = pd.DataFrame(
        {
            ("a", "b"): {("A", "B"): 1, ("A", "C"): 2},
            ("a", "a"): {("A", "C"): 3, ("A", "B"): 4},
            ("a", "c"): {("A", "B"): 5, ("A", "C"): 6},
            ("b", "a"): {("A", "C"): 7, ("A", "B"): 8},
            ("b", "b"): {("A", "D"): 9, ("A", "B"): 10},
        }
    )
    print(t)
