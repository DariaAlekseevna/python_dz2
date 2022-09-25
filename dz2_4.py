#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных пользователем через пробел позициях.

from random import random
from random import randint

N = int(input('введите число: '))
N_list = []
for i in range(N):
    N_list.append(randint(-N, N))
print(N_list)

num = int(input('введите количество позиций: '))
num_list = []
sum = 1
for j in range(num):
    num_list.append(int(input("введите позицию элемента в строке: ")))
    sum = sum * N_list[num_list[j]]
print(f'произведение элементов на указанных пользователем позициях: {sum}')

