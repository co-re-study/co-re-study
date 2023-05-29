mirror = {'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'v': 'V',
          'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', 'b': 'd', 'd': 'b', 'i': 'i', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'q', 'q': 'p', 'r': '7', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', '0': '0', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '7': 'r', '8': '8'}


def convert(x):
    return [mirror[i] for i in x]


def check(x):
    for i in range(len(x)):
        if mirror.get(x[i].lower()):
            x[i] = x[i].lower()
        elif mirror.get(x[i].upper()):
            x[i] = x[i].upper()
        else:
            print(-1)
            exit()
    return


def quilindrom(x):
    for i in range(len(x)//2+1):
        if x[i] != mirror.get(x[-1-i]):
            return False
    return ''.join(x)


S = list(input())
check(S)
for i in range(len(S), -1, -1):
    ans = quilindrom(S+convert(S[::-1][i:]))
    if ans:
        print(ans)
        break
    ans = quilindrom(convert(S[i:][::-1])+S)
    if ans:
        print(ans)
        break