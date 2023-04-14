function solution(participant, completion) {
    // 이름 : 인원
    const map = new Map();
    
    for (let name of participant) {
        const total = map.get(name)? map.get(name) + 1 : 1
        map.set(name, total)
    }
    
    for (let name of completion) {
        const total = map.get(name) - 1
        map.set(name, total)
    }
    let answer;
    map.forEach((val, key) => {
        if (val > 0) answer = key
    })

    return answer
}