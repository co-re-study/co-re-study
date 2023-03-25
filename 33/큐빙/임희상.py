import copy

def rotate_side(side, direction):
    if direction == '+':
        horizontal_cube[side] = list(map(list, zip(*horizontal_cube[side][::-1])))
        vertical_cube[side] = list(map(list, (zip(*vertical_cube[side]))))[::-1]

        if side == 'U':
            horizontal_cube['F'][0], horizontal_cube['L'][0], horizontal_cube['B'][0], horizontal_cube['R'][0] = \
                horizontal_cube['R'][0], horizontal_cube['F'][0], horizontal_cube['L'][0], horizontal_cube['B'][0]
            vertical_cube['F'] = list(map(list, zip(*horizontal_cube['F'])))
            vertical_cube['L'] = list(map(list, zip(*horizontal_cube['L'])))
            vertical_cube['B'] = list(map(list, zip(*horizontal_cube['B'])))
            vertical_cube['R'] = list(map(list, zip(*horizontal_cube['R'])))
        if side == 'D':
            horizontal_cube['F'][-1], horizontal_cube['R'][-1], horizontal_cube['B'][-1], horizontal_cube['L'][-1] = \
                horizontal_cube['L'][-1], horizontal_cube['F'][-1], horizontal_cube['R'][-1], horizontal_cube['B'][-1]
            vertical_cube['F'] = list(map(list, zip(*horizontal_cube['F'])))
            vertical_cube['R'] = list(map(list, zip(*horizontal_cube['R'])))
            vertical_cube['B'] = list(map(list, zip(*horizontal_cube['B'])))
            vertical_cube['L'] = list(map(list, zip(*horizontal_cube['L'])))
        if side == 'F':
            horizontal_cube['U'][-1], vertical_cube['R'][0], horizontal_cube['D'][0], vertical_cube['L'][-1] = \
                vertical_cube['L'][-1][::-1], horizontal_cube['U'][-1], vertical_cube['R'][0][::-1], horizontal_cube['D'][0]
            vertical_cube['U'] = list(map(list, zip(*horizontal_cube['U'])))
            horizontal_cube['R'] = list(map(list, zip(*vertical_cube['R'])))
            vertical_cube['D'] = list(map(list, zip(*horizontal_cube['D'])))
            horizontal_cube['L'] = list(map(list, zip(*vertical_cube['L'])))
        if side == 'R':
            vertical_cube['U'][-1], vertical_cube['B'][0], vertical_cube['D'][-1], vertical_cube['F'][-1] = \
                vertical_cube['F'][-1], vertical_cube['U'][-1][::-1], vertical_cube['B'][0][::-1], vertical_cube['D'][-1]
            horizontal_cube['U'] = list(map(list, zip(*vertical_cube['U'])))
            horizontal_cube['F'] = list(map(list, zip(*vertical_cube['F'])))
            horizontal_cube['B'] = list(map(list, zip(*vertical_cube['B'])))
            horizontal_cube['D'] = list(map(list, zip(*vertical_cube['D'])))
        if side == 'B':
            horizontal_cube['U'][0], vertical_cube['L'][0], horizontal_cube['D'][-1], vertical_cube['R'][-1] = \
                vertical_cube['R'][-1], horizontal_cube['U'][0][::-1], vertical_cube['L'][0], horizontal_cube['D'][-1][::-1]
            vertical_cube['U'] = list(map(list, zip(*horizontal_cube['U'])))
            horizontal_cube['R'] = list(map(list, zip(*vertical_cube['R'])))
            vertical_cube['D'] = list(map(list, zip(*horizontal_cube['D'])))
            horizontal_cube['L'] = list(map(list, zip(*vertical_cube['L'])))
        if side == 'L':
            vertical_cube['U'][0], vertical_cube['F'][0], vertical_cube['D'][0], vertical_cube['B'][-1] = \
                vertical_cube['B'][-1][::-1], vertical_cube['U'][0], vertical_cube['F'][0], vertical_cube['D'][0][::-1]
            horizontal_cube['U'] = list(map(list, zip(*vertical_cube['U'])))
            horizontal_cube['F'] = list(map(list, zip(*vertical_cube['F'])))
            horizontal_cube['B'] = list(map(list, zip(*vertical_cube['B'])))
            horizontal_cube['D'] = list(map(list, zip(*vertical_cube['D'])))

    else:
        horizontal_cube[side] = list(map(list, zip(*horizontal_cube[side])))[::-1]
        vertical_cube[side] = list(map(list, (zip(*vertical_cube[side][::-1]))))

        if side == 'U':
            horizontal_cube['F'][0], horizontal_cube['L'][0], horizontal_cube['B'][0], horizontal_cube['R'][0] = \
                horizontal_cube['L'][0], horizontal_cube['B'][0], horizontal_cube['R'][0], horizontal_cube['F'][0]
            vertical_cube['F'] = list(map(list, zip(*horizontal_cube['F'])))
            vertical_cube['L'] = list(map(list, zip(*horizontal_cube['L'])))
            vertical_cube['B'] = list(map(list, zip(*horizontal_cube['B'])))
            vertical_cube['R'] = list(map(list, zip(*horizontal_cube['R'])))
        if side == 'D':
            horizontal_cube['F'][-1], horizontal_cube['R'][-1], horizontal_cube['B'][-1], horizontal_cube['L'][-1] = \
                horizontal_cube['R'][-1], horizontal_cube['B'][-1], horizontal_cube['L'][-1], horizontal_cube['F'][-1]
            vertical_cube['F'] = list(map(list, zip(*horizontal_cube['F'])))
            vertical_cube['R'] = list(map(list, zip(*horizontal_cube['R'])))
            vertical_cube['B'] = list(map(list, zip(*horizontal_cube['B'])))
            vertical_cube['L'] = list(map(list, zip(*horizontal_cube['L'])))
        if side == 'F':
            horizontal_cube['U'][-1], vertical_cube['R'][0], horizontal_cube['D'][0], vertical_cube['L'][-1] = \
                vertical_cube['R'][0], horizontal_cube['D'][0][::-1], vertical_cube['L'][-1], horizontal_cube['U'][-1][::-1]
            vertical_cube['U'] = list(map(list, zip(*horizontal_cube['U'])))
            horizontal_cube['R'] = list(map(list, zip(*vertical_cube['R'])))
            vertical_cube['D'] = list(map(list, zip(*horizontal_cube['D'])))
            horizontal_cube['L'] = list(map(list, zip(*vertical_cube['L'])))
        if side == 'R':
            vertical_cube['U'][-1], vertical_cube['B'][0], vertical_cube['D'][-1], vertical_cube['F'][-1] = \
                vertical_cube['B'][0][::-1], vertical_cube['D'][-1][::-1], vertical_cube['F'][-1], vertical_cube['U'][-1]
            horizontal_cube['U'] = list(map(list, zip(*vertical_cube['U'])))
            horizontal_cube['F'] = list(map(list, zip(*vertical_cube['F'])))
            horizontal_cube['B'] = list(map(list, zip(*vertical_cube['B'])))
            horizontal_cube['D'] = list(map(list, zip(*vertical_cube['D'])))
        if side == 'B':
            horizontal_cube['U'][0], vertical_cube['L'][0], horizontal_cube['D'][-1], vertical_cube['R'][-1] = \
                vertical_cube['L'][0][::-1], horizontal_cube['D'][-1], vertical_cube['R'][-1][::-1], horizontal_cube['U'][0]
            vertical_cube['U'] = list(map(list, zip(*horizontal_cube['U'])))
            horizontal_cube['R'] = list(map(list, zip(*vertical_cube['R'])))
            vertical_cube['D'] = list(map(list, zip(*horizontal_cube['D'])))
            horizontal_cube['L'] = list(map(list, zip(*vertical_cube['L'])))
        if side == 'L':
            vertical_cube['U'][0], vertical_cube['F'][0], vertical_cube['D'][0], vertical_cube['B'][-1] = \
                vertical_cube['F'][0], vertical_cube['D'][0], vertical_cube['B'][-1][::-1], vertical_cube['U'][0][::-1]
            horizontal_cube['U'] = list(map(list, zip(*vertical_cube['U'])))
            horizontal_cube['F'] = list(map(list, zip(*vertical_cube['F'])))
            horizontal_cube['B'] = list(map(list, zip(*vertical_cube['B'])))
            horizontal_cube['D'] = list(map(list, zip(*vertical_cube['D'])))

T = int(input())
for test_case in range(T):
    n = int(input())
    orders = input().split()
    horizontal_cube = {
        'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
        'D': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
        'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
        'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
        'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
    }
    vertical_cube = copy.deepcopy(horizontal_cube)
    for i in range(n):
        order = orders[i]
        rotate_side(order[0], order[1])

    for i in range(3):
        print(''.join(horizontal_cube['U'][i]))

