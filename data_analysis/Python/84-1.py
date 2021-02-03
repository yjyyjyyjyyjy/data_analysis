class HauntedBus:
    """备受幽灵乘客折磨的校车"""

    # 如果没传入 passengers 参数，使用默认绑定的列表对象，一开始 是空列表。
    # 这个赋值语句把 self.passengers 变成 passengers 的别名，
    # 而没有传入 passengers 参数时，后者又是默认列表的别名。-- 导致默认列表 和 输入列表是两个列表
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    # 在 self.passengers 上调用 .remove() 和 .append() 方法时，修 改的其实是默认列表，它是函数对象的一个属性
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == "__main__":
    bus1 = HauntedBus(['Alice', 'Bill'])
    bus1.pick('Charlie')
    bus1.drop('Alice')
    print("BUS1: {0}".format(bus1.passengers))

    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print("BUS2: {0}".format(bus2.passengers))
    print(HauntedBus.__init__.__defaults__)
    bus3 = HauntedBus()
    bus3.pick('Dave')

    print("BUS3: {0}".format(bus3.passengers))

    print(bus2.passengers is bus3.passengers)
    print(HauntedBus.__init__.__defaults__)
    print("BUS1: {0}".format(bus1.passengers))
# BUS1: ['Bill', 'Charlie']
# BUS2: ['Carrie']
# (['Carrie'],)
# BUS3: ['Carrie', 'Dave']
# True
# (['Carrie', 'Dave'],)
# BUS1: ['Bill', 'Charlie']