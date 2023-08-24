
from math import gcd
def gcdOfStrings(self, str1: str, str2: str) -> str:    
    if (str1 + str2) == (str2 + str1):
        return str1[:gcd(len(str1), len(str2))]
    return ""

# Runtime 33ms Beats 94.97% of users with Python3
# Memory 16.20MB Beats 74.83%of users with Python3
       