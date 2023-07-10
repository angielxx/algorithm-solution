function solution(p) {
    if (p === '') return ''
    if (isRight(p)) return p
    
    const result = recur(p);
    return result
}

function recur(w) {
    // console.log('w :', w)
    if (w === '') return ''

    const [u, v] = split(w);
    // console.log('u, v :', u, v)
    // console.log()
    if (isRight(u)) {
        // console.log('here', u + recur(v))
        return u + recur(v)
    } else {
        let temp = '(' + recur(v) + ')' + reverse(u.slice(1, u.length - 1));
        // console.log('temp :', temp)
        return temp
    }
}

// 2. w를 두 "균형잡힌"으로 분리
function split(str) {
    let cnt1 = 0;
    let cnt2 = 0;
    let i = 0;
    while (i < str.length) {
        if (str[i] === '(') cnt1++;
        if (str[i] === ')') cnt2++;
        
        if (cnt1 === cnt2) break;
        i++
    }
    return [str.slice(0, i + 1), str.slice(i + 1)]
}

// 3. "올바른"인지
function isRight(str) {
    const stack = [];
    let result = true;
    for (const s of str) {
        if (s === '(') {
            stack.push('(')
        } else {
            if (stack[stack.length - 1] === '(') stack.pop();
            else {
                result = false;
                break;
            }
        }
    }
    if (stack.length) result = false;
    return result
}

function reverse(str) {
    let result = '';
    for (const s of str) {
        if (s === '(') result += ')';
        else if (s === ')') result += '(';
    }
    return result
}