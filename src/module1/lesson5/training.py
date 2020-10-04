first_line = input('Ученики')
PASS_GRADE = int(input('Проходной балл'))
first_line = first_line.split(',')
first_line = [elem.split() for elem in first_line]
s = set()
# print(first_line)
for elem in first_line:
    if int(elem[-1]) >= PASS_GRADE:
        s.add(elem[0])
if len(s) != 0:
    print(' '.join(sorted(list(s))))
else:
    print(0)

