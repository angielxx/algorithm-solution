# 819. Most Common Word
# 220819

# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
#
# paragraph = "a."
# banned = []

words = []
for word in list(paragraph.split()):
    for w in list(word.split(',')):
        temp = ''
        for s in w:
            if s.isalpha():
                temp += s
        if temp:
            words.append(temp.lower())

words_dict = dict()
N = len(words)
for i in range(N):
    if words[i] not in banned:
        if words[i] not in words_dict.keys():
            words_dict[words[i]] = 1
        else:
            words_dict[words[i]] += 1

mx = 0
mx_w = ''
for key, val in words_dict.items():
    if val >= mx:
        mx = val
        mx_w = key
print(mx_w)