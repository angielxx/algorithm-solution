function solution(n, m, section) {
    /*
    section : [2,3,6]
    visited : [0,0,0]
    start = 2
    end = 2 + m - 1
    end보다 큰 숫자가 나오면 다음 반복으로
    start = 방문처리가 안된 제일 처음 구역 번호
    */
    
    const visited = Array(section.length).fill(0);
    // 페인트칠 범위의 시작 인덱스
    let start = 0;
    
    // 페인트칠해야 하는 최소 횟수
    let cnt = 0;
    
    // 한 반복당 페인트칠 1회
    while (start < section.length) {
        cnt++;
        // console.log(start, cnt)
        // 이번 페인트칠에서 칠할 수 있는 가장 마지막 구역의 번호
        const max_sec = section[start] + m - 1;
        for (var i = start; i < section.length; i++) {
            if (section[i] <= max_sec) {
                visited[i]++;
            } else {
                break;
            }
        }
        start = i;
    }
    return cnt;
}