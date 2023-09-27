def uniqueOccurrences(arr: list[int]) -> bool:
    hash = {}


    for i in range(len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]] += 1


    occurrences = hash.values()

    return len(occurrences) == len(set(occurrences))

# Runtime 42ms Beats 75.60% of users with Python3
# Memory 16.37MB Beats 77.08% of users with Python3