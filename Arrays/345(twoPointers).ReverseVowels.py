def reverseVowels(string:str) -> str:
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    string = list(string)
    l = 0
    r = len(string) - 1

    while (l < r):
        if string[l] not in vowels:
            l += 1
        elif string[r] not in vowels:
            r -= 1
        else:
            string[l], string[r] = string[r], string[l]
            l += 1
            r -= 1
        
    return "".join(string)


# Runtime 60ms Beats 68.86%
# Memory 17.4MB Beats 69.65%
