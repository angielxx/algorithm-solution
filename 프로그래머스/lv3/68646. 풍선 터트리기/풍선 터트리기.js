function solution(a) {
    const leftMin = Array(a.length).fill(a[0]);
    const rightMin = Array(a.length).fill(a[a.length - 1]);
    
    let left = 1;
    while (left < a.length) {
        let right = a.length - 1 - left;
        leftMin[left] = Math.min(a[left], leftMin[left - 1]);
        rightMin[right] = Math.min(a[right], rightMin[right + 1]);
        left++;
    }

    let answer = a.length;
    for (let i = 0; i < a.length; i++) {
        if (a[i] > leftMin[i] && a[i] > rightMin[i]) answer--;
    }
    return answer;
}