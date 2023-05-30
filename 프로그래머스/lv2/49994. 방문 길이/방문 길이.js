function solution(dirs) {
    /*
    ([0,0], [[-1,0]])
    */
    const moveSet = new Set();

    let x = 0;
    let y = 0;
    for (let i = 0; i < dirs.length; i++) {
        const dir = dirs[i];
        let nx = x;
        let ny = y;
        if (dir === 'U') ny++;
        if (dir === 'D') ny--;
        if (dir === 'R') nx++;
        if (dir === 'L') nx--;
        
        if (nx < -5 || nx > 5 || ny < -5 || ny > 5) continue
        
        moveSet.add(`${x}${y}${nx}${ny}`)
        moveSet.add(`${nx}${ny}${x}${y}`)
        // console.log(moveSet)
        x = nx
        y = ny
    }
    return moveSet.size / 2
}