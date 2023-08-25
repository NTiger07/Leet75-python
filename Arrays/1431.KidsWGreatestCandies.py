def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []

        max_candies = max(candies)  

        for i in range(len(candies)):
            candies[i] += extraCandies
            res.append(candies[i] >= max_candies)  # Append True if candies[i] is greater or equal to max_candies, False otherwise
                
        return res
    
    
# Runtime 37ms Beats 96.51% of users with Python3
# Memory 16.40MB Beats 33.34% of users with Python3
