def sumPoly (polinomial1, polinomial2):
    for i in range(len(polinomial1)):
        for j in polinomial2:
            if polinomial1[i][1] == j[1]:
                polinomial1[i] = ((polinomial1[i][0] + j[0], polinomial1[i][1]))
                polinomial2.remove(j)
    sum = polinomial1 + polinomial2
    for i in sum:
        if i[0] == 0:
            sum.remove(i)
    sum = sorted(sum, key=lambda num: num[1])
    sum.reverse()
    return sum

with open("C:/Users/ariel/OneDrive/Рабочий стол/homework_4_python/homework/task5/file_1.txt", "r") as f:
    M1 = []
    i = 0
    for line in f:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M1 = M1 + [lst]
print("M1 = ", M1)


with open("C:/Users/ariel/OneDrive/Рабочий стол/homework_4_python/homework/task5/file_2.txt", "r") as f2:
    M2 = []
    i = 0
    for line in f2:
        lines = line.split(' ')
        lst = []
        for ln in lines:
            ln = ln.rstrip()
            if ln != '':
                num = int(ln)
                lst = lst + [num]
        M2 = M2 + [lst]
print("M2 = ", M2)

res = open('C:/Users/ariel/OneDrive/Рабочий стол/homework_4_python/homework/task5/sumfile.txt', 'w')

result = sumPoly(M1, M2)

print(f'Сумма многочленов в виде списка кортежей: {result}')
res.write(str(result))

f.close()
f2.close()
res.close()