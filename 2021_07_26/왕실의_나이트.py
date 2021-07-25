location = list(input())

row = {'a' : 1, 'b' : 2 , 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
location[0] = row[location[0]]
location[1] = int(location[1])
steps = [(-2,1), (2,1), (-2,-1), (2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
count = 0

for step in steps:
    next_row = location[0] + step[0]
    next_col = location[1] + step[1]

    if next_row > 0 and next_col > 0 and next_col < 9 and next_row < 9:
        count += 1

print(count)