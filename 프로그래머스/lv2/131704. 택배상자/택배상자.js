function solution(order) {
    const stack = [];
    let cnt = 0;
    let i = 1;
    while (i <= order.length) {
        stack.push(i);
        while (stack.length > 0 && stack[stack.length - 1] == order[cnt]) {
            cnt++;
            stack.pop();
        }
        i++;
    }
    return cnt
}