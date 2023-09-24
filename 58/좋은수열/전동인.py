def is_good(seq):
    length = len(seq)
    for i in range(1, length//2 + 1):  # 모든 가능한 부분수열의 길이에 대해
        if seq[-i:] == seq[-2*i:-i]:  # 마지막에 추가한 숫자로 인해 나쁜 수열이 되었는지 확인
            return False
    return True


def find_seq(n, seq=""):
    if len(seq) == n:
        return seq
    for next_num in ['1', '2', '3']:
        if is_good(seq + next_num):  # 현재 수열에 next_num을 추가했을 때 좋은 수열인지 확인
            result = find_seq(n, seq + next_num)
            if result:  # 좋은 수열을 찾았으면 그 결과를 반환
                return result


N = int(input())
print(find_seq(N))
