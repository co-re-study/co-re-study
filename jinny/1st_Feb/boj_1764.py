#듣보잡
N, M = map(int, input().split())
namespace = set()
answer = []
for _ in range(N):
    namespace.add(input())
for _ in range(M):
    name = input()
    if name in namespace:
        answer.append(name)
answer.sort()
print(len(answer))
print("\n".join(answer))