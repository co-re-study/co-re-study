const fs = require("fs");
const [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let [stack, ans] = [[], 0];

for (const i in input) {
  if (!stack.length) {
    stack.push(input[i]);
  } else {
    now = stack.pop();
    if (now === input[i]) {
      stack.push(now);
      stack.push(input[i]);
    }
  }
  if (ans < stack.length) {
    ans = stack.length;
  }
}
stack.length ? console.log(-1) : console.log(ans);
