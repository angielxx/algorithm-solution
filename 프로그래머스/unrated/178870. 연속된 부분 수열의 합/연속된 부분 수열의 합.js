function solution(sequence, k) {
    const answer = [-1, -1];
    let s = 0;
    let e = 0;
    let sum = sequence[0]
    while (s <= e && s < sequence.length && e < sequence.length) {
        // console.log(s, e, sum)
        if (sum < k) {
            e++;
            sum += sequence[e];
        } else if (sum > k) {
            sum -= sequence[s];
            s++;
        } else {
            if (answer[0] === -1) {
                answer[0] = s;
                answer[1] = e;
            } else {
                if (e - s < answer[1] - answer[0]) {
                    answer[0] = s;
                    answer[1] = e;
                } else if (e - s === answer[1] - answer[0]) {
                    if (s < answer[0]) {
                        answer[0] = s;
                        answer[1] = e;
                    }
                }
            }
            sum -= sequence[s];
            s++;
        }
    }
    return answer
}