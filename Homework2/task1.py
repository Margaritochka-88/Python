# 1 - Напишите программу, которая принимает на вход вещественное
# число и  показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример 67.82->23


def get_int(float_): # функция преобразования вещественного числа в интовое
     while round(float_, 9) % 10 != 0:
         float_ = round(float_, 9) * 10 #число умножаем на 10 пока оно не станет интовым
     new_int = int(float_)
     return new_int // 10

def sum_of_digits(number): #функция суммы знаков
     sum = 0
     while number > 0: #пока число не равно нулю мы в сумму добавляем остаток от деления числа на 10
         sum = sum + (number % 10)
         number = number//10 # делим на 10 чтобы число возвращалось с каждым циклом
     return sum


try:
     n = float(input('введите вещественное число:\n'))
     num = abs(n) # модуль чтобы исключить минус
     print(f'сумма цифр в числе: {sum_of_digits(get_int(num))}')
except ValueError:
     print('вы ввели не число')
     
# второй вариант     
# num = input('введите число:\n')
# list_num = list(num)
# print(list_num)
# semple_list=[]
# for i in range(0, len(list_num)):
#     if list_num[i].isdigit():
#         semple_list.append(int(list_num[i]))
# print(semple_list)
# sum_numbers=sum(semple_list)
# print(num, ' ->', sum_numbers)        

# третий вариант
# number= input('Ведите число: ')
# num_1= number.replace('.',"").replace('-','')

# result=round(sum(int(i) for i in num_1))

# print(result)