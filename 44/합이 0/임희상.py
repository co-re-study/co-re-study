
N = int(input())
students = list(map(int, input().split()))

students.sort()
students_dict = {}

for point in students:
    if point in students_dict:
        students_dict[point] += 1
    else:
        students_dict[point] = 1

answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        students_dict[students[i]] -= 1
        students_dict[students[j]] -= 1
        
        target = -(students[i] + students[j])
        if target in students_dict:
            answer += students_dict[target]
        
        students_dict[students[i]] += 1
        students_dict[students[j]] += 1

print(answer//3)