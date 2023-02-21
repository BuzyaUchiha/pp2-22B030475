#task1
import re
str=input()
def test1(str):
    if re.search('a(b*)',str):
        print("Yes")
    else:
        print("No")
test1(str)
#task2
import re
str=input()
def test1(str):
    if re.search('a(b*){2,3}',str):
        print("Yes")
    else:
        print("No")
test1(str)
#task3
import re
str=input()
def low_und(str):
    pat=r'[a-z]+_[a-z]+\b'
    str1=re.findall(pat,str)
    return str1
print(low_und(str))
#task4
import re
str=input()
def sequ(str):
    pat=r'[A-Z][a-z]+'
    str1=re.findall(pat,str)
    return str1
print(sequ(str))
#task5
import re
str=input()
def test2(str):
    if re.search('a()b$',str):
        print("Yes")
    else:
        print("No")
test2(str)
#task6
import re
str=input()
pat='\s+'
pat1='\,'
pat2='\.'
rep=':'
str1=re.sub(pat,rep,str)
str2=re.sub(pat1,rep,str1)
str3=re.sub(pat2,rep,str2)
print(str3)
#task7
import re
str=input()
def snaketocamel(str):
    res=''.join(x.capitalize() or '_' for x in str.split('_'))
    print(res)
snaketocamel(str)
#task8
import re
str=input()
def split(str):
    str1=re.findall('[A-Z][^A-Z]*',str)
    return ' '.join(str1)
print(split(str))
#task9
import re
str=input()
def insertsp(str):
    str1=re.sub(r'(?<!^)(?=[A-Z])', " ",str)
    print(str1)
insertsp(str)
#task10
import re
str=input()
def cameltosnake(str):
    str1=re.sub(r'(?<!^)(?=[A-Z])', "_",str).lower()
    print(str1)
cameltosnake(str)