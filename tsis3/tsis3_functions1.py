#task1
"""
def grams_to_ounces(grams):
    ounces=grams*28.3495231
    return ounces
grams=int(input())
ounces=grams_to_ounces(grams)
print(grams, "is equal to ",ounces, "ounces")
"""
#task2
"""
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
fahrenheit = float(input())
celsius = fahrenheit_to_celsius(fahrenheit)
print(fahrenheit, "°F is equal to", celsius, "°C")
"""
#task3
"""
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2) + (rabbits * 4) == numlegs:
            return chickens, rabbits
    return None, None
numheads = int(input("Number of numheads: "))
numlegs = int(input("Number of numlegs: "))
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None:
    print("There are", chickens, "chickens and", rabbits, "rabbits.")
else:
    print("There is no solution for this puzzle.")
"""
#task4
"""
def prime(lists):
    for number in lists:
        check = True
        for i in range(2,int(number/2)):
            if number % i == 0:
                check = False
        if check and number != 4 and number != 1:
            prime_numbers.append(number)
    return prime_numbers
prime_numbers=[]
lists = list(map(float,input().strip().split()))
print(prime(lists))
"""

#task5
"""
def permutations(data, i, length):
    if i == length:
        print("".join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permutations(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

def print_permutations(string):
    permutations(list(string), 0, len(string))

string = input()
print_permutations(string)

"""
#task6
"""
def reverses(string):
    new_string = " h"
    lists = list(string)
    lists.reverse()
    for i in lists:
        new_string.format(i)
    return new_string
lists = []
string = str(input())
print(reverses(string))
"""
#task7
"""
def dublicates(lists):
    a = 0
    for i in range(len(lists) -1):
        if lists[i] == lists[i+1] and lists[i] == 3:
            a += 1
    tf = ""
    if a >= 1:
        tf = "True"
    else:
        tf = "False"
        
number = int(input())
lists = list(map(int,input().strip().split()))
print(dublicates)
"""
#task8
"""
def agent(lists):
    zero = 0
    seven = 0
    booler = True
    for i in range(len(lists)):
        if seven != 1 and zero < 3:
            if lists[i] == 0:
                zero += 1
            elif lists [i] == 7:
                seven += 1
        elif (seven == 1 and zero == 2):
            break
        else:
            booler = False
            break
    return booler
n = int(input())
lists = list(map(int,input().strip().split())) [:n]
print(agent(lists))

def spy_game(list):
    che = True
    for i in range(len(list)):
        if list[i] == 7:
            che = True
        elif list[i] == 0:
            che = False
    return che

n = int(input())
list = list(map(int,input().strip().split()))[:n]
print(spy_game(list))
"""
#task9
"""
def volume(radius):
    p = 3.14
    vol = float(4/3 * p *radius*radius*radius)
    return vol
radius = int(input())
print(volume(radius)) 
"""
#task10
"""
def unique(list):
    i = 0
    while i < len(list):
        j = 0
        while j < len(list):
            if list[i] == list[j] and i!=j:
                list.pop(j)
            j += 1
        i += 1
    return list
n = int(input())
list = list(map(str,input().strip().split()))[:n]
print (unique(list))
"""
#task11
"""
def polindrome(string):
    left = string[0:int(len(string) / 2)]
    right = string[int(len(string)/2 + 1):len(string)]
    if left[len(left)::-1] == right:
        return True
    else:
        return False
string = str(input())
print(polindrome(string))
"""
#task12
"""
def histogram(list):
    histo = ""
    for i in range(len(list)):
        if i == 0:
            histo += "*"*list[i]
        else:
            histo += "\n" + "*"*list[i]
    return histo
n = int(input())
list = list(map(int,input().strip().split()))[:n]
print (histogram(list))
"""
#task13
import random

random_n = random.randrange(1,20)
nog = 0

name = (input("Hello! What is your name?" + "\n"))
print ("\n")
print(f'Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess')
while True:
    nog += 1
    nop = int(input())
    print("\n")
    if nop == random_n:
        print(f'Good job, {name}! You guessed my number in {nog} guesses!')
        break
    elif nop < random_n:
        print ("Your guess is too low. \nTake a guess")
        continue
    else:
        print ("Your guess is too high. \nTake a guess")
        continue
        

