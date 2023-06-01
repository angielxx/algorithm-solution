function solution(want, number, discount) {
    /*
    슬라이딩 윈도우
    */
    const total = number.reduce((a, b) => a + b);

    const count = {};
    const condition = {};
    for (let i = 0; i < want.length; i++) {
        count[want[i]] = 0;
        condition[want[i]] = number[i];
    }
    
    const slice = discount.slice(0, total);
    slice.forEach((x) => {
        if (want.includes(x)) count[x]++;
    })
    
    // console.log('slice :', slice)
    // console.log('count :', count)
    // 1번째~ 그룹 조건 맞는지 확인
    let flag = true;
    for (const [key, val] of Object.entries(count)) {
        if (val !== condition[key]) {
            flag = false;
            break;
        }
    }
    let answer = 0;
    if (flag) answer++;
    
    for (let i = 0; i < discount.length - total; i++) {
        const remove = discount[i];
        const add = discount[i + total];
        if (count[remove] !== undefined) count[remove]--;
        if (count[add] !== undefined) count[add]++;
        
        let flag = true;
        // console.log('i :', i, remove, add)
        // console.log(count, condition)
        for (const [key, val] of Object.entries(count)) {
            if (val !== condition[key]) {
                flag = false;
                break;
            }
        }
        if (flag) answer++;
    }
    return answer
}