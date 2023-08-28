vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

string = "hello"
values = []
indexes = []
res = []
resString = ''

strArray = list(string)
    
for char in strArray:
    if char not in vowels:
        res.append(char)
    
for index, value in enumerate(strArray):
    if value in vowels:
        indexes.append(index)
        values.insert(-1, value)

for i in range(len(indexes)):
    res.insert(indexes[i], values[i])
    
print(resString.join(res))
