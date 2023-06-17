- 방법 : 효율성 없이 그냥 찾기

```swift

func solution(_ info:[String], _ query:[String]) -> [Int] {
    // 정보 처리
    var infoList = info.map { $0.components(separatedBy: " ") }

    // 쿼리 처리
    var queryList = query.map { $0.replacingOccurrences(of: " and ", with: " ").components(separatedBy: " ") }

    var answer = [Int]()
    // 각 쿼리에 대한 처리
    for q in queryList {
        var count = 0
        for i in infoList {
            // 각 항목 검사 (언어, 직군, 경력, 소울푸드, 점수)
            if (q[0] == "-" || q[0] == i[0]) &&
                (q[1] == "-" || q[1] == i[1]) &&
                (q[2] == "-" || q[2] == i[2]) &&
                (q[3] == "-" || q[3] == i[3]) &&
                Int(q[4])! <= Int(i[4])! {
                    count += 1  // 모든 조건이 맞으면 카운터 증가
            }
        }
        answer.append(count)
    }

    return answer
}

```

- 방법 : 가능한 모든 쿼리를 전부 만듬. 그것을 키로 설정하고 값에 점수를 담는다. 이 점수 배열을 정렬하고 안에서 이진탐색을 진행한다.

```swift

func solution(_ info:[String], _ query:[String]) -> [Int] {
    var infoDict: [String: [Int]] = [:]
    let languages = ["cpp", "java", "python", "-"]
    let positions = ["backend", "frontend", "-"]
    let careers = ["junior", "senior", "-"]
    let foods = ["pizza", "chicken", "-"]

    for language in languages {
        for position in positions {
            for career in careers {
                for food in foods {
                    let key = "\(language) \(position) \(career) \(food)"
                    infoDict[key] = []
                }
            }
        }
    }

    for i in info {
        let splitInfo = i.split(separator: " ")
        let score = Int(splitInfo[4])!
        for language in [String(splitInfo[0]), "-"] {
            for position in [String(splitInfo[1]), "-"] {
                for career in [String(splitInfo[2]), "-"] {
                    for food in [String(splitInfo[3]), "-"] {
                        let key = "\(language) \(position) \(career) \(food)"
                        infoDict[key]?.append(score)
                    }
                }
            }
        }
    }

    for key in infoDict.keys {
        infoDict[key]?.sort()
    }

    var answer = [Int]()
    for q in query {
        let splitQuery = q.split(separator: " ")
        let score = Int(splitQuery[7])!
        let key = "\(splitQuery[0]) \(splitQuery[2]) \(splitQuery[4]) \(splitQuery[6])"

        if let scores = infoDict[String(key)] {
            let scoreCount = scores.count
            let overScoreIndex = binarySearch(scores, score)
            let overScoreCount = scoreCount - overScoreIndex
            answer.append(overScoreCount)
        } else {
            answer.append(0)
        }
    }
    return answer
}

func binarySearch(_ arr: [Int], _ target: Int) -> Int {
    var start = 0
    var end = arr.count - 1

    while start <= end {
        let mid = (start + end) / 2

        if arr[mid] < target {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }

    return start
}

```
