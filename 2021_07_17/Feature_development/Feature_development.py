def solution(progresses, speeds):
    answer = []
    success = 0

    while True:
        if len(progresses) == 0:
            break

        for i in range(len(progresses)):
            if progresses[i] >= 100:
                success += 1
            else:
                break

        for i in range(success):
            del progresses[0]
            del speeds[0]

        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        if success != 0:
            answer.append(success)
            success = 0

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
