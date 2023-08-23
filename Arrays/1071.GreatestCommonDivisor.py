def gcdOfStrings(str1: str, str2: str):
    str1 = set(str1)
    str2 = set(str2)
    
    res1 = []
    res2 = []
    
    str3=""
    str4=""

    
    for char in str1:
        res1.append(char)
        
    for char in str2:
        res2.append(char)
        
    res1.sort()
    res2.sort()
    
    for char in res1:
        str3 += char
        
    for char in res2:
        str4 += char
    
    if str3 in str4:
        return str3
    else:
        return '""'
 
 
print(gcdOfStrings("LEET", "CODE"))
print(gcdOfStrings("ABCABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "AB"))
