flowerbed = [1,0,0,0,1]
n = 1

freeSpaces = flowerbed.count(0)

res = []

for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
        res.append(i)
        
# print(freeSpaces)
print(res)





