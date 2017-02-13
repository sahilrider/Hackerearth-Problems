'''https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/count-enemies-5/'''

t=int(input())
for i in range(t):
    li=list(input().split('*'))
    ctr=0
    for j in li:
        if 'X' not in j:
            ctr+=len(j)
    print(ctr)
