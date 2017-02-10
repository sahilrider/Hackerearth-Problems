'''https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-best-internet-browser-3/description/'''


vowels=['a','e','i','o','u']
t=int(input())
for i in range(t):
    s=list(input().split('.'))
    l=len(s[0])+len(s[1])+len(s[2])+2
    num=0
    #print(s,l)
    for j in s[1]:
        #print(j)
        if j not in vowels:
            num+=1
    print('%d/%d'%(num+4,l))
