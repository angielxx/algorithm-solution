function solution(today, terms, privacies) {
    const [y, m, d] = today.split('.').map(Number);
    
    const terms_d = {};
    for (const term of terms) {
        const [a, b] = term.split(' ');
        terms_d[a] = Number(b);
    }
    
    const answer = [];
    for (let i = 0; i < privacies.length; i++) {
        const [day, term] = privacies[i].split(' ');
        let [sy, sm, sd] = day.split('.').map(Number);
        
        const a = Math.floor(terms_d[term] / 12);
        const b = terms_d[term] % 12;
        
        sy += a;
        sm += b;
        if (sm > 12) {
            sm -= 12;
            sy++;
        }

        if (sy < y) {
            answer.push(i + 1);
            continue
        }
        if (y < sy) {
            continue
        }
        if (sm < m) {
            answer.push(i + 1);
            continue
        }
        if (m < sm) {
            continue
        }
        if (sd <= d) {
            answer.push(i + 1);
        }
    }

    return answer
}