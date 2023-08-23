def gcdOfStrings(str1: str, str2: str):
    str1 = set(str1)
    str2 = set(str2)
    
    res1 = ""
    res2 = ""

    for char in str1:
        res1 += char
        
    for char in str2:
        res2 += char
        
    if res1 in res2:
        print(res1)
    else:
        print("")
 
 
print(gcdOfStrings("ABCABC", "ABC"))