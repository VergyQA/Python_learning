'''
3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
'''
# version num.1
# my_list = ['a', 'b', [1, 2, 3], 'd']
# item_1, item_2, item_3, item_4 = my_list
# print(item_3[0], item_3[1], item_3[2], sep = ', ')

# version num.2
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(f'{my_list[2][0]}, {my_list[2][1]}, {my_list[2][2]}')

'''
3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел (done),
   - распечатайте все строки, где есть буква 'a'
'''
# version num.1
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# i = 0
# sum_num = 0
# result = ''
# for i in range(len(list_1)):
#     if type(list_1[i]) == int:
#          sum_num = sum_num + list_1[i]
#     elif type(list_1[i]) == str and list_1[i].find('a') >= 0:
#          result = result + list_1[i] + ' '
#     else:
#          continue
# print(sum_num)
# print(result)

# version num.2
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# result_sum = 0
# result_a_char = []
# for i in range(len(list_1)):
#     if isinstance(list_1[i], int) == True:
#         result_sum = result_sum + list_1[i]
#     elif isinstance(list_1[i], str) == True and list_1[i].find('a') >= 0:
#         result_a_char.append(list_1[i])
#     else:
#         continue
# print(result_sum, result_a_char, sep = '\n')

'''
3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
'''

# lst = ['cat', 'dog', 'horse', 'cow']
# tpl = tuple(lst)
# print(tpl)

'''
3.4. Напишите программу, которая определяет, какая семья больше. 
      1) Программа имеет два input() - например, family_1, family_2. 
      2) Членов семьи нужно перечислить через запятую. 
     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
'''

'''
3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. 
В значения можете передать информацию
    о вашем любимом фильме. 
    - распечатайте только ключи
    - распечатайте только значения
    - распечатайте пары ключ - значение
'''

'''
3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
'''

'''
3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] 
'''

'''
3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
     - найдите значения, которые встречаются в обоих множествах
     - найдите значения, которые не встречаются в обоих множествах
     - проверьте являются ли эти множества подмножествами друг друга 
'''
