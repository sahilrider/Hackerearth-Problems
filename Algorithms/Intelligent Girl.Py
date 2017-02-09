'''https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/intelligent-girl-1/'''

s=input()

mem={}
count=0
for i in range(len(s)-1,-1,-1):
    if int(s[i])%2==0:
        count+=1
        mem[i]=count
    else:
        mem[i]=count
m=max(mem.values())
for i in mem.values():
    print(i,end=' ')
