'''
Задание 2.1
Напишите программу, которая проверяет здоровье персонажа в игре. 
Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
'''
# num_health = int(input())
# if num_health <= 0:
#     print(False)
# else:
#     print(True)

"""
Задание 2.2
Напишите программу, которая проверяет является ли введенное число четным. 
Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
"""
# number = int(input())
# if number % 2 != 1:
#     print("Четное")
# else:
#     print("Нечетное")

"""
Задание 2.3
Напишите программу, которая проверяет является ли год високосным. 
Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) 
и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, 
он также считается високосным (1200, 2000)
"""
# year = int(input())
# if year % 4 == 0:
#     print("Високосный год")
# elif year % 400 == 0 and not year % 100 == 0:
#     print("Високосный год")
# else:
#     print("Не високосный год")

"""
Задание 2.4
Напишите программу, которая печатает введенный текст заданное количество раз, построчно. 
Текст и количество повторений нужно ввести с помощью input()
"""
# ver.1
# text = input()
# repeat_num = int(input())
# result = ''
# while repeat_num > 0:
#     result = result + '\n' + text
#     repeat_num -= 1
# print(result)

# ver.2
# text = input()
# repeat_num = int(input())
# for i in range (repeat_num):
#     print(text)
"""
Задание 2.5.
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), 
производит заданное арифметическое действие и печатает результат в формате: 
{num1} {operator) {num2) = {result}
"""
# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# operator = str(input("Введите оператор из представленных -- \'+\', \'-\', \'/\', \'*\', \'%\', \'//\' : "))
# if operator == '+':
#     result = num_1 + num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# elif operator == '-':
#     result = num_1 - num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# elif operator == '/':
#     result = num_1 / num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# elif operator == '*':
#     result = num_1 * num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# elif operator == '%':
#     result = num_1 % num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# elif operator == '//':
#     result = num_1 // num_2
#     print(f'{num_1} {operator} {num_2} = {result}')
# else:
#     print('Оператор не найден')