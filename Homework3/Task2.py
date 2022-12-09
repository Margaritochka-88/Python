# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]



def pari(list):
     list1 = []
     count = -1
     i = 0
     len1 = len(list) / 2
     while i < len1:
         list1.append(list[i]*list[count])
         count -= 1
         i += 1
     return list1

list = [2, 3, 4, 5, 6, 7, 8]
list1 = pari(list)
print(list)
print(list1)


