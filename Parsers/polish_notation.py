operation_priority= {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '~': 4,
}
nums = '0123456789'

ops = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
    '^': lambda a, b: a**b,
}

def isnumber(s):
    try:
        n = int(s)
    except ValueError:
        return False
    return True

def encode(s):
    stack = []
    res = []
    tokens = s.split()
    for ch in tokens:
        if ch == ' ':
            continue
        if isnumber(ch):
            res.append(ch)
        else:
            if ch not in ('(', ')'):
                _priority = operation_priority[ch]
                while stack and operation_priority[stack[-1]] >= _priority and ch != '^':
                    res.append(stack.pop())
                stack.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                _ch = stack.pop()
                while stack and _ch != '(':
                    res.append(_ch)
                    _ch = stack.pop()

    res += stack[::-1]
    return res

def calculate(s):
    stack = []
    for tok in s:
        if isnumber(tok):
            stack.append(int(tok))
        else:
            b, a = stack.pop(), stack.pop()
            op = ops[tok]
            stack.append(op(a, b))

    return stack.pop()


q = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3 + 22 ^ 2'
# q = '( 3 + 1 ) + 4 * 2 ^ 3'
res = encode(q)
print(res)
f = calculate(res)
print(f)


