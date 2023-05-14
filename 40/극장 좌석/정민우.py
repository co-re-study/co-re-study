# 일정 길이마다 경우의 수를 구하는 일정한 공식이 있겠다.
# 고정석은 무조건 정해진 자리이므로 고정석 기준 양옆을 끊어진 리스트로 생각해도 되겠다.
# 고정석마다 리스트를 끊어서 각 길이의 경우의 수를 합하면 되겠다.

# n의 길이를 가진 좌석 S는 S(n-2) * 2 + (S(n-1) - S(n-2)) 의 공식을 가지고 있음.

# 풀고보니 피보나치수열과 동일한듯...

seat_case_num_list: [int] = [1, 1, 2, 3] + [0] * 37


def seat(n: int):
    if seat_case_num_list[n] == 0:
        seat_case_num_list[n] = seat(n - 2) * 2 + (seat(n - 1) - seat(n - 2))
    return seat_case_num_list[n]


N: int = int(input())
M: int = int(input())
ans: int = 1
prev_vip_seat: int = 0
for _ in range(M):
    now_vip_seat: int = int(input())
    ans *= seat(now_vip_seat - prev_vip_seat - 1)
    prev_vip_seat = now_vip_seat
ans *= seat(N - prev_vip_seat)
print(ans)
