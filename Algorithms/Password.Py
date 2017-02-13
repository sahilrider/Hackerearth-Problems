'''https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/password-1/'''

n=int(input())
li=[]
for i in range(n):
    s=input().strip()
    li.append(s)
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if (li[i])[::-1]==li[j]:
            (l,m)=(len(li[i]),li[i][len(li[i])//2])
print(l,m)
