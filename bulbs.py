
class Solution:
    # @param A : list of integers
    # @return an integer
    def  bulbs(self, A):
        return self.bulbsHelper(A, 0)

    def bulbsHelper(self, A, off_state):
        print ('*'*5)
        print (off_state)
        print (A)
        if off_state in A:
            first_off = A.index(off_state)
            print(first_off)
            return 1 + self.bulbsHelper(A[(first_off+1):], int(not off_state))
        else: # no more presses needed!
            return 0
    def bulbs2(self,A):
        state,ret=0,0
        for bulb in A:
            if bulb == state:
                ret+=1
                state = 1 - state;
        return ret

x= Solution()
print(x.bulbs([0,1,1,0]))
