'''
Created on 12-Sep-2019

@author: Neha.Hande
'''
from collections import namedtuple

(n, categories) = (int(input()),input().split())
row = namedtuple('Student', categories)
marks = [int(row._make(input().split()).MARKS) for i in range(n)]
print(sum(marks)/len(marks))

'''
Try with this input
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
'''