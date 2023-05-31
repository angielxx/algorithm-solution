function solution(cacheSize, cities) {
    let answer = 0;
    const cache = new Map();
    
    for (let i = 0; i < cities.length; i++) {
        const city = cities[i].toLowerCase();
        // 캐시 히트
        // console.log('city :', city, cache.has(city))
        if (cache.has(city)) {
            cache.delete(city)
            cache.set(city, i);
            answer += 1;
        } else {
            // 캐시 가득
            if (cache.size === cacheSize) {
                // console.log('to delete :', cache.keys().next().value)
                cache.delete(cache.keys().next().value)   
            }
            if (cacheSize > 0) cache.set(city, i)
            answer += 5;
        }
        // console.log(cache)
    }
    return answer
}