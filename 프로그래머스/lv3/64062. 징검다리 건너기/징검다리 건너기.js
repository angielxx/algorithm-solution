
function solution(stones, k) {
    // 바위를 제거하는 최소의 갯수, 최대의 갯수
    let left = 0;
    let right = 200000000;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        let cnt = 0;
        const arr = [...stones]
        for(let i = 0; i < stones.length; i++) {
            if (arr[i] <= mid) cnt++;
            else cnt = 0;
            
            if (cnt >= k) break;
        }

        if (cnt >= k) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return left
}