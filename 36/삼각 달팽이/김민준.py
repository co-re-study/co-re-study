### 피라미드 그리기

n = int(input())
triangle = []
for i1 in range(n):
    triangle.append([0]*(i1+1))
r = -1
c =  0
count = 1
current = 0
for i in range(n):
    for j in range(i,n):
        if i%3 == 0:
            r += 1
        elif i%3 == 1:
            c += 1
        else:
            r -= 1
            c -= 1
        triangle[r][c] = count
        count += 1
ans = []
for output in range(n):
    for num in triangle[output]:
        ans.append(num)
print(ans)