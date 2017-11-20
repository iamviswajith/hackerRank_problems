"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]

If a < c OR a==c AND b < d. 
"""


class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        # check upto hald of A because there need to be a prime number between 2-- A/2 -- A
        # just so that we can check if i and A-i are both prime numbers
        for i in range(2, A//2 + 1):
            if self.is_prime(i) and self.is_prime(A - i):
                return (i, A - i)
        return (0, 0)
    def is_prime(self, a):
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        return True

x = Solution()
print (x.primesum(10))
