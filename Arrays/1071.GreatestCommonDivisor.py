def gcdOfStrings(str1: str, str2: str):
    str1 = set(str1)
    str2 = set(str2)
    
    arr1 = []
    arr2 = []
    
    str1 = ""
    str2 = ""
    
    for char in str1:
        arr1.append(char)
        
    for char in str2:
        arr2.append(char)
        
    arr1.sort()
    arr2.sort()
    
    for char in arr1:
        str1 += char
        
    for char in arr2:
        str2 += char
    
    if str1 in str2:
        return str1
    else:
        return '""'
 
 
print(gcdOfStrings("LEET", "CODE"))
print(gcdOfStrings("ABCABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "AB"))
