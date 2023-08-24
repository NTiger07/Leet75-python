str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
from math import gcd


gCD = gcd(len(str1), len(str2))

print(gCD)
if (str1 + str2) == (str2 + str1):
    print(str1[:gCD])
else:
    print("")