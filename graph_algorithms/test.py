from sys import stdin

for line in stdin:
    l = list(line[-1])

    pair = {'}': '{', ']': '[', ')': '('}
    is_poss = True
    stack = []
    for symb in l:
        if symb in '})]' and (len(stack) == 0 or stack.pop() != pair[symb]):
            is_poss = False
            break
        if symb in '{([':
            stack.append(symb)

    if is_poss and len(stack) == 0:
        print(0, end='')
    else:
        print(1, end='')
