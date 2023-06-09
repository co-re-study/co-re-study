def solution(n, info):
    answer = [-1]
    my_scores = [0] * 11
    sc_diff = 0

    def shoot(depth, arrows):
        nonlocal answer, my_scores, sc_diff
        if depth == 11:
            if arrows == n:
                me = 0
                enemy = 0
                for i in range(10):
                    if my_scores[i] > info[i]:
                        me += 10 - i
                    else:
                        if info[i]:
                            enemy += 10 - i
                if me > enemy:
                    if me - enemy > sc_diff:
                        answer = my_scores[:]
                        sc_diff = me - enemy
                    elif me - enemy == sc_diff:
                        for i in range(10, 0, -1):
                            if answer[i] > my_scores[i]:
                                break
                            if my_scores[i] > answer[i]:
                                answer = my_scores[:]
                                break
            return
        if depth == 10:
            my_scores[depth] = n - arrows
            shoot(depth+1, n)
            my_scores[depth] = 0
            return

        if n - arrows > info[depth]:
            my_scores[depth] += info[depth] + 1
            shoot(depth+1, arrows + info[depth] + 1)
            my_scores[depth] -= info[depth] + 1
        shoot(depth+1, arrows)

    shoot(0, 0)

    return answer