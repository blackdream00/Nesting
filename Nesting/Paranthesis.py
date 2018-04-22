def solution(S):
    parant = 0

    for element in S:
        if element == '(':
            parant += 1
        if element == ')':
            parant -= 1
            if parant < 0:
                return False

    if parant == 0:
        return True
    else:
        return False


print(solution('()()'))
print(solution('((())'))