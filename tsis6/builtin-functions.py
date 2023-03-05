#task1
lst=[2, 3, 4, 5]
sum=1
for i in range(len(lst)):
    sum*=lst[i]
    i+=1
print(sum)
#task2
str=input()
def countUpLow(str):
    c1=0
    c2=0
    for i in range(0, len(str)):
        if str[i].isupper():
         c1+=1
        if str[i].islower():
         c2+=1
    print(f'Number of upper cases: {c1}')
    print(f'Number of lower cases: {c2}')
countUpLow(str)
#task3
str=input()
str1= str[::-1]
if str1==str:
    print('Palindrome')
else:
    print('Not palindrome')
#task4
import math
print('Sample Input:')
n=int(input())
time=int(input())
root=math.sqrt(n)
print('Sample Output:')
print(f'Square root of {n} after {time} miliseconds is {root}')
#task5
tup=input()
def true_tup(tup):
    return all(tup)
print(true_tup(tup))