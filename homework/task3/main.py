def uniq_elements_list(numbers):
    if numbers.replace(" ", "").isdigit():
        result = set(numbers.split())
        print(f'Список неповторяющихся элементов исходной последовательности -> [{result}]')
    else:
        print("Введены неверные данные")

def input_numbers():
    nums = input('Введите числа через пробел, чтобы создать список: ')
    uniq_elements_list(nums)

input_numbers()