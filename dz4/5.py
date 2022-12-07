# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('dz5_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('dz5_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('dz5_1.txt','r') as file:
    dz5_1 = file.readline()
    list_of_dz5_1 = dz5_1.split()


with open('dz5_2.txt','r') as file:
    dz5_2 = file.readline()
    list_of_dz5_2 = dz5_2.split()

print(f'{list_of_dz5_1} + {list_of_dz5_2}')
dz5 = list_of_dz5_1 + list_of_dz5_2

with open('dz5.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_dz5_1} + {list_of_dz5_2}')