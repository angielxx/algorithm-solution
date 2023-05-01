function solution(sticker) {
    if (sticker.length === 1) return sticker[0]
    const dp1 = Array.from({ length: sticker.length }, _=> 0);  // 첫번째 스티커 사용
    const dp2 = Array.from({ length: sticker.length }, _=> 0);  // 첫번째 스티커 사용x
    
    dp1[0] = sticker[0];
    dp1[1] = sticker[0]; 
    
    dp2[1] = sticker[1];
    
    // dp1 : 마지막 스티커는 사용 불가
    // dp2 : 마지막 스티커 사용 가능
    for (let i = 2; i < sticker.length - 1; i++) {
        dp1[i] = Math.max(dp1[i-2] + sticker[i], dp1[i-1]);
    }
    for (let i = 2; i < sticker.length; i++) {
        dp2[i] = Math.max(dp2[i-2] + sticker[i], dp2[i-1]);
    }
    
    const val1 = Math.max(...dp1);
    const val2 = Math.max(...dp2);
    
    return Math.max(val1, val2)
}