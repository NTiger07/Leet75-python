arr = [1,2,2,1,1,3]
def uniqueOccurrences(arr):
    hash = {}


    for i in range(len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]] += 1


    occurrences = hash.values()

    return len(occurrences) == len(set(occurrences))


print(uniqueOccurrences(arr))