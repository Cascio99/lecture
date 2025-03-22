postfix = []
stack = []
number = []

def infix_to_postfix(expr):

    for token in expr:
        if(len(token) == 1):
            if token[0] in ['+', '-' ,'*']:
                while stack and op_priority(stack[-1]) >= op_priority(token):
                    postfix.append(stack.pop())
                stack.append(token)
            else:
                number.append(int(token))
        else:
            number.append(int(token))

    while stack:
        postfix.append(stack.pop())

    return postfix