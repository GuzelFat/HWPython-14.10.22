# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
size=int( input('Введите количество элементов списка: '))
list=[round(random.uniform(1,10),2) for x in range(size)]
print(list)

list1=[round((i%1),2) for i in list]
min=1
max=0
for i in list1:
    if i<min and i!=0: min=i
    if i>max:max = i
print (round((max-min),2))    
