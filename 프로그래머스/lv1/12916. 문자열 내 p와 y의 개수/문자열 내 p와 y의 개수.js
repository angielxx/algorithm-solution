function solution(s){
    let cnt_p = 0;
    let cnt_y = 0;
    for (let i = 0; i < s.length; i++) {
        const char = s[i].toLowerCase();
        if((char === 'p') ) cnt_p++;
        if(char === 'y') cnt_y++;
    }
    if ((cnt_p === cnt_y) || (!cnt_p && !cnt_y)) {
        return true;
    } else {
        return false;
    }
}