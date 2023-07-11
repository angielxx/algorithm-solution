function solution(exp) {
    // "100-200*300-500+20"
    // 연산자의 종류를 구한다(set) : -, * , +
    // 완전 탐색
    
    const arr = [];
    let num = ''
    for (const x of exp) {
        if (/[0-9]/.test(x)) {
            num += x
        } else {
            arr.push(Number(num));
            num = '';
            arr.push(x);
        }
    }
    arr.push(Number(num));
    
    const ops = Array.from(new Set(arr.filter(x => ['-', '+', '*'].includes(x))));
    const turns = combi(ops, ops.length);
    
    let answer = 0;
    
    for (const turn of turns) {
        let temp1 = [...arr];
        for (const op of turn) {
            const stack = [];
            const temp = [...temp1];
            while (temp.length) {
                const a = temp.shift();
                if (a === op) {
                    stack.push(cal(op, stack.pop(), temp.shift()))
                } else {
                    stack.push(a)
                }
            }
            temp1 = [...stack];
        }
        if (answer < Math.abs(temp1[0])) answer = Math.abs(temp1[0]);
    }

    return answer
}

function cal(op, num1, num2) {
    if (op === '+') return num1 + num2;
    if (op === '-') return num1 - num2;
    if (op === '*') return num1 * num2;
}

function combi(arr, num) {
    const result = [];
    
    if (num === 1) return arr.map((x) => [x]);
    
    arr.forEach((x, i, origin) => {
        const rest = origin.filter((y, idx) => idx !== i);
        const combine = combi(rest, num - 1).map(z => [x, ...z]);
        result.push(...combine)
    })
    return result
}