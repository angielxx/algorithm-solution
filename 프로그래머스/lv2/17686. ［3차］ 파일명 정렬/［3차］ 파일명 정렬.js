function solution(files) {
    /*
    head = {}, number = {}, tail = {}
    key : index, value : Head, number, tail
    */    
    const HEAD = {};
    const NUMBER = {};
    const TAIL = {};
    
    const number_reg = /[0-9]/;
    
    for (let i = 0; i < files.length; i++) {
        const name = files[i]
        const file = files[i].split('');
        
        let idx;
        let last_idx;
        let number = '';
        let flag = false;
        
        for (let j = 0; j < file.length; j++) {
            if (number_reg.test(file[j])) {
                if (!flag) idx = j;
                if (!flag) flag = true;
                last_idx = j;
                number += file[j];
            }
            if (flag && !number_reg.test(file[j])) break;
        }
        HEAD[name] = file.slice(0, idx).join('');
        NUMBER[name] = number;
        TAIL[name] = file.slice(last_idx + 1).join('');
    }
    // console.log(HEAD, NUMBER, TAIL)
    const answer = files.sort((a, b) => {
        // 사전순
        if (HEAD[a].toLowerCase() < HEAD[b].toLowerCase()) return -1;
        else if (HEAD[a].toLowerCase() > HEAD[b].toLowerCase()) return 1;
        // 숫자순
        if (Number(NUMBER[a]) < Number(NUMBER[b])) return -1
        else if (Number(NUMBER[a]) > Number(NUMBER[b])) return 1;
        // else
        if (files.indexOf(a) < files.indexOf(b)) return -1;
        else if (files.indexOf(a) > files.indexOf(b)) return 1;
        else return 0;
    })
    return answer
}