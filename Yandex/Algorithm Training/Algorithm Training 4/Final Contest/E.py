import math
from collections import defaultdict

# Функция определяет пересекаются ли треугольники
def isIntersectedTriangles(point1_A, point2_A, point3_A, point1_B, point2_B, point3_B):
    # Функция проверяет, лежит ли точка внутри треугольника
    def isPointInTriangle(point1_A, point2_A, point3_A, point):
        x1, x2, x3 = point1_A[0], point2_A[0], point3_A[0]
        x0 = point[0]

        y1, y2, y3 = point1_A[1], point2_A[1], point3_A[1]
        y0 = point[1]     

        a = (x1-x0)*(y2-y1)-(x2-x1)*(y1-y0)
        b = (x2-x0)*(y3-y2)-(x3-x2)*(y2-y0)
        c = (x3-x0)*(y1-y3)-(x1-x3)*(y3-y0)

        if ((a > 0 and b > 0 and c > 0) or (a < 0 and b < 0 and c < 0)):            
            return True
        else:            
            return False      
           
    # Функция определяет, пересекаются ли отрезки. Касание не учитывается
    def isIntersectedSegments(a, b, c, d):
        def area(a, b, c):
            return (b[0]-a[0])*(c[1]- a[1])-(b[1]-a[1])*(c[0]-a[0])
              
        return area(a,b,c)*area(a,b,d) < 0 and area(c,d,a)*area(c,d,b) < 0
    
    # Костыль
    t1 = [point1_A, point2_A, point3_A]
    t2 = [point1_B, point2_B, point3_B]
    t1.sort()
    t2.sort()
    if t1 == t2: return True

    # Проверки, лежат ли точки второго треугольника внутри первого
    for point in (point1_B, point2_B, point3_B):
        if isPointInTriangle(point1_A, point2_A, point3_A, point): return True

    # Проверки, лежат ли точки первого треугольника внутри второго
    for point in (point1_A, point2_A, point3_A):
        if isPointInTriangle(point1_B, point2_B, point3_B, point): return True

    # Заплатка вместо моей проверки по совету из чата
    (x1, y1), (x2, y2), (x3, y3) = point1_A, point2_A, point3_A
    p1, p2, p3 = ((x1 + x2)/2, (y1 + y2)/2), ((x2 + x3)/2, (y2 + y3)/2), ((x3 + x1)/2, (y3 + y1)/2)
    if any(isPointInTriangle(point1_B, point2_B, point3_B, p) for p in (p1, p2, p3)):
        return True
    (x1, y1), (x2, y2), (x3, y3) = point1_B, point2_B, point3_B
    p1, p2, p3 = ((x1 + x2) / 2, (y1 + y2) / 2), ((x2 + x3) / 2, (y2 + y3) / 2), ((x3 + x1) / 2, (y3 + y1) / 2)
    if any(isPointInTriangle(point1_A, point2_A, point3_A, p) for p in (p1, p2, p3)):
        return True       

    # Попарное проверка пересекаются ли стороны одного треугольника с другим
    for segment1 in ((point1_A, point2_A), (point2_A, point3_A), (point1_A, point3_A)):
        for segment2 in ((point1_B, point2_B), (point2_B, point3_B), (point1_B, point3_B)):
            if isIntersectedSegments(segment1[0], segment1[1], segment2[0], segment2[1]): return True

    return False

# Функция считает площадь треугольника по формуле Герона
# Удваиваю площать треугольники (фактически принимаю длину стороны минимальной клетки за 2), чтобы избавится перейти к целочисленным площадям
def getTriSquare(p1, p2, p3): 
    A = math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))
    B = math.sqrt((p1[0]-p3[0])*(p1[0]-p3[0])+(p1[1]-p3[1])*(p1[1]-p3[1]))
    C = math.sqrt((p2[0]-p3[0])*(p2[0]-p3[0])+(p2[1]-p3[1])*(p2[1]-p3[1]))

    P = (A+B+C)/2

    return round(2*math.sqrt(P*(P-A)*(P-B)*(P-C)))

# Проверка пересекается ли добавляемый треугольник с уже добавленными
def isIntersectsWithOriginals(intersectedTriangles, original_triangles, p1, p2, p3):
    for i in range(len(original_triangles)):
        x1, y1, x2, y2, x3, y3 = original_triangles[i]
        if intersectedTriangles[((x1, y1), (x2, y2), (x3, y3))][(p1, p2, p3)]: return True

    return False
    
# Основная функция поиска ответа, запускающая рекурсию
def countNewTriangles(original_triangles, possible_triangles, intersectedTriangles, N, M, remain_square):    
    def getMinNumberOfTriangles(N, M, original_triangles, possible_triangles, curr_index, remain_square, result):
        # Если незакрашенная площаль равно нулю, завершаем текущую рекурсию, при необходимости, обновляем результат
        if remain_square == 0:
            if len(original_triangles) < len(result): result[:] = original_triangles.copy()
            return
        elif remain_square > 0:
            # Если еще не вся площаль заполнена идем по массиву возможных для добавления треугольников. Если выходим за границу этого массива, завершаем рекурсию
            if curr_index == len(possible_triangles): return
            
            # Если уже найден лучший результат, завершаем ветвь рекурсии
            if ((len(result)-len(original_triangles))*possible_triangles[curr_index][3] <= remain_square): return
                                        
            p1, p2, p3 = possible_triangles[curr_index][0], possible_triangles[curr_index][1], possible_triangles[curr_index][2]
            # Если треугольник данного вида может быть добавлен, добавляем, запускаем новую ветвь рекурсии
            if not isIntersectsWithOriginals(intersectedTriangles, original_triangles, p1, p2, p3):
                original_triangles.append([*p1, *p2, *p3])
                getMinNumberOfTriangles(N, M, original_triangles, possible_triangles, curr_index, remain_square-possible_triangles[curr_index][3], result)
                original_triangles.pop()

                if ((len(result)-len(original_triangles))*possible_triangles[curr_index][3] <= remain_square): return

            # Запускаем ветвь, пропуская текущий возможный треугольник и переходя к следующему виду
            getMinNumberOfTriangles(N, M, original_triangles, possible_triangles, curr_index+1, remain_square, result)
      
    result = [0]*(N*M*2+1) # Ответ устанавливаем заведомо большего размера, чем может быть максимально треугольников на поле
    getMinNumberOfTriangles(N, M, original_triangles, possible_triangles, 0, remain_square, result)

    return result

# Сдвиг треугольника по оси X и/или Y
def shiftTriangle(p1, p2, p3, dx, dy):
    return (p1[0]+dx, p1[1]+dy), (p2[0]+dx, p2[1]+dy), (p3[0]+dx, p3[1]+dy)

fin = open('input.txt')
N, M, K = [int(x) for x in fin.readline().split()]

# Считывание уже добавленных треугольников (оставшихся учпочмаков). Подсчет оставшейся для заполнения площади в квадрате. Сторона минимального квадрата = 2
remain_square = N*M*2
original_triangles = [0]*K
for i in range(K):
    original_triangles[i] = [int(x) for x in fin.readline().split()]

    point1 = (original_triangles[i][0], original_triangles[i][1])
    point2 = (original_triangles[i][2], original_triangles[i][3])
    point3 = (original_triangles[i][4], original_triangles[i][5])

    remain_square -= getTriSquare(point1, point2, point3)

# Создание по одному каждого возможного треугольника без учета сдвига на поле - три следующих цикла
temp_triangles = [] # point1, point2, point3, width по оси X, heights по оси Y, square
# Прямоугольные треугольники
for i in range(1, min(N+1, M+1)):
    S = getTriSquare((0, 0), (i, 0), (0, i))    
    temp_triangles.append(((0, 0), (i, 0), (0, i), i, i, S))
    temp_triangles.append(((i, i), (i, 0), (0, i), i, i, S))
    temp_triangles.append(((0, 0), (0, i), (i, i), i, i, S))
    temp_triangles.append(((0, 0), (i, 0), (i, i), i, i, S))

for i in range(2, N+1, 2):
    S = getTriSquare((0, 0), (i, 0), (i//2, i//2))
    temp_triangles.append(((0, 0), (i, 0), (i//2, i//2), i, i//2, S))
    temp_triangles.append(((i//2, 0), (0, i//2), (i, i//2), i, i//2, S))

for i in range(2, M+1, 2):
    S = getTriSquare((0, 0), (0, i), (i//2, i//2))
    temp_triangles.append(((0, 0), (0, i), (i//2, i//2), i//2, i, S))
    temp_triangles.append(((0, i//2), (i//2, 0), (i//2, i), i//2, i, S))

# # Непрямоугольные треугольники (в большинстве случаев :D)
# for i in range(2, N+1, 2):
#     for j in range(M, 0, -1):
#         S = getTriSquare((0, 0), (i, 0), (i//2, j))
#         temp_triangles.append(((0, 0), (i, 0), (i//2, j), i, j, S))
#         temp_triangles.append(((i//2, 0), (0, j), (i, j), i, j, S))

# for i in range(2, M+1, 2):
#     for j in range(N, 0, -1):
#         S = getTriSquare((0, 0), (0, i), (j, i//2))
#         temp_triangles.append(((0, 0), (0, i), (j, i//2), j, i, S))
#         temp_triangles.append(((0, i//2), (j, 0), (j, i), j, i, S))

# Сортировка треугольников по убыванию площади
temp_triangles.sort(key=lambda x: -x[5])

# Получение всех возможных треугольников на поле путем сдвига треугольника каждого вида
possible_triangles = []
for curr_index in range(len(temp_triangles)):    
    delta_x = temp_triangles[curr_index][3] # Ширина треугольника
    delta_y = temp_triangles[curr_index][4] # Высота треугольника
    tri_square = temp_triangles[curr_index][5]

    for i in range(N-delta_x+1):
        for j in range(M-delta_y+1):                        
            p1, p2, p3 = shiftTriangle(temp_triangles[curr_index][0], temp_triangles[curr_index][1], temp_triangles[curr_index][2], i, j)
            possible_triangles.append((p1, p2, p3, tri_square))

# Подсчет заранее попарно за N^2 пересекаются ли треугольники, а также...
# Проверка пересекаются ли возможные треугольники с уже добавленными (исходными) и формирование массива возможных треугольников с учетом этого
intersectedTriangles, temp = defaultdict(dict), []
for *triangle1, S in possible_triangles:
    for *triangle2, _ in possible_triangles:
        intersectedTriangles[tuple(triangle1)][tuple(triangle2)] = intersectedTriangles[tuple(triangle2)][tuple(triangle1)] = isIntersectedTriangles(*triangle1, *triangle2)
    
    trigger = False
    for triangle2 in original_triangles:
        point1 = (triangle2[0], triangle2[1])
        point2 = (triangle2[2], triangle2[3])
        point3 = (triangle2[4], triangle2[5])

        res = isIntersectedTriangles(*triangle1, point1, point2, point3)
        if res: trigger = True
        intersectedTriangles[tuple(triangle1)][(point1, point2, point3)] = intersectedTriangles[(point1, point2, point3)][tuple(triangle1)] = res

    if not trigger: temp.append((*triangle1, S))        

original_number = len(original_triangles)
res = countNewTriangles(original_triangles, temp, intersectedTriangles, N, M, remain_square)

print(len(res)-original_number)
for ans in res[original_number:]:
    print(*ans)