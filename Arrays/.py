vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

str = "hello"
# holle
strList = []

for char in str:
    strList.append(char)

positonVowels = []
positonVowelsReversed = []
vowels1 = []
vowels1Reversed = []


for i in range(len(strList)):
    if strList[i] in vowels:
        positonVowels.append(i)
        positonVowelsReversed.insert(-1, i)
        
for pos in positonVowels:  
    vowels1.append(str[pos])
    vowels1Reversed.insert(-1, str[pos])
        
# print(strList)

index = 0
for i in range(len(strList)):
    if strList[i] in vowels:
        index += 1
        print(1)
        strList[i] = vowels1Reversed[index]
    else:
        print(0)
print("i =", index)

    
# print(strList)
        
