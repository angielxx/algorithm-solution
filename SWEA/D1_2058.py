num = input()
list_str = list(num)
list_int = list(map(int, list_str))
result = sum(list_int)

print(result)