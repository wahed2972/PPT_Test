def unique(s):
    
    char_count = {}
    
    for i in s:
        char_count[i] = char_count.get(i,0) + 1
        
    for i , c in enumerate(s):
        if char_count[c] == 1:
            return i
    
    return -1

s = "leetcode"
# s = "aabb"
a = unique(s)
print(a)