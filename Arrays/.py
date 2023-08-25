def dev(flowerbed: list, n: int) -> bool:
    flowerbed.append(0)
    flowerbed.insert(0, 0)
    
    count = 0
    if n >= flowerbed.count(0):
        return False
   
    else:
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                count += 1
        
    return True if count >= n else False

print(dev([1,0,0,0,1], 1))


# Runtime 145ms Beats 89.30% of users with Python3
# Memory 16.89MB Beats 20.25% of users with Python3
    