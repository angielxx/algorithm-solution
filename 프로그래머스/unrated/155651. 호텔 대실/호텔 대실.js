function solution(book_time) {
    const sorted = book_time.sort((a, b) => {
        const [ah, am] = a[0].split(':').map(Number);
        const [bh, bm] = b[0].split(':').map(Number);
        if (ah < bh) return -1
        else if (ah > bh) return 1
        else if (ah === bh) {
            if (am < bm) return -1
            else if (am > bm) return 1
            else {
                const [ah, am] = a[1].split(':').map(Number);
                const [bh, bm] = b[1].split(':').map(Number);
                if (ah < bh) return -1
                else if (ah > bh) return 1
                else if (ah === bh) {
                    if (am < bm) return -1
                    else if (am > bm) return 1
                    else return 0
                }
            }
            }
        }
    );
    // const sorted = book_time.sort()

    const table = [];
    
    for (const book of sorted) {
        const [sh, sm] = book[0].split(':').map(Number);
        const [eh, em] = book[1].split(':').map(Number);

        if (!table.length) {
            table.push(endTime(eh, em));
            continue;
        }
        
        let flag = true;
        for (let i = 0; i < table.length; i++) {
            const [h, m] = table[i];
            if (isSameRoom(h, m, sh, sm)) {
                table[i] = endTime(eh, em);
                flag = false;
                break;
            }
        }
        if (flag) table.push(endTime(eh, em));
    }
    return table.length;
}

function endTime(eh, em) {
    if (em + 10 < 60) {
        return [eh, em + 10]
    } else {
        return [eh + 1, em + 10 - 60]
    }
}
    
function isSameRoom(h, m, sh, sm) {
    if (h < sh) return true
    else if (h > sh) return false
    else if (h === sh) {
        if (m <= sm) return true
        else if (m > sm) return false
    }
}