def dev(flowerbed: list, n: int) -> bool:
    if flowerbed.count(0) >= n:
        return False
        
    else:
        return "Let's begin"
        
        
print(dev([1,0,0,0,1], 1))
    