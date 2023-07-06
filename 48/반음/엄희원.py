N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

p = ['C', -1, 'D', -1, 'E', 'F', -1, 'G', -1, 'A', -1, 'B'] * 2

se_list = []

for i in range(12):
    if p[i] != -1:
        temp = i
        start = p[i]
        end = -1
        flag = True
        for num in arr:

            temp += num

            if temp < 0:
                temp = 24 + temp
                if p[temp] == -1:
                    flag = False
                    break
            elif temp >= 24:
                temp = temp - 24
                if p[temp] == -1:
                    flag = False
                    break
            else:
                if p[temp] == -1:
                    flag = False
                    break

        if flag and p[temp] != -1:
            end = p[temp]
            se_list.append((start, end))

se_list.sort()

for t in se_list:
    print(t[0], t[1])




