arr = [1,2,2,1,1,3]

from collections import Counter

def uniqueOccurrences(arr: list[int]) -> bool:
    return len(set(Counter(arr).values())) == len(Counter(arr).values())

print(uniqueOccurrences(arr))
