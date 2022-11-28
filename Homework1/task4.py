# 4-Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти 
# (x и y).
# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

quarter=int(input('введите номер четверти: \n'))
if quarter==1:
    print('quarter = 1 = x∈(0, ∞) u y∈(0,∞)')
if quarter==2:
    print('quarter = 2 = x∈(0, ∞) u y∈(-∞,0)')    
if quarter==3:
    print('quarter = 3 = x∈(-∞,0) u y∈(-∞,0)')
if quarter==4:
    print('quarter = 4 = x∈(-∞,0) u y∈(0,∞)')
