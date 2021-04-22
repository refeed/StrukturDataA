number_list = list(map(int, input().split()))

result = 1

for number in number_list:
    result *= number

print(result)
