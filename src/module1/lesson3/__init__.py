# count1 = 0
# while count1 <= 10:
#     print(count1)
#     count1 += 1

# for i in range(0, 11):  # [0; 10) -- [0, 9]
#     print(i)

# n = int(input())
# count = 0
# s = 0
# while count <= n:
#     s = s + count
#     count = count + 1
# print(s)

# n = int(input())
# s = 0
# for i in range(n + 1):
#     if i == 3:
#         continue
#     s += i
# print(s)

s = 'Hello'
count = 0

while count < len(s):
    print(s[count])
    count += 1

print("---------------")

for c in s:
    print(c)

print("---------------")

for i in range(0, len(s), 2):
    print(s[i])

