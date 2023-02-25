def solution(enroll, referral, seller, amount):
    
    # 돈 분배 함수
    def split_money(idx, money):
        
        # center에 도달하면 종료
        if idx == -1:
            return
        
        current_person = enroll[idx]
        
        # 더이상 나눌 수 없으면 다 갖기
        if money * 0.1 < 1:
            answer[person_dict[current_person]] += money
            return
        
        # 자기 몫만 남기고 위로 보내기
        answer[person_dict[current_person]] += money - int(money * 0.1)
        split_money(parent[idx], int(money * 0.1))
    
    answer = [0] * len(enroll)
    
    # person_dict
    # key: 사람 이름 / value: 인덱스
    person_dict = dict()
    for idx in range(len(enroll)):
        person = enroll[idx]
        person_dict[person] = idx
    
    # 부모 인덱스를 가리키는 parent 리스트 생성
    parent = [0] * len(enroll)
    for idx in range(len(referral)):
        person = referral[idx]
        if person == "-":
            parent[idx] = -1
        else:
            parent[idx] = person_dict[person]
            
    # 판매 시작 노드부터 돈 분배
    for idx in range(len(seller)):
        person = seller[idx]
        split_money(person_dict[person], amount[idx] * 100)
            
    return answer