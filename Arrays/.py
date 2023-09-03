def longestPrefix(strs: list) -> str:
    l = 0
    r = len(strs) - 1
    
    prefix = strs[0]
    currentPrefix = "" 
    
    while l != r:
        for i in range(len(prefix)):
            if prefix[i] == strs[r][i]:
                currentPrefix += prefix[i]
            else:
                break
            
        prefix = currentPrefix
        currentPrefix = ""
        r -= 1
        
        
    return prefix


print(longestPrefix(["flower","flight","flow"]))
            
     