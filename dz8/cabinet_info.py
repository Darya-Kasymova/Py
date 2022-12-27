import pandas as pd

print('----'*30)
print('Данные о классах')

class_card = {
        'Предмет': ['Литература','Математика','Русский язык','Информатика','История'],
        'Номер парты' : ['1','2','3','4','5'],
        'Ряд': ['Первый ряд','Второй ряд','Третий ряд','Четвертый ряд','Пятый ряд'],
        'Вид парты' : ['Двуместная','Одноместная','Одноместная ','Двуместная ','Двуместная'],
        'ID' : ['01','02','03','04','05']
}

cc = pd.DataFrame(data = class_card)

with open('cabinet.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{cc}')
        cl.write('\n')

print(cc)