'''https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/remove-duplicates-3/'''


s=input()
known=[]
for i in range(len(s)):
    if s[i] not in known:
        known.append(s[i])
print(''.join(known))
