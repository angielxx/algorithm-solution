function solution(str1, str2) {

    const arr1 = {};
    const arr2 = {};
    str1 = str1.toLowerCase()
    str2 = str2.toLowerCase()
    const regExp = /^[a-zA-Z]*$/
    for (let i = 0; i < str1.length - 1; i++) {
        const part = str1.slice(i, i+2);
        if (regExp.test(part)) arr1[part] = arr1[part]? arr1[part] + 1 : 1
    }
    for (let i = 0; i < str2.length - 1; i++) {
        const part = str2.slice(i, i+2);
        if (regExp.test(part)) arr2[part] = arr2[part]? arr2[part] + 1 : 1
    }
    console.log(arr1, arr2)
    let union_cnt = 0;
    let sub_cnt = 0;
    const key1 = Object.keys(arr1)
    const key2 = Object.keys(arr2)
    const union = new Set([...key1, ...key2])
    const sub = key1.filter(x => key2.includes(x));
    union.forEach(x => {
        if (key1.includes(x) && key2.includes(x)) {
            union_cnt += Math.max(arr1[x], arr2[x])
        } else if (!key1.includes(x)) {
            union_cnt += arr2[x]
        } else {
            union_cnt += arr1[x]
        }
    })
    sub.forEach(x => sub_cnt += Math.min(arr1[x], arr2[x]))
    // console.log('union_cnt :', union_cnt)
    // console.log('sub_cnt :', sub_cnt)
    if (union_cnt === 0) return 65536
    return Math.floor((sub_cnt / union_cnt) * 65536)
}