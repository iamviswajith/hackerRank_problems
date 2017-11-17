
array = [1,2,2,3,1]


"""
doing bitwise XOR would cancel all the same numbers and leave the variable
with single value item in this case
explanation:
1^2 is a some bitwise between these two numbers
!^2^2 leaves the variable with 1
"""
ret = array[0]
for i in range(1,len(array)):
    ret ^= array[i]
print (ret)
