function solution(s) {
    const answer = [];
    let str = s;
    while (str.length) {
        const x = str[0];
        let isX = 1;
        let isNotX = 0;
        for (let i = 1; i < str.length; i++) {
            if (x === str[i]) isX++;
            else if (x !== str[i]) isNotX++;
            if (isX === isNotX) {
                answer.push(str.slice(0, i + 1));
                str = str.slice(i + 1);
                break;
            }
        }
        if (isX !== isNotX ) {
            answer.push(str);
            break;
        }
    }
    return answer.length
}