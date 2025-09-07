def validateStackSequences(pushed, popped):
    stack = []
    pop_idx = 0
    for val in pushed:
        stack.append(val)           
        while stack and stack[-1] == popped[pop_idx]:
            stack.pop()
            pop_idx += 1
    return not stack           
