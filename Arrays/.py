str1 = "ABABAB"
str2 = "ABAB"

if max(len(str1), len(str2)) == len(str1):
    long = str1
    short = str2
else:
    long = str2
    short = str1

res = ""
numberOccur = 0
 
for i in range(len(long)):
    if str1[i] == str1[0] and i != 0:
        res += str1[:i]
        break

if res in short:
    numberOccur += short.count(res)


# Check how many times AB is in long and check how many times ABAB is in long and choose max

resOccursInLong = long.count(res)
resOccursInLong2 = long.count(res*numberOccur)

if resOccursInLong > resOccursInLong2:
    print(res)
else:
    print(res*numberOccur)
