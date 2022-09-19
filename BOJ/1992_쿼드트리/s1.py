# BOJ 1992 쿼드트리
# 220919

import sys
input = sys.stdin.readline

# 입력값 받기
N = int(input())
arr = [ input() for _ in range(N)]

# 한 영역을 기준으로 모든 원소의 값이 같은지 확인
def quadTree(i_start=0, i_end=N-1, j_start=0, j_end=N-1):
    # 영역 왼쪽 위의 첫번째 원소의 값을 기준으로 비교
    num = arr[i_start][j_start]
    # flag
    status = True
    # 전체 영역을 순회하면서 비교
    for i in range(i_start, i_end+1):
        # flag가 True일 때만 계속 진행
        if not status:
            break
        for j in range(j_start, j_end+1):
            # 하나라도 숫자가 다르면 flag 세우고 중단
            if arr[i][j] != num:
                status = False
                break
    # flag가 True면 모든 숫자가 같다는 뜻으로
    # 해당 숫자를 반환
    if status:
        return num
    # flag가 False면 숫자가 다르다는 뜻으로
    # 영역을 4분할하여 재귀 호출
    else:
        i_mid = (i_start + i_end) // 2
        j_mid = (j_start + j_end) // 2
        return '({}{}{}{})' .format(quadTree(i_start, i_mid, j_start, j_mid), quadTree(i_start, i_mid, j_mid+1, j_end), quadTree(i_mid+1, i_end, j_start, j_mid), quadTree(i_mid+1, i_end, j_mid+1, j_end))

print(quadTree())