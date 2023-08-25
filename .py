flowerbed = [0, 1, 0, 0, 1]
n = 1

# Handle edge cases by adding a 0 at the beginning and end of the flowerbed
flowerbed = [0] + flowerbed + [0]

# Initialize count
count = 0

for i in range(1, len(flowerbed) - 1):
    if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        flowerbed[i] = 1
        count += 1

# Check if the number of planted flowers is at least n
if count >= n:
    print(True)
else:
    print(False)