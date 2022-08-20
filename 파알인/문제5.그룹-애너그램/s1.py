# 49. Group Anagrams
# 220819

strs = ["eat","tea","tan","ate","nat","bat"]

spell = dict()

for str in strs:
    temp = []
    for s in str:
        temp.append(s)
    temp.sort()
    key = ''.join(temp)
    if key in spell.keys():
        spell[key].append(str)
    else:
        spell[key] = [str]

result = []
for key,val in spell.items():
    result.append(val)

print(result)