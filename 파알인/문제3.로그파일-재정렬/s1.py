# 937. Reorder Data in Log Files
# 220815

"""
틀린 테스트케이스
["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
문자들이 같은 경우
["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]
"""
logs = ["27 85717 7", "2 y xyr fc", "52 314 99", "d 046099 0", "m azv x f", "7e apw c y", "8 hyyq z p", "6 3272401", "c otdk cl", "8 ksif m u"]

N = len(logs)

dig = list()
let_dict = dict()

for i in range(N):
    contents = logs[i].split()
    iden = contents.pop(0)
    if contents[-1].isalpha():
        let_dict[iden] = ' '.join(contents)
    else:
        dig.append(logs[i])

# value들(리스트 [act, car]) 저장해놓은 리스트
# sorted하면 알파벳 순으로 정렬됨
# 순서대로 조회해서 맞는 key랑 붙여서 output 리스트에 넣는다.
vals = sorted(let_dict.values())
keys = sorted(let_dict.keys())

print('val', vals)
print('key', keys)
# 최종 정렬하여 넣을 리스트
output = list()

for i in range(len(vals)):
    val = vals.pop(0)
    j = 0
    while j < len(keys):
        if let_dict[keys[j]] == val:
            key = keys.pop(j)
            output.append(key + ' ' + val)
        else:
            j += 1

output += dig
print(output)
