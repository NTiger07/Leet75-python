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

Runtime
Details
109ms
Beats 5.40%of users with Python3
Memory
Details
16.30MB
Beats 97.91%of users with Python3

# print(words)
        
print("".join(words[::-1]).strip())
