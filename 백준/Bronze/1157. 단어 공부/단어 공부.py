# BOJ 1157 단어공부
# 221001

import collections
import sys
input = sys.stdin.readline

word = input().strip()
word = word.lower()

counter = collections.Counter(word)

max_num = counter.most_common(1)

if len(word) == 1:
    print(word.upper())
else:
    if list(counter.values()).count(max_num[0][1]) > 1:
        print('?')
    elif list(counter.values()).count(max_num[0][1]) == 1:
        print(counter.most_common(1)[0][0].upper())