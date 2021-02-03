
# !/usr/bin/python
# -*- coding: UTF-8 -*-
def fab_a(max):
    """
    >>> fab_a(5)
    1
    1
    2
    3
    5
    """
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

def fab_b(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b      # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1

if __name__ == "__main__":
    fab_a(5)
    for n in fab_b(5):
        print(n)
    import doctest
    doctest.testmod(verbose=True)
#
# def read_file(fpath):
#     BLOCK_SIZE = 1024
#     with open(fpath, 'rb') as f:
#         while True:
#             block = f.read(BLOCK_SIZE)
#             if block:
#                 yield block
#             else:
#                 return