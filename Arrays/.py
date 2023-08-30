# string = "the sky is blue"
# string = " hello world "
string = "a good  example"
words = []

l = 0
r = 0
string = string + " "
while r < len(string):
    if string[r] == " ":
        words.append(string[l:r+1])
        l = r + 1
        r += 1

    elif string[r] != " ":
        r += 1
    
    
words.remove(" ")
    
res = "".join(words[::-1]).strip()

print(res)


        

