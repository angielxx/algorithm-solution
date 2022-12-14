function solution(s) {
    const dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];

    let answer = '';
    let i = 0;
    while (i < s.length) {
        const substr = s.slice(i)
        if (!isNaN(s[i])) {
            answer += s[i]
            i++
        } else {
            for (let j = 0; j < dict.length; j++) {
                if (substr.startsWith(dict[j])) {
                    answer += String(j)
                    i += dict[j].length
                }
            }
        }
        // console.log(answer)
    }
    return Number(answer)
}