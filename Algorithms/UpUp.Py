'''https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/upup/'''

import re

s=list(input().split(' '))
s2=[]
for key in s:
    key = re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), key, 1)
    s2.append(key)
print(' '.join(s2))
    
