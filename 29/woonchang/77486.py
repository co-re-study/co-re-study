def solution(enroll, referral, seller, amount):
    answer = [0 for x in range(len(enroll))]
    people = dict()
    for i in range(len(enroll)):
        people[enroll[i]] = i
    for idx in range(len(seller)):
        target = people[seller[idx]]
        profit = amount[idx]*100
        answer[target] += profit
        while referral[target] != "-":
            loss = int(profit*0.1)
            if loss < 1:
                break
            answer[target] -= loss
            answer[people[referral[target]]] += loss
            profit = loss
            target = people[referral[target]]
        if referral[target] == "-":
            answer[target] -= int(profit*0.1)
    return answer
