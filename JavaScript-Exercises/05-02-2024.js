/*
 * There exists a staircase of N steps, and you can climb up either 1 or 2
 * steps at a  time. Given N, write a function that returns of the number
 * of unique ways you can climb the staircase. The order of the steps matters.
 * 
 * For example if N is 4, there are 5 unique ways:
 * 1, 1, 1, 1
 * 2, 1, 1
 * 1, 2, 1
 * 1, 1, 2
 * 2, 2
 */

let N = 4
let diffWays = [];
diffWays[1] = 1;
diffWays[2] = 2;

for (let i = 3; i <= N; i++) {
    diffWays[i] = diffWays[i-1] + diffWays[i-2];
}

console.log(diffWays[N])