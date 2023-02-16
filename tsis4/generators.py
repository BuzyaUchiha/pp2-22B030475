#task1
"""
def square_generator(N):
    for i in range(1, N+1):
        yield i**2

for square in square_generator(int(input())):
    print(square)
    """
#task2
"""
def even_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = even_generator(n)

print(','.join(map(str, even_nums)))
"""
#task3
"""
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in divisible_by_3_and_4(int(input())):
    print(num)
"""
#task4
"""
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
for square in squares(int(input()), int(input())):
    print(square)
"""
#task5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
for num in countdown(int(input())):
    print(num)


