function solution(word) {
    const dict = {};
    const vowels = [..."AEIOU"];
    let index = 0;
    function dfs(now) {
        if (now.length > 5) return;
        dict[now] = index++;
        vowels.forEach((vowel) => dfs(now + vowel))
    }
    dfs('', 0)
    return dict[word]
}