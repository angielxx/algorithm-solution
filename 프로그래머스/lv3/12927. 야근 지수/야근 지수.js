function solution(n, works) {
    // 야근 피로도 = 야근 시작 지점 작업량 + 남은 일의 작업량 ^ 2
    // n 시간동안 야근 피로도 최소화, 1시간에 작업량 1
    // 야근 피로도가 최소가 되려면 각 남은 작업량의 숫자가 편차가 적어야 함
    /*
    내림차순으로 정렬
    제일 큰 수를 -1
    n--;
    */
    const arr = works.sort((a, b) => b - a);

    while ( n > 0) {
        const max = arr[0];
        if (max === 0) break;
        
        for (let i = 0; i < works.length; i++) {
            if (arr[i] >= max) {
                arr[i]--;
                n--;
            }
            else if (arr[i] < max) break;
            if (n === 0) break;
            // console.log(arr, n)
        }
    }
    // console.log(arr)
    return arr.reduce((a, b) => a + b ** 2, 0)
}