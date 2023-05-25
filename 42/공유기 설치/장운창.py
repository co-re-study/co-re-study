N, C = map(int,input().split())
line = sorted([int(input()) for _ in range(N)])
left = 0
right = 1000000001
space = (left+right)//2
while right-left > 1:
    prev = -float('inf')
    cnt = C+0
    for i in line:
        if i-prev < space:
            continue
        cnt -= 1
        if not cnt:
            break
        prev = i
    if cnt:
        right = (left+right)//2
        space = (left+right)//2
    else:
        left = space+0
        space = (left+right)//2
print(left)
