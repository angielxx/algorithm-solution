function solution(m, musicinfos) {
    let max_len = 0;
    let answer = '';
    
    for (let music of musicinfos) {
        const arr = music.split(',')
        const [sh, sm] = arr[0].split(':').map(Number);
        const [eh, em] = arr[1].split(':').map(Number);
        
        const len = 60 * (eh - sh) + em - sm;
        const target = toArr(m);
        const song = toArr(arr[3]);
        const temp = arr[3].repeat(Math.floor(len / song.length)) + song.slice(0, len % song.length).join('');
        const play = toArr(temp);
        
        for (let i = 0; i <= play.length - target.length; i++) {
            if (play.slice(i, i + target.length).join('') === m) {
                if (max_len < len) {
                    max_len = len;
                    answer = arr[2];
                }
                break;
            }
        }
    }
    if (max_len === 0) return '(None)'
    return answer
}

function toArr(str) {
    return str.split('').map((x, i) => {
        if (i + 1 < str.length && str[i + 1] === '#') {
            return x + '#'
        } else return x
    }).filter(x => x !== '#')
}