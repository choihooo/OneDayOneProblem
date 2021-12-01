def solution(s):
    answer = 0
    tmp = []
    answer_list = []
    num_eng = { "zero": "0",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"
                }

    find_key = list(num_eng.keys())
    
    for i in s:
        stmp = "".join(tmp)
        if i.isdigit():
            if len(tmp) != 0:
                answer_list.append(num_eng[stmp])
                tmp.clear()
            answer_list.append(i)
        elif stmp in find_key:
                answer_list.append(num_eng[stmp])
                tmp.clear()
                tmp.append(i)
        else:
            tmp.append(i)

    stmp = "".join(tmp)
    if stmp in find_key:
        answer_list.append(num_eng[stmp])


    answer = "".join(answer_list)
    return int(answer)

print(solution("one4seveneight"))