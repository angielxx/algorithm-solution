function solution(number, k) {
    const stack = [];
    const numbers = [...number].map(Number)
    
    let cnt = k;
    for (let num of numbers) {
        if (!stack.length) {
            stack.push(num)
            continue;
        }
        if (cnt > 0) {
            while (stack[stack.length - 1] < num) {
                stack.pop();
                cnt--;
                if (stack.length === 0 || cnt <= 0) break;
            }
        } 
        stack.push(num);
    }
    return stack.splice(0, number.length - k).join('')
}