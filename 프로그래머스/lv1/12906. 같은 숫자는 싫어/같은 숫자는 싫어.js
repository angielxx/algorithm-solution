function solution(arr){
    if (!arr.length) return arr;
    
    let current_num = arr[0];
    let answer = [arr[0]];
    for (let i = 1; i < arr.length; i++){
        if (arr[i] !== current_num) {
            answer.push(arr[i])
            current_num = arr[i]
        }
    }
    return answer
}