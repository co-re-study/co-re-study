/* readline Module */

// 문제 풀이
function solution(input) {
  // 답변 출력, list
  let peopleNum = input[0][0];
  let pi = input[1];
  pi.sort((a, b) => a - b);
  let addNum = 0;
  let AllNum = 0;
  for (let i = 0; i < pi.length; i++) {
    AllNum += pi[i] + addNum;
    addNum += pi[i];
  }
  console.log(AllNum);
}

/* readline Module */
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let list = [];

rl.on("line", function (line) {
  input.push(line); // 입력받은 여러줄, line
}).on("close", function () {
  // 형변환, 구분자(띄어쓰기)기준으로 배열에 삽입
  input.forEach((val) => {
    list.push(val.split(" ").map((el) => parseInt(el)));
  });

  solution(list); // 문제 풀이 함수 호출
  process.exit(); // 프로세스 종료
});
