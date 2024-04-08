fin = open('input.txt')
N, M = [int(x) for x in fin.readline().split()]
students = [(int(num), i) for i, num in enumerate(fin.readline().split())]
students.sort()
classes = [(int(num), i) for i, num in enumerate(fin.readline().split())]
classes.sort()

students_in_class, success = [0]*N, 0

index1, index2 = 0, 0
while index1 < len(students) and index2 < len(classes):
    while index2 < len(classes) and students[index1][0] >= classes[index2][0]:
        index2 += 1

    if index2 < len(classes) and students[index1][0] < classes[index2][0]:
        students_in_class[students[index1][1]] = classes[index2][1]+1
        success += 1
        index2 += 1
    index1 += 1

print(success)
print(*students_in_class)