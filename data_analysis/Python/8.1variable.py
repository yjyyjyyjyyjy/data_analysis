if __name__ == "__main__":
    # 标识
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    # 别名
    lewis = charles
    print(lewis is charles)
    print(lewis == charles)

    print(id(charles))
    print(id(lewis))

    lewis['balance'] = 950
    print(charles)

    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    # is 比较对象的标识-对象 对象 对象
    print(alex is charles)
    # == 运算符比较两个对象的值（对象中保存的数据）
    print(alex == charles)