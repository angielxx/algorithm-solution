function solution(progresses, speeds) {
    /*
    [7, 70, 45]
    [7, 3, 9]
    
    [5, 10, 1, 1, 20, 1]
    1 
    */
    const answer = [];
    
    for (let i = 0; i < progresses.length; i++) {
        progresses[i] = Math.ceil((100 - progresses[i]) / speeds[i])
    }
    
    let cnt = progresses[0];
    let days = 1;
    let i = 1;
    while(i < progresses.length) {
        if (progresses[i] <= cnt) days++
        else {
            answer.push(days);
            cnt = progresses[i];
            days = 1
        }
        i++;
    }
    answer.push(days)
    return answer
}