def solution(priorities, location):
    answer = 0
    cur = location
    cnt = 0
    i = priorities[location]

    while True:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            del priorities[0]
            if cur == 0:
                cur = len(priorities)
            else:
                cur -= 1
        if cur == 0 and i == max(priorities):
            cnt += 1
            answer = cnt
            break
        elif max(priorities) == priorities[0]:
            del priorities[0]
            cnt += 1
            cur -= 1

        if len(priorities) == 0:
            answer = cnt
            break

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
