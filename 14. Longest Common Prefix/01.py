# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
# Input: strs = ["dog", "racecar", "car"]
# Output: ""


strs = ["flower", "flow", "flight", 'lf']


def min_strs(strs):
    min_str = len(strs[0])
    for i in strs:
        if len(i) <= min_str:
            min_str = len(i)
    return min_str


print(min_strs(strs))

# pef = ''
#
# while True:
#     con = 0
#     for i in strs:

print(strs[0][0])

# def longestCommonPrefix(strs):
#     pref = strs[0]
#     print(pref)
#     pref_len = len(pref)
#     print(pref_len)
#     print(strs[1:])
#     for s in strs[1:]:
#         while pref != s[0:pref_len]:
#             pref_len -= 1
#             if pref_len == 0:
#                 return ""
#
#             pref = pref[0:pref_len]
#
#     return pref
#
# print(longestCommonPrefix(strs))