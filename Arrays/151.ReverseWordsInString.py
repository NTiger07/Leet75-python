def reverseWords(s: str) -> str:
    words = []

    l = 0
    r = 0
    s = s + " "
    while r < len(s):
        if s[r] == " ":
            words.append(s[l:r+1])
            l = r + 1
            r += 1

        elif s[r] != " ":
            r += 1
        
    if " " in words:
        words.remove(" ")
        
    return "".join(words[::-1]).strip()

    
print(reverseWords("the sky is blue"))
print(reverseWords(" hello world "))
print(reverseWords("a good  example"))