def is_matched(expression):
    start_time = timeit.default_timer()
    dic = {"{":"}",
           "[":"]",
           "(":")"}
    stack = []
    for char in expression:
        if char in dic:
            stack.append(dic[char])
        else:
            if len(stack) == 0 or char != stack[-1]:
                return False
            stack.pop()
    elapsed = timeit.default_timer() - start_time
    print (elapsed)
    return len(stack) == 0
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
