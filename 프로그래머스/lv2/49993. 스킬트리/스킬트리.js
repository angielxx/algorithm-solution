function solution(skill, skill_trees) {
    /*
    BCD CBD CB BD
    */
    const arr = skill.split('');
    const filtered = skill_trees.map((tree) => {
        return tree.split('').filter(str => arr.includes(str)).join('')
    })
    let answer = 0;
    return filtered.filter((tree) => skill.startsWith(tree)).length
}