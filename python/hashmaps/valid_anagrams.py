def is_anagram(s,t):
    if len(s) != len(t):
        return False
    
    count = {} #dictionary to count characters in s
    
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]

    return len(count) == 0
    