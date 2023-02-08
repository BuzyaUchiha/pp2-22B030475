"""#task1
class St:
    def __init__(self, name):
        self.name = name
    def getString(self, name):
        self.name = name
    def printString(name):
        print(name.upper())
n = input()
x = St(n)
print(x)
"""
"""#task2
class Shape:
    def area(self, length:int):
        self.length = length
        length = 0
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length**2)
n = int(input())
x = Square(n)
x.area()"""

"""#task3
class Shape:
    def area(self, length:int, width:int):
        self.length = length
        self.width = width
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)
n = int(input())
m = int(input())
x = Rectangle(n,m)
x.area()"""

"""#task4
import math   
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = abs(other.x - self.x)
        dy = abs(other.y - self.y)

        return math.sqrt(dx * dx + dy * dy)

    
    def __str__(self):
        return f'Point (x = {self.x}, y = {self.y})'

point1 = Point(10, 4)
print(point1)
print(point1.get_x())
print(point1.get_y())
point1.move(10, 1)
print(point1)
point2 = Point(6,7)
print(point1.dist(point2))
"""
"""#task5
class Account:
    def __init__(self, owner:str, balance:int):
        self.owner = owner
        self.balance = balance
    def deposit(self,balance:int):
        self.balance += balance
        print(f'Your balance: {balance}')
    def withdraw(self, withdraw_amount:int):
        self.balance = balance
        self.withdraw_amount = withdraw_amount
        if self.balance >= self.withdraw_amount:
         balance = self.balance - self.withdraw_amount
         print(f'Your balance after withdrawal: {balance}')
        else:
            print('You can`t withdraw')
x = input()
y = int(input())
w = int(input())
print(Account.deposit(y), Account.withdraw(w))
"""
#task6
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers=[]
n = int(input())
lists = list(map(float,input().strip().split()))[:n]
print(is_prime(lists))
"""
