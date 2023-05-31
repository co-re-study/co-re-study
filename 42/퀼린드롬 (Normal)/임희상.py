symmetries = {
    'A': 'A',
    'B': False,
    'C': False,
    'D': False,
    'E': '3',
    'F': False,
    'G': False,
    'H': 'H',
    'I': 'I',
    'J': False,
    'K': False,
    'L': False,
    'M': 'M',
    'N': False,
    'O': 'O',
    'P': False,
    'Q': False,
    'R': False,
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    'a': False,
    'b': 'd',
    'c': False,
    'd': 'b',
    'e': False,
    'f': False,
    'g': False,
    'h': False,
    'i': 'i',
    'j': False,
    'k': False,
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'q',
    'q': 'p',
    'r': '7',
    's': False,
    't': False,
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
    'y': False,
    'z': False,
    '0': '0',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '4': False,
    '5': 'Z',
    '6': False,
    '7': 'r',
    '8': '8',
    '9': False
}


def get_letter(letter):
    if symmetries[letter.lower()]:
        return letter.lower()
    if symmetries[letter.upper()]:
        return letter.upper()
    return False


def check_qalindrome(arr):
    if len(arr) == 1:
        if symmetries[arr[0]] == arr[0]:
            return arr[0]

    for i in range(len(arr) // 2 + 1):
        if arr[i] != symmetries[arr[-1 - i]]:
            return False

    return ''.join(arr)


answer = False
target = list(input())

latter = []

for i in range(len(target) - 1, -1, -1):
    target[i] = get_letter(target[i])
    letter = target[i]
    if not letter:
        answer = '-1'
        break
    latter.append(symmetries[letter])

# 문자를 앞 뒤로 추가하며 퀼린드롬이 되는지 확인
if answer:
    print(answer)
else:
    answer = check_qalindrome(target)
    if answer:
        print(answer)
    else:
        for i in range(len(target)):
            answer = check_qalindrome(target + latter[-1 - i:])
            if answer:
                print(answer)
                break
            answer = check_qalindrome(latter[:i + 1] + target)
            if answer:
                print(answer)
                break