function solution(genres, plays) {
    // cnt = 장르 : 재생횟수
    // song = 장르 : [고유번호...]
    const cnt = new Map();
    const song = new Map();
    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i]
        cnt.set(genre, cnt.has(genre) ? cnt.get(genre) + play : play)
        song.set(genre, song.has(genre) ? [...song.get(genre), i] : [i])
        // console.log(cnt)
        // console.log(song)
    }
    const genre_arr = Array.from(cnt.keys()).sort((a,b) => cnt.get(b) - cnt.get(a))
    let answer = []
    for (let i = 0; i < genre_arr.length; i++) {
        const genre = genre_arr[i];
        const candidates = song.get(genre)
        // console.log(candidates)
        candidates.sort((a, b) => {
            if (plays[a] - plays[b] > 0) return - 1
            if (plays[a] - plays[b] < 0) return 1
            if (plays[a] - plays[b] === 0) {
                if (a  - b) return 1
                else return -1
            }
        })
        // console.log(candidates)
        answer = [...answer, ...candidates.slice(0,2)]
    }
    return answer
}