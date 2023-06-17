function solution(A, B) {
    /*
    2 - 1
    2 - 1
    6 - 1 3 5 (여러 개에 가능할 때는 작은 수를 먼저)
    8 - 1 3 5 7
    
    5 - 8 : WIN
    1 - 2 : WIN
    3 - 6 : WIN
    7
    7 5 3 1 / 8 6 2 2 
    9 5 3 1 / 8 6 2 2
    */
    const sortedA = A.sort((a, b) => b - a);
    const sortedB = B.sort((a, b) => b - a);
    
    let a = 0;
    let b = 0;
    let answer = 0;
    while (a < A.length && b < B.length) {
        if (A[a] < B[b]) {
            answer++;
            a++;
            b++;
        } else if (A[a] >= B[b]) {
            a++;
        }
    }
    return answer;
}