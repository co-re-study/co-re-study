from collections import defaultdict

def solution(enroll, referral, seller, amount):
    referral_set = defaultdict(str)
    amount_set = defaultdict(int)
    answer_set = defaultdict(int)
    answer = []
    #순서쌍 구하기 {하위: 부모}
    for i in range(len(enroll)):
        referral_set[enroll[i]] = referral[i]

    #seller에 있는 사람을 referral_set에서 찾아서
    #이것을 "-"만나게 되면 center에 10퍼를 누적하고 끝
    for k in range(len(seller)):
        #상위에 사람이 있으면 루프 돌기
        tmp = amount[k]*100
        tmp_upper = 0
        receive_name = seller[k]
        # 돌기
        while True:
            if tmp != 0 :
                if referral_set[receive_name] == "-":
                    tmp_upper = int(tmp*0.1)
                    answer_set[receive_name] +=  (tmp - tmp_upper)
                    break
                else:
                    tmp_upper = int(tmp*0.1)
                    answer_set[receive_name] +=  + (tmp - tmp_upper)
                    # answer_set[referral_set[receive_name]] = answer_set.get(referral_set[receive_name], 0) + int(tmp*0.1)
                    tmp = tmp_upper
                    receive_name = referral_set[receive_name]
            else:
                break
    for l in enroll:
        answer.append(answer_set[l])


    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young" ,"john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))
