# 내 답: 처참히 틀린답
# def solution(priorities, location):
#     answer = 0
#     cur = location
#     cnt = 0
#     i = priorities[location]

#     while True:
#         if priorities[0] < max(priorities):
#             priorities.append(priorities[0])
#             del priorities[0]
#             if cur == 0:
#                 cur = len(priorities)
#             else:
#                 cur -= 1
#         if cur == 0 and i == max(priorities):
#             cnt += 1
#             answer = cnt
#             break
#         elif max(priorities) == priorities[0]:
#             del priorities[0]
#             cnt += 1
#             cur -= 1

#         if len(priorities) == 0:
#             answer = cnt
#             break

#     return answer


# print(solution([2, 1, 3, 2], 2))
# print(solution([1, 1, 9, 1, 1, 1], 0))

def solution(priorities, location):
    answer = 0
    from collections import deque

    d = deque([(v, i) for i, v in enumerate(priorities)])
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer


print(solution([2, 1, 3, 2], 2))
