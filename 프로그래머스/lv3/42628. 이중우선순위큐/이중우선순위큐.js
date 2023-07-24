function solution(operations) {
    let heap = [];
    
    operations.forEach(op => {
        const [a, b] = op.split(' ');
        
        if (a === 'I') {
            heap.push(Number(b));
        }
        else {
            if (b == 1) {
                const idx = heap.indexOf(Math.max(...heap));
                heap = heap.slice(0, idx).concat(heap.slice(idx + 1));
            } else {
                const idx = heap.indexOf(Math.min(...heap));
                heap = heap.slice(0, idx).concat(heap.slice(idx + 1));
            }
        }
    })
    return heap.length? [Math.max(...heap), Math.min(...heap)] : [0,0];
}