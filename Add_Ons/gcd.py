"""
THERE ARE MANY METHODS/APPROACHES TO FIND GCD

SOME ARE LIST BELOW
"""


# EFFICIENT : FASTER
import math
a,b = 4,88
print(math.gcd(a,b))


# TIME COMPLEXITY: O(log(max(a,b)))
# EFFICIENT when one of the numbers is very large
while a:
	a, b = b % a, a
print("GCD of a,b is: ",b)
