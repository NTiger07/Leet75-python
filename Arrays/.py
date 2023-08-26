vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

str = "hello"
positionOfVowels = []

for i in range(len(str)):
    if str[i] in vowels:
        positionOfVowels.append(i)
        
print(positionOfVowels)