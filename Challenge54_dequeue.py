'''
Created on 12-Sep-2019

@author: Neha.Hande
'''
from collections import deque

d= deque()
for _ in range(int(input())):
    method , *args = input().split()
    getattr(d, method)(*args)
    
print(*d)
'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft
'''