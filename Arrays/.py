string = "the sky is blue"
words = []

l = 0
r = 0

while r < len(string):
    if string[r] == " ":
        words.append(string[l:r+1])
        l = r
        r += 1

    elif string[r] != " ":
        r += 1
       
        
print(words)