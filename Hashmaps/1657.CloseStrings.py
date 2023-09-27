from collections import Counter

def closeStrings(self, word1: str, word2: str) -> bool:
    c1=Counter(word1)
    c2=Counter(word2)
    a,b=sorted(c1.values()),sorted(c2.values())
    return c1.keys()==c2.keys() and a==b

# In simple terms, this algorithm checks if two words 
# have the same set of characters 
# and the same frequency of each character. 
# If they do, it considers the words to be close.

