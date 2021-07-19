def solution(a, b):
    tmp = 0
    for i in range(len(a)):
        tmp += a[i] * b[i]

    return tmp
