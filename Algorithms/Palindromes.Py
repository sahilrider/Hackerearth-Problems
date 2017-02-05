'''https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/palindromes-3/description/'''


def check(s):
    if s[:]!=s[::-1]:
        print(len(s))
        return
    for i in range(1,len(s)):
        if s[i:]!=s[:i-1:-1]:
            print(len(s[i:]))
            return
    print('0')
    return


s=input()
check(s)
