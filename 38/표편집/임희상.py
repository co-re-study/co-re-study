def solution(n, k, cmd):
    answer = []
    current = k
    deleted = [False] * n
    delete_stack = []
    portal = [[0, 0] for _ in range(n)]
    for i in range(n):
        portal[i][0] = i - 1
        portal[i][1] = i + 1

    last = n - 1
    for command in cmd:
        if command[0] == 'U':
            stride = int(command.split()[1])
            for i in range(stride):
                current = portal[current][0]

        if command[0] == 'D':
            stride = int(command.split()[1])
            for i in range(stride):
                current = portal[current][1]

        if command == 'C':
            deleted[current] = True
            delete_stack.append(current)
            if current != last:
                prev, follow = portal[current]
                if current != 0:
                    portal[prev][1] = follow
                if current != n-1:
                    portal[follow][0] = prev
                current = follow
            else:
                current = portal[current][0]
                last = current

        if command == 'Z':
            target = delete_stack.pop()
            deleted[target] = False
            prev, follow = portal[target]
            if target != 0:
                portal[prev][1] = target
            if target != n-1:
                portal[follow][0] = target
            if target > last:
                last = target

    for deleted_record in deleted:
        if not deleted_record:
            answer.append('O')
        else:
            answer.append('X')
    return ''.join(answer)
