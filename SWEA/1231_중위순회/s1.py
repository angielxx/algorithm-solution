# SWEA 1231 중위순회
# 220913

T = 10
for tc in range(1, T+1):
    # 정점의 총 수
    N = int(input())
    # 부모 번호를 인덱스로 자식 번호를 저장
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    # 각 노드 번호를 인덱스로 알파벳 저장
    letters = [0] * (N + 1)
    # 루트 정점의 번호는 항상 1
    root = 1

    for _ in range(N):
        arr = list(input().split())
        # 입력값 한 줄 당 '노드번호 알파벳' 2개는 무조건 있음
        for i in range(2):
            if i == 0:
                node = int(arr.pop(0))
            if i == 1:
                letter = arr.pop(0)
        letters[node] = letter
        # arr가 남아있다면 자식노드가 있는 것
        if arr:
            while arr:
                c = int(arr.pop(0))
                if ch1[node] == 0:
                    ch1[node] = c
                else:
                    ch2[node] = c
    
    def inorder(root):
        if root:
            inorder(ch1[root])
            print(letters[root], end='')
            inorder(ch2[root])

    print('#{}'.format(tc), end=' ')
    inorder(root)
    print()