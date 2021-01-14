class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print('walk')


class Fish(Animal):

    def swim(self):
        print('swim')


m = Mammal()
print(m.age)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
