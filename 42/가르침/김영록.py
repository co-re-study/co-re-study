'''
초기 아이디어
antic 를 제외한 나머지 21개의 
알파벳을 재귀로 넣고 빼면서 ans를 갱신하자. -> 시간초과
2차 아이디어 
재귀를 combinations로 바꾸고 경우의 수를 모두 계산해보자.
결과는 시간초과.
최악의 경우 combinations는 21!/10!11! = 352716개를 봐야하고
거기에 N의 최대 개수 50개에 
단어의 최대 길이 15-8 = 7개에 갱신도 하고, 처음 받을때 파싱도 하니
시간 초과가 날 법 하다고 생각했다...
그래서 2차 아이디어에 비트마스킹을 넣은 방법을 생각했다.
가능한 나머지 21개의 알파벳을 enumerate로 번호 지정을 해주고,
이걸 2진수의 자리수에 넣는다고 생각했다. (기본 비트마스킹 아이디어)
그래서 (2진수로 변환한 수)&(경우의 수의 합) 를 했을때 2진수로 변환한 수가 나온다면
해당 경우의 수에 2진수로 변환한 수가 포함된다는 소리이므로 temp += 1 를 해주고
temp와 ans를 비교하며 ans를 갱신시켜준다. (최댓값 찾기)
'''


import sys
from itertools import combinations


def bit(word):
    res = 0
    for w in word:
        res |= 1 << available_bin[w]
    return res


input = sys.stdin.readline
N, K = map(int, input().split())
ans = 0
alpha = {'a', 'n', 't', 'i', 'c'}
words = [set(input().strip()[4:-4]) - alpha for _ in range(N)]
available = set(chr(i) for i in range(97, 123)) - alpha
available_bin = {val: num for num, val in enumerate(available)}

if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    words_bin = [bit(word) for word in words]
    for c in combinations([2**i for i in range(21)], K-5):
        temp = 0
        c_sum = sum(c)
        for word_bin in words_bin:
            if word_bin & c_sum == word_bin:
                temp += 1
        ans = max(ans, temp)
    print(ans)



'''
첫 번째 방법 set + 재귀 (시간초과)

def back(cnt):
    global ans
    if cnt == K-5:
        temp = 0
        for word in words:
            for w in word:
                if w not in alpha:
                    break
            else:
                temp += 1
        ans = max(ans, temp)
        return
    for a in set(chr(i) for i in range(97, 123)) - alpha:
        alpha.add(a)
        back(cnt+1)
        alpha.remove(a)


N, K = map(int, input().split())
ans = 0
alpha = {'a', 'n', 't', 'i', 'c'}
words = set(input()[4:-4] for _ in range(N))
if K < 5:
    print(0)
    exit()
if K == 26:
    print(N)
    exit()
back(0)
print(ans)

두 번째 방법 combinations (시간초과)

import sys
from itertools import combinations
input = sys.stdin.readline
N, K = map(int, input().split())
ans = 0
alpha = {'a', 'n', 't', 'i', 'c'}
words = [set(input().strip()[4:-4]) - alpha for _ in range(N)]
available = set(chr(i) for i in range(97, 123)) - alpha
if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    for c in combinations(available, K-5):
        temp = 0
        for word in words:
            if not word - set(c):
                temp += 1
        ans = max(ans, temp)
    print(ans)
'''
