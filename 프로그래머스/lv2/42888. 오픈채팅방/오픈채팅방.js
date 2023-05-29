function solution(record) {
    /*
    [유저아이디]의 닉네임 변경사항을 추적
    uid1234 : Muzi - Prodo
    uid4567 : Prodo - Ryan
    */
    const ment = [];  // ${id}님이 ~했습니다.
    const nicknames = {};  // id : nickname
    for (let r of record) {
        const arr = r.split(' ');
        const id = arr[1];
        if (arr[0] === 'Enter') {
            ment.push([id, `님이 들어왔습니다.`])
            nicknames[id] = arr[2]
        } else if (arr[0] === 'Leave') {
            ment.push([id, `님이 나갔습니다.`])
        } else if (arr[0] === 'Change') {
            nicknames[id] = arr[2]
        } 
    }
    const answer = []
    ment.forEach((m) => {
        const id = m[0];
        const str = m[1];
        answer.push(nicknames[id] + str)
    })

    return answer
}