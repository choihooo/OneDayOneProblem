# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     d = deque(truck_weights)
#     cur = []
#     with_truck = 0
#     while len(truck_weights):
#         cur.append(d.popleft())
#         while True:
#             item = d.popleft
#             if sum(cur) + item > weight:
#                 d.appendleft(item)
#                 break
#             else:
#                 cur.append(item)
#                 with_truck += 1

#         answer += bridge_length

#     return answer


# print(solution(2, 10, [7, 4, 5, 6]))

# 1번
def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer
