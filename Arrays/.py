candies = [2, 3, 5, 1, 3]
extraCandies = 3
res = []

max_candies = max(candies)  

print(max_candies)

for i in range(len(candies)):
    candies[i] += extraCandies
    res.append(candies[i] >= max_candies) 
    print(res)





