def romanToInt(s: str) -> int:
    res = 0
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for a in range(len(s)):
        if a == len(s)-1:
            res += roman.get(s[a])
        elif roman.get(s[a]) < roman.get(s[a+1]):
            res -= roman.get(s[a])
        else:
            res += roman.get(s[a])
    return res
    #     if roman.get(a) > roman.get(int(a)+1):
    #         res += roman.get(a)
    #     else: res -= roman.get(a)
    # return res

print(romanToInt('MCMXCIV'))