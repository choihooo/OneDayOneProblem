def rank(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            same += 1
        if lottos[i] == 0:
            zero += 1

    answer.append(rank(same+zero))
    answer.append(rank(same))
    return answer
