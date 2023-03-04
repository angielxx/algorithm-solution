function solution(elements) {
    /*
    7 9 1 1 4, 7 9 1 1 4
    */
    const results = new Set();
    const circle = [...elements, ... elements];
    
    for (let length = 1; length <= elements.length; length++) {
        let start = 0;
        let end = start + length;
        let sum = circle.slice(start, end).reduce((a, b) => a + b);
        while (start < elements.length) {
            results.add(sum);
            sum += circle[end];
            sum -= circle[start];
            start++;
            end++;
        }
    }
    return results.size;
}