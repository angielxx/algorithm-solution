
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