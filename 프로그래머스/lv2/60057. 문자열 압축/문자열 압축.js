function solution(s) {
    let answer = s.length;
    
    let length = 1;
    while (length <= Math.ceil(s.length / 2)) {
    // while (length <= 2) {
        
        let str = '';
        
        let i = 0;
        let cnt = 1;
        let temp = '';
        while (i < s.length) {
            if (s.slice(i, i + length) !== s.slice(i+length, i + 2*length)) {
                if (cnt > 1) {
                    str += `${cnt}${temp}`;
                    cnt = 1;
                    i += length;
                } else {
                    str += s.slice(i, i + length);        
                    i += length;    
                }
            } else {
                cnt += 1;
                temp = s.slice(i, i + length);
                i += length;
            }
        }
        if (cnt > 1) {
            str += `${cnt}${temp}`;
            cnt = 1;
        }

        if (str.length < answer) {
            answer = str.length}
        length += 1;
    }
    return answer
}