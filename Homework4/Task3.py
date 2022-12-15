# В файле, содержащем фамилии студентов и их оценки, изменить на прописные 
# буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл. 
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4


from typing import Optional
from typing import List

def get_list_data(filename: str) -> List[str]:
    '''
    Возвращает список из строк файла
    Args:
    filename - имя файла
    Returns:
    List[str]
    '''
    with open(filename, encoding='utf-8') as file:
        return file.read().split('\n')




def elements_to_caps(lst: list, trigger_str: str) -> List[str]:
     '''
     Changes the case of an item on condition
     Args: 
     lst - list name
     trigger_str - condition    
     Returns: list
     '''
     for i in range(len(lst)):
         if trigger_str in lst[i]:
             lst[i] = lst[i].upper()
     return lst



    
lst = get_list_data('/Users/margaritakrylova/Desktop/Python/HelloPython/Homework4/Students.txt')

print(elements_to_caps(lst, '5'))

with open('/Users/margaritakrylova/Desktop/Python/HelloPython/Homework4/Students.txt', 'w', encoding='utf-8') as data:
     for i in range(len(lst)):
         data.writelines(f'{lst[i]}\n')