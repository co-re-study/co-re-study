# 반음
import sys
input = sys.stdin.readline

piano = ['A', 0, 'B', 'C', 0, 'D', 0, 'E', 'F', 0, 'G', 0]
n = int(input())
music = []
for _ in range(n):
    music.append(int(input()))
for i in range(len(piano)):
    if piano[i]:
        now = i
        for play in music:
            now += 12 + play
            if not piano[now % 12]:
                break
        else:
            print(piano[i], piano[now % 12])
