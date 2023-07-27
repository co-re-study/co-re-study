import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input().rstrip()

    fp = 0
    bp = len(s) - 1
    cnt = 0
    while fp < bp:

        if s[fp] == s[bp]:
            fp += 1
            bp -= 1

        elif s[fp] != s[bp]:
            a = s[fp:bp]
            b = s[fp+1:bp+1]

            if a == a[::-1] or b == b[::-1]:
                cnt = 1
                break
            else:
                cnt = 2
                break
    print(cnt)

