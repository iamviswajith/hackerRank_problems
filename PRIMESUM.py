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
