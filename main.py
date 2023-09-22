#1 Вводим одномерный массив числовых значений
numbers = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in numbers]

# Инициализируем переменные для подсчета
count_divisible_by_3 = 0
sum_even_numbers = 0

# Подсчитываем количество чисел, делящихся на 3 нацело, и суммируем четные числа
for number in numbers:
    if number % 3 == 0:
        count_divisible_by_3 += 1
    if number % 2 == 0:
        sum_even_numbers += number

# Вычисляем среднее арифметическое четных чисел (если они есть)
average_even = sum_even_numbers / len(numbers)

# Расширяем кортеж на 2 элемента и ставим полученные значения на первое и последнее места
numbers = (count_divisible_by_3, average_even, *numbers, average_even, count_divisible_by_3)

# Выводим результат
print("Массив с добавленными значениями на первое и последнее место:", numbers)

# 2....................................................................................................................


# Введите нечетное число n
n = int(input("Введите нечетное число n: "))

# Создайте двумерный массив из n×n элементов, заполнив его символами "."
array = [["." for _ in range(n)] for _ in range(n)]

# Заполните символами "*" среднюю строку массива
mid_row = n // 2
array[mid_row] = ["*" for _ in range(n)]

# Заполните символами "*" средний столбец массива
mid_col = n // 2
for row in array:
    row[mid_col] = "*"

# Заполните символами "*" главную диагональ
for i in range(n):
    array[i][i] = "*"

# Заполните символами "*" побочную диагональ
for i in range(n):
    array[i][n - i - 1] = "*"

# Выведите полученный массив на экран, разделяя элементы массива пробелами
for row in array:
    print(" ".join(row))



#3 ................................................................................
# Введите список чисел
numbers = [int(x) for x in input("Введите список чисел через пробел: ").split()]

# Инициализируйте счетчик элементов, которые больше двух своих соседей
count = 0

# Перебирайте элементы списка, начиная со второго и заканчивая предпоследним
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        count += 1

# Выведите количество элементов, которые больше двух своих соседей
print(f"Количество элементов, которые больше двух своих соседей: {count}")




# 4............................................................................
# Создаем множества для каждой книги и учеников, прочитавших все три книги
book_A = set(range(1, 26))
book_B = set(range(1, 23))
book_C = set(range(1, 23))
all_three_books = set(range(1, 11))

# Находим учеников, прочитавших по одной книге
only_A = book_A - (book_B | book_C)
only_B = book_B - (book_A | book_C)
only_C = book_C - (book_A | book_B)

# Находим учеников, прочитавших ровно 2 книги
two_books = (book_A & book_B) | (book_A & book_C) | (book_B & book_C)

# Находим учеников, не прочитавших ни одной книги
no_books = set(range(1, 41)) - (book_A | book_B | book_C)

# Выводим результаты
print("Учеников, прочитавших по одной книге:", len(only_A) + len(only_B) + len(only_C))
print("Учеников, прочитавших ровно 2 книги:", len(two_books))
print("Учеников, не прочитавших ни одной книги:", len(no_books))
#5...........................................................................
# Создаем пустые словари для хранения информации о странах и городах
country_to_cities = {}
city_to_countries = {}

# Вводим количество строк со странами и городами
num_lines = int(input("Введите количество строк со странами и городами: "))

# Считываем информацию о странах и городах
for _ in range(num_lines):
    line = input().split()
    country = line[0]
    cities = line[1:]

    # Добавляем страну и города в соответствующие множества
    country_to_cities[country] = set(cities)
    for city in cities:
        if city in city_to_countries:
            city_to_countries[city].add(country)
        else:
            city_to_countries[city] = {country}

# Вводим количество строк с городами
num_queries = int(input("Введите количество строк с городами: "))

# Считываем запросы и выводим список стран для каждого города
for _ in range(num_queries):
    city = input()
    if city in city_to_countries:
        countries = sorted(list(city_to_countries[city]))
        print("Город {} находится в странах: {}".format(city, ", ".join(countries)))
    else:
        print("Город {} не найден.".format(city))
