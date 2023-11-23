function solution(play_time, adv_time, logs) {
    
    const strToSec = (time) => {
        const [h, m, s] = time.split(':').map(Number);
        return s + m * 60 + h * (60 * 60)
    }
    
    const secToStr = (sec) => {
        let h = Math.floor(sec / (60 * 60));
        sec -= h * 60 * 60;
        let m = Math.floor(sec / 60);
        sec -= m * 60;
        let s = sec;
        
        h = String(h).padStart(2, '0');
        m = String(m).padStart(2, '0');
        s = String(s).padStart(2, '0');
        
        return `${h}:${m}:${s}`;
    }
    
    const total = strToSec(play_time);
    const adv = strToSec(adv_time);
    
    logs = logs.map(log => log.split('-').map(strToSec));
    
    const timeline = Array.from({length:total+1}, _=>0);
    for (let log of logs) {
        const [s, e] = log;
        timeline[s]++;
        timeline[e]--;
    }
    
    for (let i = 1; i < total+1; i++) {
        timeline[i] += timeline[i-1];
    }
    for (let i = 1; i < total+1; i++) {
        timeline[i] += timeline[i-1];
    }

    let currSum = timeline[adv];
    let end = adv;
    let answer = 0;
    
    for (let i = end; i < total+1; i++) {
        const tempSum = timeline[i] - timeline[i - adv];
        if (tempSum > currSum) {
            currSum = tempSum;
            answer = i - adv + 1;
        }
    }

    return secToStr(answer)
}