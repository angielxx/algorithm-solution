function solution(weights) {
    // 1:1, 1:2, 2:3, 3:4
    // 1 2 3/2 4/3
    
    const obj = new Map();
    
    const cal = [1, 2, 3/2, 4/3];
    
    let answer = 0;
    
    weights.sort((a, b) => b - a).forEach((w) => {
        cal.forEach((c) => { 
            const target = w * c;
            if (obj.get(target)) {
                answer += obj.get(target);
            }
        })
        
        obj.set(w, obj.get(w)? obj.get(w) + 1 : 1);
    })
    
    return answer
}