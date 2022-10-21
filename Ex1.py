# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

#  Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, 
# ответ: 12

# 
import random

list_len=int( input('Введите количество элементов списка:'))
num_list=[]
for i in range(list_len):
    num_list.append(random.randint(0,40))
print(num_list)    

sum=0
for i in range(list_len):
    if i % 2 == 1:
        sum += num_list[i]
print(sum)        
