s = input().strip()
bomb = input().strip()

stack = []
bomb_len = len(bomb)

for char in s:
    stack.append(char)
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        for _ in range(bomb_len):
            stack.pop()

result = ''.join(stack)
if result:
    print(result)
else:
    print("FRULA")
