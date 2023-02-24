def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    parents = {}
    children = {'-': set()}
    idx_dict = {}
    for i in range(len(enroll)):
        idx_dict[enroll[i]] = i
        parents[enroll[i]] = referral[i]
        if referral[i] in children.keys():
            children[referral[i]].add(enroll[i])
        else:
            children[referral[i]] = {enroll[i]}

    for i in range(len(seller)):
        person = seller[i]
        left = 100 * amount[i]
        current = person
        while left and current != '-':
            bribe = int(left * 0.1)
            answer[idx_dict[current]] += left - bribe
            current = parents[current]
            left = bribe

    print(answer)
    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
         ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])