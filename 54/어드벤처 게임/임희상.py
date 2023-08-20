n = int(input())
answers = []

while n:

    rooms = [0]
    portals = [0] * (n+1)
    for i in range(1, n+1):
        info = input().split()
        content, money, next_rooms = info[0], int(info[1]), list(map(int, (info[2:-1])))
        portals[i] = next_rooms
        rooms.append([content, money])
    
    visited = [-1] * (n+1)
    if n == 1:
        if rooms[1][1] != 'T':
            stack = [(1, 0)]
    else:
        stack = [(1, 0)]
    answer = 'No'

    while stack:
        current, money = stack.pop()
        
        if current == n:
            answer = 'Yes'
            break
        
        if rooms[current][0] == 'L':
            money = max(money, rooms[current][1])
        elif rooms[current][0] == 'T':
            money -= rooms[current][1]
        
        if visited[current] >= money or money < 0:
            continue
        visited[current] = money
        

        for destination in portals[current]:
            if rooms[destination][0] == 'T' and rooms[destination][1] > money:
                continue
            stack.append((destination, money))
    

    answers.append(answer)

    n = int(input())

print('\n'.join(answers))