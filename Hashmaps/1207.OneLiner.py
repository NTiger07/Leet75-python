arr = [1,2,2,1,1,3]

from collections import Counter

def uniqueOccurrences(arr: list[int]) -> bool:
    return len(set(Counter(arr).values())) == len(Counter(arr).values())


# Runtime 43ms Beats 65.55% of users with Python3
# Memory1 6.37MB Beats 77.08% of users with Python3
