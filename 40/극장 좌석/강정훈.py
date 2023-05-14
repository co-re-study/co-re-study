'''
VIP좌석 기준으로 배열이 차단된다고 생각하면 풀기 쉽고 차단된 배열들의 각자의 경우의수를 곱해주면 답이 나옴.
점화식 세우면
N = 1일 때, A = 1
N = 2일 때, A = 2
N = 3일 때, A = 3
N = 4일 때, A= 5
N = 5일 때, A =8
...
=> 피보나치 점화식임
'''
N = int(input())
VIP_N = int(input())
VIP_list = []
for i in range(VIP_N):
    VIP_list.append(int(input()))

Fibo = [1, 1]
for i in range(2, N+1):
    Fibo.append(Fibo[i-2] + Fibo[i-1])

answer = 1
if VIP_N != 0:
    for i in range(len(VIP_list)+1):
        if i == 0:
            answer = answer * Fibo[VIP_list[i]-1]

        elif i == len(VIP_list):
            last_arr_length = N - VIP_list[-1]
            answer = answer * Fibo[last_arr_length]
        else:
            arr_length = VIP_list[i] - VIP_list[i-1] -1
            answer = answer * Fibo[arr_length]
else:
    answer = Fibo[N]

print(answer)




