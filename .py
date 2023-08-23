str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


res = ""
    
firstElem = str1[0]

for i in range(len(str1)):
    if str1[i] == str1[0] and i != 0:
        res += str1[:i]
        break
    
print(res)