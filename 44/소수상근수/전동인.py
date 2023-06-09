# 상근수 : 각자리 숫자를 제곱해서 더하는 결과를 구하는 과정을 계속 반복해서 마지막에 1이 나오는 수
# 소수 : 1과 자기자신을 제외하고 약수가 없는 수이다.
# n이 주어졌을 때, n보다 작거나 같은 모든 소수 상근수를 구하라.

# 소수
def is_p(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 상근수


def is_s(n):
    visited = set()  # 중복을 방지하기 위한 집합
    while n != 1:
        n = sum(int(str_n)**2 for str_n in str(n))
        if n in visited:
            return False
        visited.add(n)
    return True


n = int(input())

for i in range(2, n+1):
    if is_p(i):
        if is_s(i):
            print(i)
