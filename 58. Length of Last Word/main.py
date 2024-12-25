def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])

a = '   fly me   to   the moon  '


print(lengthOfLastWord(a))