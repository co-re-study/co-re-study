from itertools import permutations


def solution(user_id, banned_id):
    answer = []
    num = len(banned_id)
    for target in list(permutations(user_id, num)):
        count = 0
        for x, y in zip(target, banned_id):
            if len(x) != len(y):
                break
            else:
                for i, j in zip(x, y):
                    # print(i, j)
                    if j == '*':
                        continue
                    if i != j:
                        break
                else:
                    count += 1
        if count == num:
            if sorted(target) not in answer:
                answer.append(sorted(target))
    return len(answer)


print(solution(["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "abc1**"]))


print(solution(["frodo", "fradi", "crodo", "abc123",
      "frodoc"], ["*rodo", "*rodo", "******"]))

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],
      ["fr*d*", "*rodo", "******", "******"]))
