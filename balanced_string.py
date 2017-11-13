def is_matched(expression):

    start_time = timeit.default_timer()
    stack = []
    for char in expression:
       if char is "{":
           stack.append("}")
       elif char is "[":
           stack.append("]")
       elif char is "(":
           stack.append(")")
       else:
           if len(stack) is 0 or char != stack[-1]:
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
