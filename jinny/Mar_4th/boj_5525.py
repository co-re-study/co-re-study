# IOIOI
n = int(input())
m = int(input())
s = input()

answer = 0
pattern = 0
arrow = 0
while arrow < m - 2:
    if s[arrow:arrow+3] == "IOI":
        pattern += 1
        if pattern == n:
            answer += 1
            pattern -= 1
        arrow += 1
    else:
        pattern = 0
    arrow += 1
print(answer)
# 시간 초과
# n = int(input())
# m = int(input())
# s = input()
# pattern = "I"+"OI"*n
# answer = 0
# for i in range(m-(n*2)):
#     if s[i:i+(2*n)+1] == pattern:
#         answer += 1
# print(answer)