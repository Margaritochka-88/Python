# 1 - Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]




# def nums(n):
#     ans = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         ans.append(n)
#     return ans


# print(nums(int(input( 'Введите число для разложения на простые множители: \n'))))

from typing import Optional 

def give_int(input_string: str, min_num: Optional[int] = None, max_num: Optional[int] = None) -> int:
     '''
     Takes an int number from user
     Takes: string
     Returns: int number or a message about an error
     '''
     while True:
         try:
             num = int(input(input_string))
             if min_num and num < min_num:
                 print(f'Введите больше{min_num}')
                 continue
             if max_num and num > max_num:
                 print(f'Введите больше{max_num}')
                 continue
             return num
         except ValueError:
             print('Вы ввели не число')


def is_prime(n: int) -> bool: # функция проверяющая простое ли число
     '''
     Checks if the given number is prime
     Takes: int number
     Returns: True/False
     '''
     for i in range(2, n):
         if not (n % i):
             return False
     return True


n = abs(give_int('Введите число:\n'))
lst_of_prime_numbers = [i for i in range(2, n+1) if not n % i and is_prime(i)] # составляется список чисел от 2 до n и проверяем является ли оно простым и делится ли на это число
print(lst_of_prime_numbers)