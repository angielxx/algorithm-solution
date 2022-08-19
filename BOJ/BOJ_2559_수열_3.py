# BOJ 2559 수열
# 220819
# 투포인터, 슬라이딩 윈도우

N, K = map(int, input().split())
li = list(map(int, input().split()))

temp_sum = sum(li[:K])
sum_list = []
sum_list.append(temp_sum)

for i in range(N-K):
    j = i+K
    temp_sum = temp_sum - li[i] + li[j]
    sum_list.append(temp_sum)

print(max(sum_list))

# 연산수를 줄였더니 맞게 나옴
# 틀렸을때 : 투포인터 쓰고 while문으로 하나씩 올려감
# 투포인터가 필요가 없음 -> 계산해야되는 범위의 크기가 일정하기 때문
