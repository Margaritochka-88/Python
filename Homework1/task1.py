# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
# *Пример:*

# - 6 -> да
# - 7 -> да
#  - 1 -> нет

n = int(input('Введите цифру обозначающую день недели:\n'))
if n==6 or n==7:
    print('->Yes')
if n<=5:
    print('-> No')
elif n>7:
    print('Такого дня недели не существует')
 