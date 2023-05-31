import sys
input = sys.stdin.readline

def find_parent(person):
    if parent[person] != person:
        return find_parent(parent[person])
    return person

N, M = map(int, input().split())

enemy_dict = dict() # 적대 관계
friend_dict = dict() # 우호 관계
parent = list(range(N))

for _ in range(M):
    p1, p2 = map(lambda x: int(x) - 1, input().split())

    # 부모 갱신
    parent[p1] = find_parent(p1)
    parent[p2] = find_parent(p2)

    # 우호 관계 맺기
    if parent[p1] in friend_dict:
        friend_dict[parent[p1]].add(p1)
    else:
        friend_dict[parent[p1]] = {parent[p1]}
    if parent[p2] in friend_dict:
        friend_dict[parent[p2]].add(p2)
    else:
        friend_dict[parent[p2]] = {parent[p2]}

    # 적대 관계 맺기
    if parent[p1] not in enemy_dict:
        # 둘 다 처음 적대 관계를 맺는다면 서로 적으로 관계 맺기
        if parent[p2] not in enemy_dict:
            enemy_dict[parent[p1]] = find_parent(parent[p2])
            enemy_dict[parent[p2]] = find_parent(parent[p1])
        # p2가 이미 적대 관계가 있다면 p1은 p2의 적대 관계의 부모를 따라가기
        else:
            parent[p1] = find_parent(enemy_dict[parent[p2]])

    else:
        # p1이 이미 적대 관계가 있다면 p2는 p1의 적대 관계의 부모를 따라가기 
        if parent[p2] not in enemy_dict:
            parent[p2] = find_parent(enemy_dict[parent[p1]])
        # 둘 다 이미 적대 관계가 있다면
        else:
            # 둘이 우호 관계인 경우 0 출력 후 종료
            if parent[p2] in friend_dict[parent[p1]] or parent[p1] in friend_dict[parent[p2]]:
                print(0)
                break
            # 둘이 적대 관계인 경우 통과
            if enemy_dict[parent[p1]] == parent[p2] or enemy_dict[parent[p2]] == parent[p1]:
                continue
            # 둘이 관계로 맺어져 있지 않은 경우 우호 및 적대 관계 맺어주기
            friend_dict[parent[p1]] |= friend_dict[enemy_dict[parent[p2]]]
            friend_dict[parent[p2]] |= friend_dict[enemy_dict[parent[p1]]]
            parent[p1], parent[p2] = find_parent(enemy_dict[parent[p2]]), find_parent(enemy_dict[parent[p1]])
    
else:
    print(1)
