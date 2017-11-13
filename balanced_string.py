def is_matched(expression):
    # start_time = timeit.default_timer()
    # dic = {"{":"}",
    #        "[":"]",
    #        "(":")"}
    # stack = []
    # for char in expression:
    #     if char in dic:
    #         stack.append(dic[char])
    #     else:
    #         if len(stack) == 0 or char != stack[-1]:
    #             return False
    #         stack.pop()
    # elapsed = timeit.default_timer() - start_time
    # print (elapsed)
    # return len(stack) == 0
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
