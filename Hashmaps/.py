# In simple terms, this algorithm checks if two words have the same set of characters 
# and the same frequency of each character. 
# If they do, it considers the words to be close.
from collections import Counter

word1 = "abc"
word2 = "bca"

hash1 = {}
hash2 = {}

for index in range(len(word1)):
    if word1[index] not in hash1:
        hash1[word1[index]] = 1
    else:
        hash1[word1[index]] += 1

for index in range(len(word1)):
    if word2[index] not in hash2:
        hash2[word2[index]] = 1
    else:
        hash2[word2[index]] += 1



print(hash1.keys() == hash2.keys())


print(hash1)
print(hash2)