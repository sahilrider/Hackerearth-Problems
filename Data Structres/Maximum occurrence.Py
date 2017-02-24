'''https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/maximum-occurrence-9/'''

s=input()
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        
k=max(d,key=d.get)
print(k,d[k])
