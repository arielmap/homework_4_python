def list_n(n):
    if n > 0:
        result = ""
        for i in range(1, n+1):
            if n % i == 0:
                result += str(i) + " "
        print(f'Список простых множителей числа {n} -> [{result}]')
    else:
        print("Задайте натуральное число")


def input_N():
    num = int(input('Введите натуральное число N: '))
    list_n(num)


input_N()
