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
        
    while " " in words:
        words.remove(" ")
        
    return "".join(words[::-1]).strip()

    
# Runtime 109ms Beats 5.40% of users with Python3
# Memory 16.30MB Beats 97.91% of users with Python3
