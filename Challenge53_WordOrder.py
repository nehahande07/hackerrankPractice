'''
Created on 12-Sep-2019

@author: Neha.Hande
'''
from collections import OrderedDict


d= OrderedDict()
for _ in range(int(input())):
    word = input()
    d.setdefault(word, 0)
    d[word] +=1
print(len(d))
print(*d.values())
'''
Test against input
4
bcdef
abcdefg
bcde
bcdef
'''