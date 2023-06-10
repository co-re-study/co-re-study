from collections import deque
n, m = map(int, input().split())

head = (0, 1)
dc = [1, -1]

queue = deque([])

def next_line(line_type, num, d):
    if d == 1:
        current = 2
    else:
        if line_type == 'row':
            current = m
        else:
            current = n
    if line_type == 'row':
        for _ in range(m-1):
            queue.append((num, current))
            current += d
        return
    if line_type == 'column':
        for _ in range(n-1):
            queue.append((current, num))
            current += d
        return
    

if not (n % 2):
    for i in range(1, n+1):
        if i % 2:
            d = 1
        else:
            d = -1
        next_line('row', i, d)
    for j in range(n, 0, -1):
        queue.append((j, 1))

elif not (m % 2):
    for i in range(1, m+1):
        if i % 2:
            d = 1
        else:
            d = -1
        next_line('column', i, d)
    for j in range(m, 0, -1):
        queue.append((1, j))
else:
    for i in range(1, n-1):
        if i % 2:
            d = 1
        else:
            d = -1
        next_line('row', i, d)
    
    for k in range(m, 1, -1):
        if k % 2:
            queue.extend([(n-1, k), (n, k)])
        else:
            queue.extend([(n, k), (n-1, k)])    
    for j in range(n-1, 0, -1):
        queue.append((j, 1))
    
print(len(queue))
while queue:
    print(*queue.popleft())