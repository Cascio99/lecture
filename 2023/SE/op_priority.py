def op_priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*':
        return 2
    else:
        return 0