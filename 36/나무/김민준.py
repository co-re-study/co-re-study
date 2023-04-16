N, tree = map(int,input().split(' '))

tree_list = sorted(list(map(int,input().split(' '))),reverse=1)

diff_list = [ 0 for _ in range(N) ]
#차이 저장하는 리스트
for i1 in range(1,N):
    diff_list[i1-1] = tree_list[i1-1] - tree_list[i1]
diff_list.append(tree_list[-1])

sum_tree = 0
ans = 0
if len(tree_list) == 1:
    ans = tree_list[0]
    print(tree_list[0]-ans)
#걸렀을 경우
else:
    for i2 in range(len(diff_list)):
        if diff_list[i2] != 0:
            #해당 인덱스 사정거리에 들어옴
            if sum_tree + diff_list[i2]*(i2+1) >= tree:
                if ((tree - sum_tree)%(i2+1)==0 ):
                    ans += (tree - sum_tree)//(i2+1)
                else:
                    ans += ((tree - sum_tree) // (i2 + 1))+1
                if (i2 + 1) != N:
                    print(ans)
                else:
                    print(tree_list[0] - ans)
                break
            else:
                sum_tree += diff_list[i2] * (i2 + 1)
                ans += diff_list[i2]

###못품....