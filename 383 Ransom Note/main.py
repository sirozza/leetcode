
ransomNote = 'bg'
magazine = 'efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj'

print(set(ransomNote))

def canConstruct(ransomNote: str, magazine: str):
    a = {}
    while ransomNote != '':
        a[ransomNote[0]] = ransomNote.count(ransomNote[0])
        ransomNote = ransomNote.replace(ransomNote[0], '')
    for key, value in a.items():
        if magazine.count(key) <= value:
            return False
    return True
print(canConstruct(ransomNote, magazine))