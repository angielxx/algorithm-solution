function solution(arr) {
    var answer = 0;
    answer = arr.reduce((pre, cur) => pre + cur) / arr.length
    return answer;
}