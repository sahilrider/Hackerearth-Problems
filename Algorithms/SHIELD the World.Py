'''https://www.hackerearth.com/problem/algorithm/shield-the-world/'''

def printf(d):
    for key,freq in d.items():
        if ord(key)-96 != freq:
            #print(ord(key)-96,freq)
            print('S.H.I.E.L.D')
            return
    print('HYDRA')
    return

t=int(input())
for i in range(t):
    s=input()
    d={}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1
    printf(d)
