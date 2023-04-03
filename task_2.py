 
pets = dict()

t = 'Вид'
a = 'Возраст'
o = 'Владелиц'

def create():
    num = lest
    name = input('Введите имя питомца: ')
    typ = input('Введите вид питомца: ')
    age = (input('Введите возраст: '))
    owner = input('Введите имя владельца: ')
    pets.update({num:{name:{t:typ, a:age, o:owner}}})
    print(f'{name} => ID-{num}')

def update(num):
    what = input(f'Что Вы хотите изменить?\n{a} => Возраст\n{o} => Владельца\n')
    l = list(pets[num])
    l = ' '.join(l)
    if (what == 'Возраст') or (what == 'возраст'):
        age = (input('Введите новый возраст: '))
        pets[num][l]['Возраст'] = age
    elif (what == 'Владелиц') or (what == 'владелиц'):
        owner = input('Введите нового владельца: ')
        pets[num][l]['Владелиц'] = owner
    print(f'данные о питомцы по кличке {l} обновлены')

def delete(num):
    del pets[num]

def read(num):    
    i = pets[num] 
    i = ''.join(i)
    print(i)
    t = pets[num][i]['Вид']
    t = ''.join(t)
    print(t)
    a = pets[num][i]['Возраст']
    a = ''.join(a)
    print(a)
    o = pets[num][i]['Владелиц']
    o = ''.join(o)
    print(o)
    print (f'Это {t} по кличке {i}. Возраст питомца: {a}. Имя владельца: {o}')
    return 

def _list():
    L = len(list(pets))
    print(f'Всего {L} питомцем')    
    for i in range(1,L+1):
        x = list(pets[i])
        x = ''.join(x)
        print(f'{x} => ID - {i}')
    
def _data():
    L = len(list(pets))
    print(f'Всего {L} записи')    
    for i in range(1,L+1):
        x = list(pets[i]) 
        x = ''.join(x)#имя
        t = pets[i][x]['Вид']
        t = ''.join(t)
        a = pets[i][x]['Возраст']
        a = ''.join(a)
        o = pets[i][x]['Владелиц']
        o = ''.join(o)
        print(f'{x} => ID - {i}')
        print (f'Это {t} по кличке {x}. Возраст питомца: {a}. Имя владельца: {o}')

def info():
    print('\n[stop]: Для завершения программы\n[create]: Запись новых питомцев\n[read]: Пoлучение информации о питомцах по ID\n[update]: Обновление информации записанных питомцев\n[delete]: Удаление информации о питомце\n[list]: Список всех записанных питомцем\n[data]: Вывод всей информации' )




lest = 0
command = 'go'
print('Для вывода информации о командах => ?')
while True:
        command = input('Введите команду: ')
        if command == 'stop':
            print('| Выход |')
            exit()

        elif command == 'create':
         lest += 1
         create()
         
        elif command == 'read':
            num = int(input('Введите ID питомца на которого нужна информация: '))
            if num in pets.keys():    
                read(num)
            else:
                print('Не верный ID!')

        elif command == 'update':
            num = int(input('Введите ID питомца информазию которого вы хотите обновить: '))
            if num in pets.keys():
                update(num)
            else:
                print('Не верный ID!')

        elif command == 'delete':
             num = int(input('Введите ID питомца запись которого хотите удалить:'))
             if num in pets.keys():
                delete(num)
             else:
                 print('Не верный ID!')

        elif command == 'list':
            _list()

        elif command == 'data':
            _data()

        elif command == '?':
             info()
        else:
            print('Такой команды нет!')


