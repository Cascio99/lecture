def calc_postfix(expr):
    result = 0
    stack = []  # 스택을 사용하여 계산에 필요한 값들을 저장합니다.

    for token in expr:
        if token.isdigit():
            # 토큰이 숫자인 경우
            stack.append(int(token))  # 스택에 숫자를 넣습니다.
        else:
            # 토큰이 연산자인 경우
            second = stack.pop()  # 스택에서 두 번째 피연산자를 팝합니다.
            first = stack.pop()   # 스택에서 첫 번째 피연산자를 팝합니다.
            op = token            # 현재 연산자를 가져옵니다.

            if op == '+':
                result = first + second  # 덧셈 연산 수행
            elif op == '-':
                result = first - second  # 뺄셈 연산 수행
            elif op == '*':
                result = first * second  # 곱셈 연산 수행

            stack.append(result)  # 연산 결과를 스택에 넣습니다.

    return stack[0]  # 스택에 남은 값은 최종 결과값입니다.
