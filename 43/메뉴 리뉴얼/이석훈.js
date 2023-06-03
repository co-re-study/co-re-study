function solution(orders, course) {
  let orderLetters = [];
  let allNumArr = [];
  let Ans = [];
  //각 요소에 포함된 문자를 오름차순으로 정렬

  for (let i = 0; i < orders.length; i++) {
    let sortArr = [];
    let element = orders.shift();
    for (let k = 0; k < element.length; k++) {
      sortArr.push(element[k]);
    }
    orderLetters.push(sortArr.sort());

    orders.push(sortArr.join(""));
  }

  for (let i = 0; i < orderLetters.length; i++) {
    let k = 0;
    allNumArr.push([]);
    allNumArr[i].push([]);
    for (let p = 0; p < orderLetters[i].length; p++) {
      allNumArr[i][0].push([orderLetters[i][p]]);
    }

    while (k !== orderLetters[i].length) {
      allNumArr[i].push([]);
      for (let j = 0; j < allNumArr[i][k].length; j++) {
        let compareArr = allNumArr[i][k].shift();
        for (let p = 0; p < orderLetters[i].length; p++) {
          if (!compareArr.includes(orderLetters[i][p])) {
            allNumArr[i][k + 1].push([...compareArr, orderLetters[i][p]].sort().join(""));
          }
        }
        allNumArr[i][k + 1] = [...new Set(allNumArr[i][k + 1])];
        allNumArr[i][k].push(compareArr);
      }
      k++;
    }
    //마지막 빈 배열 삭제
    allNumArr[i].pop();
  }

  for (let i = 0; i < course.length; i++) {
    let ansArr = [];
    for (let k = 0; k < allNumArr.length; k++) {
      if (allNumArr[k][course[i] - 1]) {
        ansArr.push(allNumArr[k][course[i] - 1]);
      }
    }
    ansArr = ansArr.flat().sort();

    if (ansArr.length >= 2) {
      let numArr = [[ansArr[0], 1]];
      for (let j = 1; j < ansArr.length; j++) {
        if (numArr[numArr.length - 1][0] !== ansArr[j]) {
          numArr.push([ansArr[j], 1]);
        } else if (numArr[numArr.length - 1][0] === ansArr[j]) {
          numArr[numArr.length - 1][1] += 1;
        }
      }
      numArr = numArr.sort((a, b) => b[1] - a[1]);
      console.log(numArr);
      if (numArr[0][1] >= 2) {
        Ans.push(numArr[0][0]);
        for (let e = 1; e < numArr.length; e++) {
          if (numArr[0][1] === numArr[e][1]) {
            Ans.push(numArr[e][0]);
          }
        }
      }
    }
  }

  return Ans.sort();
}
