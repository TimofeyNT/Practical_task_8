# Задача 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать
# построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = file.read().splitlines()
#         for e in range(len(text) - lines, len(text)):
#             print(text[e])
#
# flag = True
# while flag == True:
#     lines = int(input('Введите число: '))
#     if lines >= 0:
#          flag = False
#     else:
#         print('Некоректный ввод! Повторите.')
#
# file = input('Введите имя файла: ')   # article.txt
# read_last(lines, file)

# Задача 2.
# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину
# (или список слов, если таковых несколько).
#
# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as file:
#         text = set(file.read().split())
#         text = list(sorted(text, key=len, reverse=True))
#         print(text[0])
#         for i in range(1, len(text)):
#             if len(text[0]) == len(text[i]):
#                 print(text[i])
#             else:
#                 break
# file = input('Введите имя файла: ')   # article.txt
# longest_words(file)