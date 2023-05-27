import sys
input = sys.stdin.readline

def comb(sidx, idx):
    global answer

    if sidx == K - 5:
        tmp = 0
        alphabet_set = set(selection)
        for word in words:
            for char in words[word]:
                if char not in alphabet_set:
                    break
            else:
                tmp += 1
        if tmp > answer:
            answer = tmp
        return
    
    if idx == 21:
        return
    
    selection[sidx] = alphabets[idx]
    comb(sidx+1, idx+1)
    comb(sidx, idx+1)


N, K = map(int, input().split())
if K < 5:
    print(0)
    exit(0)

# 각 단어가 갖고 있는 알파벳 set 구하기
words = dict()
for _ in range(N):
    word = input().strip()
    alphabet_set = set()
    for char in word:
        if char not in {"a", "n", "t", "c", "i"}:
            alphabet_set.add(char)
    words[word] = alphabet_set

# "a", "n", "t", "c", "i" 제외한 나머지 알파벳에 대해 모든 조합 구하기
selection = [""] * (K - 5)
alphabets = ["b", "d", "e", "f", "g", "h", "j", "k", "l", "m",
             "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"]

answer = 0
comb(0, 0)
print(answer)