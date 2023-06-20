function solution(n, t, m, timetable) {
    // i = 0, 1, ... <  n
    // i번째 도칙시간 = 9:00 + i * t
    // stack = []; -> i번째 도착시간에 셔틀에 탈 수 있는 'HH:MM'
    timetable.sort((a, b) => {
        const ah = Number(a.slice(0, 2));
        const bh = Number(b.slice(0, 2));
        const am = Number(a.slice(3, 5));
        const bm = Number(b.slice(3, 5));
        
        if (ah < bh) return -1
        else if (ah > bh) return 1
        else if (ah === bh) {
            if (am < bm) return -1
            else if (am > bm) return 1
            else return 0
        }
    })
    let i = 0;
    const bus = [];
    let stack = [];
    const time = [];
    let cnt
    while (i < n && timetable.length) {
        cnt = m;
        const hour = 9 + Math.floor((i * t) / 60);
        const min = (i * t) % 60;
        time.push(`${hour < 10? `0${hour}` : hour}:${min < 10? `0${min}` : min}`)

        while (cnt > 0 && timetable.length) {
            const x = timetable[0];
            const xh = Number(x.slice(0, 2));
            const xm = Number(x.slice(3,5));
            
            if (xh < hour || (xh === hour && xm <= min)) {
                stack.push(timetable.shift());
                cnt--;
            } else {
                break;
            }
        }
        bus.push(stack);
        stack = [];
        // console.log(bus)
        i++;
    }
    // cnt가 남은 경우 - 마지막 버스 탑승 시간
    // cnt가 남지 않은 경우
        // 그 전 버스 인원이 있다면 - 마지막 사람의 -1분
    // console.log('cnt :', cnt)
    // console.log('i :', i)
    // console.log(time)
    if (cnt) return time[time.length - 1]
    else {
        const last_bus = bus[bus.length - 1];
        const last = last_bus[last_bus.length - 1];
        let hour = Number(last.slice(0,2));
        let min = Number(last.slice(3.5));
        // console.log('last :', hour, min)
        if (min - 1 < 0) {
            hour--;
            min = 60 + (min - 1);
        } else min--;
        return `${hour < 10? `0${hour}` : hour}:${min < 10? `0${min}` : min}`
    }
}