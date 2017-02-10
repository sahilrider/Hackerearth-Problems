'''https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-reversed-numbers/description/'''

t=int(input())
for i in range(t):
    s1,s2=input().split()
    s1=s1[::-1]
    s2=s2[::-1]
    s3=int(s1)+int(s2)
    s3=str(s3)[::-1]
    print(int(s3))
