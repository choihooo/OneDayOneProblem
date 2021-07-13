def solution(answers):
    answer = []
    size = len(answers)

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i in range(size):
        if first[i % 5] == answers[i]:
            score[0] += 1
        if second[i % 8] == answers[i]:
            score[1] += 1
        if third[i % 10] == answers[i]:
            score[2] += 1

    max_score = max(score)

    for i in range(len(score)):
        if max_score == score[i]:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))
