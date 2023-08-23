str1 = "ABABAB"
str2 = "ABAB"
# expect AB SINCE ABAB APPEAR ONLY ONCE IN STR1

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
    

# if res in short:
#     numberOccur += short.count(res)

print(res)
       
# print(res*numberOccur)