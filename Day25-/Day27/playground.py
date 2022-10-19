def add(*args):
    return sum(args)
    # for n in args:


num = add(5, 2, 6, 1, 3, 56, 3)
print(num)


def calc(n, **kwargs):
    # print(type(kwargs), kwargs) #dictionnary
    n += kwargs['add']
    n *= kwargs['mul']
    return n


tot = calc(3, add=3, mul=45)
print(tot)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_Car = Car(make="Nissa", model="GTR")
