import random
numbers=int(input('Введи число N длинну списка который надо перемешать: '))
initial_list=[random.randint(0,100) for i in range(numbers)]# не буду изменять традициям
# for number in range(numbers):
#     number=random.randint(0,100)
#     initial_list.append(number)
print (initial_list)
for i in range(len(initial_list)-1, 0, -1):
    j = random.randint(0, i + 1)
    initial_list[i], initial_list[j] = initial_list[j], initial_list[i]
print (initial_list)