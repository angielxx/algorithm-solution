function solution(s) {
    let words = s.split(' ');
    let newWords = [];
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        let newWord = '';
        for (let j = 0; j < word.length; j++) {
            if (j == 0) {
                newWord += word[j].toUpperCase();
            } else {
                newWord += word[j].toLowerCase();
            }
        }
        newWords.push(newWord);
    }
    var answer = newWords.join(' ');
    return answer;
}