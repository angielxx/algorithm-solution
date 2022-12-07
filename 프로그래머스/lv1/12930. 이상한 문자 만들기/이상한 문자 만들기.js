function solution(s) {
    function changeAlphabet(array) {
        for (let i = 0; i < array.length; i++) {
            if (i%2 === 0) array[i] = array[i].toUpperCase()
            else array[i] = array[i].toLowerCase();
        }
        return array
    }
    
    let answer = s.split(' ').map((word) => {
        let arr = Array.from(word);
        arr = changeAlphabet(arr)
        return arr.join('')
    })
    return answer.join(' ')
}