function solution(n)
{
    const str = String(n);
    let arr = Array.from(str)
    arr = arr.map((el) => {
        return parseInt(el)
    })
    return arr.reduce((acc, cur) => acc + cur)
}