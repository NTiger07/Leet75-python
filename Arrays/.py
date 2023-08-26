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
        

# print(positonVowels)
# print(positonVowelsReversed)
# print(vowels1)
# print(vowels1Reversed)

# for i in range(len(strList)):
#     if strList[i] in vowels:
#         strList[i] = vowels1Reversed[i]
#         break
    
print(strList)
i = 0
while i < len(vowels1Reversed):
    strList[i] = vowels1Reversed[i]
    print(i)
    i += 1
    
print(strList)
        
