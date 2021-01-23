import random

# [1, 2, 3, 4, 0, 6, 7, 0, 0, 9]
# [1, 2, 3, 4, 6, 7, 9, 0, 0, 0]


input_list = [random.randint(0, 7) for _ in range(10)]
print(input_list)

j = 0
for i in range(len(input_list)):
    if input_list[i] != 0:
        input_list[j] = input_list[i]
        j += 1
print(j)
for i in range(j, len(input_list)):
    input_list[i] = 0

print(input_list)
