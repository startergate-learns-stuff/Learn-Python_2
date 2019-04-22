from .f04221 import *

prec = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}


def solution(S):
    opStack = ArrayStack()
    answer = ''

    for i in len(S):
        char = S[i]
        if char not in prec.keys():
            answer += char
            continue
        if char == '(':



    return answer
