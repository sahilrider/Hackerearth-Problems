'''https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/my-girlfriend-and-her-love-for-cats-1/'''


n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))
s.sort()
c.sort()
sum=0
for i in range(n):
    sum+=s[i]*c[i]
print(sum)
