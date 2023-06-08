function solution(topping) {
    let answer = 0;
    
    let left = new Map();
    let right = new Map();
    for (const top of topping) {
        right.set(top, right.get(top)? right.get(top) + 1 : 1);
    }
    console.log(right)
    let i = 0;
    while (i < topping.length) {
        const top = topping[i];
        left.set(top, left.get(top)? left.get(top) + 1 : 1);
        right.set(top, right.get(top) - 1);
        if (right.get(top) === 0) right.delete(top)
        
        if (left.size === right.size) answer++;
        if (left.size > right.size) break;
        
        i++;
    }
    return answer
}