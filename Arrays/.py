vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

string = "race car"
string = list(string)
values = []
indexes = []
    

# for char in string:
#     if char not in vowels:
#         res.append(char)
    
# for index, value in enumerate(string):
#     if value in vowels:
#         indexes.append(index)
#         values.insert(-1, value)

# for i in range(len(indexes)):
#     # res.insert(indexes[i], values[i])
#     string[index[i]] = values[i]

for i in range(len(string)):
    if string[i] in vowels:
        values.append(string[i])
        indexes.append(i)
values = values[::-1]
for i in range(len(indexes)):
    string[indexes[i]] = values[i]

    

print("".join(string))
