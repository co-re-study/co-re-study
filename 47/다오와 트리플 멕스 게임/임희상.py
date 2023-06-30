N = int(input())
M = 1000000
A = set(map(int, input().split()))

def mex(target):
    for i in range(M):
        if i not in target:
            return i


def get_next(target):
    target_mex = mex(target)
    if 0 not in target:
        return {0}
    if len(target) == 1:
        return {1}
    return set(range(target_mex+1))
        

B = get_next(A)
C = get_next(B)
print(mex(C))
