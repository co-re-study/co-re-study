def solution(enroll, referral, seller, amount):
    answer = []
    
    recom = dict()
    money = dict()
    
    j = 0
    for i in enroll:
        money[i] = []
        recom[i] = referral[j]
        j += 1
    
    for i in range(len(seller)):
        name = seller[i]
        coin = amount[i]*100
        while True:          
            if name not in recom:
                money[name].append(coin)
                break
            
            elif recom[name] == "-":
                money[name].append(coin - coin//10)
                break
            
            else:
                money[name].append(coin - coin//10)
                name = recom[name]
                coin = coin//10
                if not coin:
                    break
    for i in money:
        answer.append(sum(money[i]))
    return answer