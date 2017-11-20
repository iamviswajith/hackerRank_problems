"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.

Example:

The 32-bit integer 11 has binary representation

00000000000000000000000000001011
so the function should return 3.

"""
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        A = '{0:032b}'.format(A);
        return A.count('1')


class Solution1:
    # @param A : integer
    # @return an integer
    """
    This special solution uses a trick which is normally used in bit manipulations.
    Notice what x - 1 does to bit representation of x.
    x - 1 would find the first set bit from the end, and then set it to 0, and set all the bits following it.

    Which means if x = 10101001010100
                                  ^
                                  |
                                  |
                                  |

                           First set bit from the end
    Then x - 1 becomes 10101001010(011)

    All other bits in x - 1 remain unaffected.
    This means that if we do (x & (x - 1)), it would just unset the last set bit in x (which is why x&(x-1) is 0 for powers of 2).
    """
    def numSetBits(self, A):
        ret = 0
        while A != 0:
            if A&1:
                ret += 1
            A = A >> 1
        return ret

x= Solution()
print(x.numSetBits(11))
y= Solution1()
print(y.numSetBits(11))
