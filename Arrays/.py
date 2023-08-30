s = "a good   example"
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
# print(words)

# if " " in words:
#     words.remove(" ")

while " " in words:
    words.remove(" ")

# print(words)
        
print("".join(words[::-1]).strip())
