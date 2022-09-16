# BOJ 1991 트리순회
# 220915

import sys
input = sys.stdin.readline

N = int(input())

ch1 = {}
ch2 = {}

for _ in range(N):
    p, c1, c2 = input().split()
    if c1 != '.':
        ch1[p] = c1
    if c2 != '.':
        ch2[p] = c2

def preorder(n):
    print(n, end='')
    if n in ch1.keys():
        preorder(ch1[n])
    if n in ch2.keys():
        preorder(ch2[n])

def inorder(n):
    if n in ch1.keys():
        inorder(ch1[n])
    print(n, end='')
    if n in ch2.keys():
        inorder(ch2[n])

def postorder(n):
    if n in ch1.keys():
        postorder(ch1[n])
    if n in ch2.keys():
        postorder(ch2[n])
    print(n, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')