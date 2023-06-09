from collections import deque
people_numbers = int(input())
person1, person2 = map(int, input().split())
relative_number = int(input())
relative_tree = [[] for _ in range(people_numbers+1)]
for i in range(relative_number):
    one, two = map(int, input().split())
    relative_tree[one].append(two)
    relative_tree[two].append(one)
visited = set()
queue = deque()
queue.append(person1)
cnt = 0
check = [0 for _ in range(people_numbers+1)]
flag = False
while queue:
    current = queue.popleft()
    visited.add(current)
    for i in relative_tree[current]:
        if not i in visited:
            check[i] = check[current] + 1
            queue.append(i)
        if i == person2:
            print(check[i])
            flag = True
            break
    if flag:
        break

if check[person2] == 0:
    print(-1)