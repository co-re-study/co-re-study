'''
슬라이딩 윈도우로 풀어봅시다.
첫 번째 방법은 원래 하던대로 배열을 두배로 늘린 뒤,
(배열에서 k개씩 보는 것 + 보너스)의 개수를 갱신해주는 방법이었는데 시간초과가 났다.
두 번째 방법은 배열은 그대로 두배로 한 뒤 deque와 defaultdict로 초밥을 관리해주는 방법을 사용했다.
pypy3 로 통과하기는 했지만, 배열의 길이를 두배로 만드는 것이 비효율적이라고 생각함.
세 번째 방법은 배열의 길이를 원래대로 하고, deque도 없애보았다.
deque를 없앤 대신 cnt를 사용해 counts의 길이를 관리하도록 함.
'''
# 첫 번째 방법 시간초과
import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]*2
ans = 0
for i in range(0, 2*N-k+1):
    ans = max(ans, len(set(arr[i:i+k]) | {c}))
print(ans)

# 두 번째 방법 pypy3 (1352ms)
import sys
from collections import deque, defaultdict
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]*2
counts = defaultdict(int)
curr = deque()
counts[c] += 1
ans = 0
for i in range(k):
    counts[arr[i]] += 1
    curr.append(arr[i])
for j in range(k, 2*N):
    a = curr.popleft()
    counts[a] -= 1
    if not counts[a]:
        del counts[a]
    counts[arr[j]] += 1
    curr.append(arr[j])
    ans = max(ans, len(counts))
print(ans)

# 세 번째 방법 python3 (3844ms) pypy3 (984ms)
import sys
from collections import defaultdict
input = sys.stdin.readline
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
counts = defaultdict(int)
counts[c] += 1
ans = 0
cnt = 1
for i in range(k):
    if not counts[arr[i]]:
        cnt += 1
    counts[arr[i]] += 1
for j in range(k, N+k):
    counts[arr[j-k]] -= 1
    if not counts[arr[j-k]]:
        cnt -= 1
    if not counts[arr[j % N]]:
        cnt += 1
    counts[arr[j % N]] += 1
    ans = max(ans, cnt)
print(ans)
