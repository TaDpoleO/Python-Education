fin = open('input.txt')
a = int(fin.readline())
b = int(fin.readline())
n = int(fin.readline())

max_students_in_group1 = a
min_students_in_group2 = b//n + (0 if b%n == 0 else 1)

print('YES') if max_students_in_group1 > min_students_in_group2 else print('NO')