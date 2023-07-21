def check(t, i, j):
    global sights

    stack = [(i, j)]

    while stack:
        start_i, start_j = stack.pop()

        sights[start_i][start_j] = "."

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= start_i + di < r and 0 <= start_j + dj < c:
                if matrix[start_i + di][start_j + dj] == t and sights[start_i + di][start_j + dj] != ".":
                    stack.append((start_i+di, start_j+dj))


def end(i, j):
    global sights

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= i + di < r and 0 <= j + dj < c:
            if sights[i + di][j + dj] == "#":
                sights[i+di][j+dj] = "."
    else:
        sights[i][j] = "."


r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
i, j = map(int, input().split())
works = list(input())

direct = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
sights = [["#"]*c for _ in range(r)]

i -= 1
j -= 1
for w in works:
    if w == "W":
        check(matrix[i][j], i, j)
    else:
        di, dj = direct[w]
        i += di
        j += dj

end(i, j)

for el in sights:
    print("".join(el))
