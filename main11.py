# n = 20
# A = []
#
# for i in range(n):
#     A.append(int(input("Введите оценку: ")))
#
# negative_count = 0
# for num in A:
#     if num < 0:
#         negative_count += 1
#
# print("Список оценок:", A)
# print("Количество отрицательных оценок:", negative_count)
#


# # Создание списка из 20 элементов
# B = []
# for i in range(20):
#     num = float(input("Введите элемент списка B: "))
#     B.append(num)
#
# # Вычисление суммы положительных элементов списка B
# sum_positive = 0
# for num in B:
#     if num > 0:
#         sum_positive += num
#
# print("Сумма положительных элементов списка B:", sum_positive)



# # Ввод количества оценок
# num_grades = int(input("Введите количество оценок: "))
#
# # Ввод оценок в список
# grades = []
# for i in range(num_grades):
#     grade = int(input("Введите оценку №{}: ".format(i+1)))
#     grades.append(grade)
#
# # Вывод оценок
# print("Введенные оценки:", grades)
#
# # Средняя оценка
# average_grade = sum(grades) / num_grades
# print("Средняя оценка за урок:", average_grade)




# B = []
# for i in range(20):
#     element = int(input("Введите элемент №{} списка B: ".format(i+1)))
#     B.append(element)
#
# # Сумма положительных элементов списка
# positive_sum = 0
# for element in B:
#     if element > 0:
#         positive_sum += element
#
# # Вывод суммы положительных элементов
# print("Сумма положительных элементов списка B:", positive_sum)



# # Создаем список из 10 целых чисел
# numbers = []
# for i in range(10):
#     number = int(input("Введите целое число №{}: ".format(i+1)))
#     numbers.append(number)
#
# # Находим наименьший элемент
# min_value = min(numbers)
# min_index = numbers.index(min_value)
#
# # Меняем наименьший элемент местами с последним элементом
# last_index = len(numbers) - 1
# numbers[min_index], numbers[last_index] = numbers[last_index], numbers[min_index]
#
# # Выводим измененный список
# print("Измененный список:", numbers)



#7
# X = []
# for i in range(14):
#     x = float(input("Введите элемент списка X: "))
#     if 0 < x < 1:
#         print("Номера элементов, удовлетворяющих условию 0 < X(i) < 1:", X)




#10
# a = []
# for i in range(25):
#     mark = int(input("Введите оценку на первом экзамене: "))
#     a.append(mark)
# not_allowed = 0
# for mark in a:
#     if mark == 2:
#         not_allowed += 1
# print("Количество людей не допущенных ко второму экзамену:", not_allowed)



# import random
# numbers = [random.randint(1, 100) for _ in range(20)]
# print("Исходный список:")
# print(numbers)
# max_num = max(numbers)
# max_index = numbers.index(max_num)
# numbers[0], numbers[max_index] = numbers[max_index], numbers[0]
# print("Список после замены наибольшего элемента с первым:")
# print(numbers)



# numbers = []
# for i in range(10):
#     number = int(input("Введите число: "))
#     numbers.append(number)
# min_number = min(numbers)
# min_index = numbers.index(min_number)
# numbers[min_index], numbers[-1] = numbers[-1], numbers[min_index]
# print("Список с наименьшим элементом, поменявшимся местами с последним:")
# print(numbers)




# numbers = []
# for i in range(12):
#     num = float(input("Введите число: "))
#     numbers.append(num)
#
# min_index = numbers.index(min(numbers))
# numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
#
# print("numbers[0]:", numbers[0])
# print("min element swapped with first element:", numbers)




# numbers = []
# for i in range(10):
#     number = float(input("Введите вещественное число: "))
#     numbers.append(number)
# numbers.sort(reverse=True)
# print("Отсортированный список по убыванию:")
# print(numbers)




# numbers = []
# for i in range(15):
#     num = int(input("Введите целое число: "))
#     numbers.append(num)
#     numbers.sort()
#
# print("Отсортированный список по возрастанию:", numbers)



# lst = []
# for i in range(10):
#     num = int(input("Введите целое число: "))
#     lst.append(num)
#
# positive_nums = [x for x in lst if x > 0]
# negative_nums = [x for x in lst if x < 0]
#
# lst.clear()
# lst.extend(positive_nums)
# lst.extend(negative_nums)
#
# print("Список положительных и отрицательных чисел:", lst)



# # ввод списка вещественных чисел
# numbers = []
# for i in range(12):
#     num = float(input("Введите {} число: ".format(i + 1)))
#     numbers.append(num)
# # создание нового списка для отрицательных чисел
# negative_numbers = [num for num in numbers if num < 0]
# # создание нового списка для положительных чисел
# positive_numbers = [num for num in numbers if num >= 0]
# # объединение списков отрицательных и положительных чисел
# result = negative_numbers + positive_numbers
# # вывод результата
# print("Список с отрицательными числами и затем с положительными числами:", result)



# lst = []
#
# for i in range(14):
#     num = int(input("Введите число: "))
#     lst.append(num)
# lst.reverse()
# print("Переставленные элементы списка в обратном порядке:")
# print(lst)



a = []
for i in range(12):
    a.append(int(input(f'Введите значение для a{i+1}: ')))
zeros = []
ones = []
for num in a:
    if num == 0:
        zeros.append(num)
    else:
        ones.append(num)

a = zeros + ones

print('Последовательность с нулями в начале и единицами в конце:')
print(a)



