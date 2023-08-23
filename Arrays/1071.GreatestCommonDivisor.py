def gcdOfStrings(str1: str, str2: str):
    str1 = set(str1)
    str2 = set(str2)
    
    arr1 = []
    arr2 = []
    
    str3 = ""
    str4 = ""
    
    for char in str1:
        arr1.append(char)
        
    for char in str2:
        arr2.append(char)
        
    arr1.sort()
    arr2.sort()
    
    for char in arr1:
        str3 += char
        
    for char in arr2:
        str4 += char
    
    if str3 in str4:
        return str3
    else:
        return 'crud'
 
 
# print(gcdOfStrings("LEET", "CODE"))
print(gcdOfStrings("ABCABC", "ABC"))
# print(gcdOfStrings("ABABAB", "AB"))
