n = int(input())
piano = ['A', '', 'B', 'C', '', 'D', '', 'E', 'F', '', 'G', '']
notes = [int(input()) for _ in range(n)]
for key in [0, 2, 3, 5, 7, 8, 10]:
    start, flag = piano[key], True
    for note in notes:
        key = (key + note) % 12
        if not piano[key]:
            flag = False
            break
    if flag:
        print(start, piano[key])
