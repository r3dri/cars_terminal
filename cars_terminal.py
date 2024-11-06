import os
import tabulate  #библиотека для таблиц

columns = ['№', 'Производитель', 'Модель', 'Цвет', 'Коробка передач', 'Привод','Тип двигателя','Заведена/Не заведена','Открыта/Закрыта'] #названия столбцов

#Функции ↓ ↓ ↓ ↓ ↓ ↓
def showdata(): #txt в таблицу
    d=open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    r=[]
    for i in d:
        s=[x for x in i.split("/")]
        r.append(s)
    return r
def find_num(): #нахождение последнего номера
    d = open('../../Desktop/cars_terminal/data_source.txt', encoding='utf-8').readlines()
    r=[]
    number=0
    for i in d:
        s = [x for x in i.split("/")]
        r.append(s)
    for i in range(len(r)):
        num1=r[i][0]
        if int(num1)>number:
            number=int(num1)
    return number
def delete_car_func(x): # Удалить машину функция
    os.system('clear')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))  # таблица
    print("")
    number_for_delete = x
    os.system('clear')
    d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
    rdata = []
    for i in d:
        s = [x for x in i.split("/")]
        if int(s[0]) != number_for_delete: #убираем машину
            rdata.append(s)
    for i in range(len(rdata)): #сдвигаем номер
        rdata[i][0]=str(i+1)
    s = ["/".join(x) for x in rdata]
    file.truncate(0)
    for i in s: #редачим файл
        file.write(str(i))
    file.close()
    page_data()
def showtask(x): #выводить список
    d=open(f'../../Desktop/cars_terminal/data_{x}.txt', 'r+', encoding='utf-8').readlines()
    for i in d:
        print(i.strip())
def showmarks(x): #выводим список моделей по производителю
    d=open(f'../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
    for i in d:
        s=[x.strip() for x in i.split("/")]
        if s[0]==x:
            for i in range(1,len(s)):
                print(s[i])

def add_mark_again(vvod_fabric):
    os.system('clear')
    d = open(f'../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
    r3 = [x for x in d]
    r4 = []
    count = 0
    vvod_marka2 = input("Введите модель для добавления: ")
    if vvod_marka2.count("/") == 0:
        for i in r3:
            s = [x.strip() for x in i.split("/")]
            if vvod_fabric in s:
                s.append(vvod_marka2)
                count += 1
            r4.append('/'.join(s))
        if count == 0: r4.append(f'{vvod_fabric}/{vvod_marka2}')
        file = open(f'../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8')
        file.truncate(0)
        for i in r4:  # редачим файл
            file.write(f'{i}\n')
        file.close()
    else:
        print("Введен запрещенный символ => / ")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Добавить еще модель")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                k += 1
            except:
                print("")
        if vvod_data3 == 1:
            os.system('clear')
            page_main()
        elif vvod_data3 == 2:
            os.system('clear')
            add_mark_again(vvod_fabric)
        else:
            os.system('clear')
            page_main()
    print(f"Модели производителя {vvod_fabric}:")
    showmarks(vvod_fabric)
    print("_______________________")
    print("1.Вернуться на главную")
    print("2.Добавить еще модель")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            k += 1
        except:
            print("")
    if vvod_data3 == 1:
        os.system('clear')
        page_main()
    elif vvod_data3 == 2:
        os.system('clear')
        add_mark_again(vvod_fabric)
    else:
        os.system('clear')
        page_main()
def add_again():
    print("_______________________")
    print("1.Вернуться на главную")
    print("2.Повторить добавление")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
            k += 1
        except:
            print("")
    if vvod_data == 1:
        os.system('clear')
        page_main()
    elif vvod_data == 2:
        add_car()

#Страницы ↓ ↓ ↓ ↓ ↓ ↓
def page_main():  # основная страница
    print('База данных машин')
    print('1.Список машин')
    print('2.Добавить авто')
    print('3.Удалить авто')
    print('4.Изменить авто')
    print('5.Поиск авто')
    print('6.Списки параметров')
    print('7.Выйти')
    print('')
    k=0
    while k==0: #проверка на буквы
        try:
            vvod_main = int(input("Для выбора страницы введите ее номер(1-7):"))
            k+=1
        except: print("")
    if vvod_main == 1: page_data()
    elif vvod_main == 2: add_car()
    elif vvod_main == 3: delete_car()
    elif vvod_main == 4: change_car()
    elif vvod_main == 5: find_car()
    elif vvod_main==6: page_tasks()
    elif vvod_main == 7:
        os.system('clear')
        exit()
    else:
        os.system('clear')
        page_main()
def page_data():  # Page 1.Список машин
    os.system('clear')
    print("Список машин")
    data=showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))
    print("")
    print("_______________________")
    print("1.Вернуться на главную")
    print("2.Добавить авто")
    print("3.Удалить авто")
    print('4.Изменить авто')
    print('5.Выйти')
    k=0
    while k==0: #проверка на буквы
        try:
            vvod_data = int(input("Для выбора действия введите его номер(1-5):"))
            k+=1
        except: print("")
    if vvod_data==1:
        os.system('clear')
        page_main()
    elif vvod_data==2: add_car()
    elif vvod_data==3: delete_car()
    elif vvod_data==4: change_car()
    elif vvod_data==5:
        os.system('clear')
        exit()
    else:
        os.system('clear')
        page_data()
def add_car(): #Page 2. Добавить машину
    os.system('clear')
    num = find_num() + 1
    d2 = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
    data_proizvod=open('../../Desktop/cars_terminal/data_proizvod.txt', 'r+', encoding='utf-8')
    data_marka=open('../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
    r=[]
    for i in data_proizvod:
        r.append(i.rstrip())
    showtask("proizvod")
    vvod_fabric = input("Выберите производителя авто:")
    if vvod_fabric in r:
        os.system('clear')
        showmarks(vvod_fabric)
        vvod_mark=input(f"Выберите модель производителя {vvod_fabric}:")
        r2=[]
        for i in data_marka:
            s = [x.strip() for x in i.split("/")]
            if s[0] == vvod_fabric:
                r2=s
        if vvod_mark in r2:
            os.system('clear')
            data_color=open('../../Desktop/cars_terminal/data_color.txt', 'r+', encoding='utf-8').readlines()
            r = []
            for i in data_color:
                r.append(i.rstrip())
            showtask("color")
            vvod_color=input("Введите цвет:")
            if vvod_color in r:
                os.system('clear')
                print("Коробка передач:")
                print("1.Автомат")
                print("2.Механика")
                print("3.Робот")
                print("4.Вариатор")
                k = 0
                while k == 0:  # проверка на буквы
                    try:
                        vvod_data = int(input("Для выбора коробки передач введите ее номер(1-4):"))
                        k += 1
                    except: print("")
                if vvod_data<5:
                    if vvod_data == 1: KPP="Автомат"
                    elif vvod_data == 2: KPP="Механика"
                    elif vvod_data == 3: KPP = "Робот"
                    elif vvod_data == 4: KPP = "Вариатор"
                    os.system('clear')
                    print("Выберите привод:")
                    print("1.Задний")
                    print("2.Передний")
                    print("3.Полный")
                    k = 0
                    while k == 0:  # проверка на буквы
                        try:
                            vvod_data = int(input("Для выбора привода введите его номер(1-3):"))
                            k += 1
                        except:
                            print("")
                    if vvod_data <4:
                        if vvod_data ==1: privod="Задний"
                        elif vvod_data==2: privod="Передний"
                        elif vvod_data == 3:privod = "Полный"
                        os.system('clear')
                        print("Выберите тип двигателя:")
                        print("1.Бензиновый")
                        print("2.Дизельный")
                        print("3.Инжекторный")
                        print("4.Роторный")
                        print("5.Гибридный")
                        k = 0
                        while k == 0:  # проверка на буквы
                            try:
                                vvod_data = int(input("Для выбора типа двигателя введите его номер(1-5):"))
                                k += 1
                            except:
                                print("")
                        if vvod_data < 6:
                            if vvod_data == 1: dvig="Бензиновый"
                            elif vvod_data == 2: dvig="Дизельный"
                            elif vvod_data == 3: dvig="Инжекторный"
                            elif vvod_data == 4: dvig="Роторный"
                            elif vvod_data == 5: dvig="Гибридный"
                            os.system('clear')
                            print("Заведена/Не заведена машина?:")
                            print("1.Заведена")
                            print("2.Не заведена")
                            k = 0
                            while k == 0:  # проверка на буквы
                                try:
                                    vvod_data = int(input("Для выбора варианта введите его номер(1-2):"))
                                    k += 1
                                except:
                                    print("")
                            if vvod_data < 3:
                                if vvod_data == 1: onoff = "Заведена"
                                elif vvod_data == 2: onoff = "Не заведена"
                                os.system('clear')
                                print("Открыта/Закрыта машина?:")
                                print("1.Открыта")
                                print("2.Закрыта")
                                k = 0
                                while k == 0:  # проверка на буквы
                                    try:
                                        vvod_data = int(input("Для выбора варианта введите его номер(1-2):"))
                                        k += 1
                                    except: print("")
                                if vvod_data < 3:
                                    if vvod_data == 1: closeop = "Открыта"
                                    elif vvod_data == 2: closeop = "Закрыта"
				    os.system('clear')
				    print("Фары горят/Не горят?:")
				    print("1. Горят")
				    print("2. Не горят")
				    k = 0
				    while k == 0:
					try:
					    vvod_data = int(input("Для выбора варианта введите его номер(1-2):"))
					    k += 1
					except:
					    print("")
				    if vvod_data < 3:
					if vvod_data == 1:
					    lights = "Фары горят"
					elif vvod_data == 2:
					    lights = "Фары не горят"
                                    car_string = f'{num}/{vvod_fabric}/{vvod_mark}/{vvod_color}/{KPP}/{privod}/{dvig}/{onoff}/{closeop}/{lights}'  # новая строка
                                    for i in d2:
                                        file.write(str(i))
                                    file.write(f"{car_string}\n")
                                    file.close()
                                    page_data()
                                else:
                                    print("Такого варианта нет")
                                    add_again()
                            else:
                                print("Такого варианта нет")
                                add_again()
                        else:
                            print("Такого типа двигателя нет")
                            add_again()
                    else:
                        print("Такого привода нет")
                        add_again()
                else:
                    print("Такой коробки передач нет")
                    add_again()
            else:
                print("Такого цвета нет")
                add_again()
        else:
            print("Такой модели нет")
            add_again()
    else:
        print("Такого производителя нет")
        add_again()

def delete_car(): #Page 3. Удалить машину
    os.system('clear')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))  # таблица
    d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    lines = len(d)
    print("")
    print("_______________________")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_delete = int(input(f"Для удаления машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_delete<=lines:
        os.system('clear')
        file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
        rdata = []
        for i in d:
            s = [x for x in i.split("/")]
            if int(s[0]) != number_for_delete: #убираем машину
                rdata.append(s)
        for i in range(len(rdata)): #сдвигаем номер
            rdata[i][0]=str(i+1)
        s = ["/".join(x) for x in rdata]
        file.truncate(0)
        for i in s: #редачим файл
            file.write(str(i))
        file.close()
        page_data()
    else:
        os.system('clear')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Удалить авто")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('clear')
            page_main()
        elif vvod_data == 2:
            delete_car()
def change_car(): #Page 4. Редачить машину
    os.system('clear')
    data=showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe')) #таблица
    print("")
    d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    d_proizvod = open('../../Desktop/cars_terminal/data_proizvod.txt', 'r+', encoding='utf-8').readlines()
    lines=len(d)
    print("_______________________")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_change = int(input(f"Для редактирования данных машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_change<=lines:
        os.system('clear')
        rdata=[]
        r = []
        rs=[x.strip() for x in d_proizvod]
        for i in d:
            r = []
            s = [x for x in i.split("/")]
            rdata.append(s)
            if int(s[0]) == number_for_change: #сравниваем номер
                r.append(s)
        print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
        print("")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Изменить производителя")
        print("3.Изменить модель")
        print("4.Изменить цвет")
        print("5.Изменить коробку передач")
        print("6.Изменить привод")
        print("7.Изменить тип двигателя")
        print("8.Изменить Заведена/Не заведена")
        print("9.Изменить Открыта/Закрыта")
	print("10. Изменить Фары горят/не горят")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-10):"))
                k+=1
            except: print("")
        if vvod_data==1:
            os.system('clear')
            page_main()
        elif vvod_data==2:
            showtask("proizvod")
            vvod_fabric = input("Выберите производителя авто:")
            if vvod_fabric in rs:
                os.system('clear')
                showmarks(vvod_fabric)
                data_marka = open('../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
                vvod_mark = input(f"Выберите модели производителя {vvod_fabric}:")
                r2 = []
                for i in data_marka:
                    s = [x.strip() for x in i.split("/")]
                    if s[0] == vvod_fabric:
                        r2 = s
                if vvod_mark in r2:
                    rdata = []
                    for i in d:
                        r = []
                        s = [x for x in i.split("/")]
                        rdata.append(s)
                    rdata[number_for_change-1][1]=vvod_fabric
                    rdata[number_for_change - 1][2] = vvod_mark
                    os.system('clear')
                    file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
                    s = ["/".join(x) for x in rdata]
                    for i in s:
                        file.write(str(i))
                    file.close()
                    print("Успешно")
                    print("_______________________")
                    print("1.Вернуться на главную")
                    print("2.Повторная замена")
                    vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                    if vvod_data3==1:
                        os.system('clear')
                        page_main()
                    elif vvod_data3 == 2:
                        change_car()
                else: print("такой модели нет")
            else: print("такого производителя нет",rs)
        elif vvod_data==3:
            os.system('clear')
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            vvod_fabric=rdata[number_for_change-1][1]
            showmarks(vvod_fabric)
            data_marka = open('../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
            vvod_mark = input(f"Выберите модель производителя {vvod_fabric}:")
            r2 = []
            for i in data_marka:
                s = [x.strip() for x in i.split("/")]
                if s[0] == vvod_fabric:
                    r2 = s
            if vvod_mark in r2:
                rdata[number_for_change - 1][1] = vvod_fabric
                rdata[number_for_change - 1][2] = vvod_mark
                os.system('clear')
                file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
                s = ["/".join(x) for x in rdata]
                for i in s:
                    file.write(str(i))
                file.close()
                print("Успешно")
                print("_______________________")
                print("1.Вернуться на главную")
                print("2.Повторная замена")
                k = 0
                while k == 0:  # проверка на буквы
                    try:
                        vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                        k += 1
                    except:
                        print("")
                if vvod_data3 == 1:
                    os.system('clear')
                    page_main()
                elif vvod_data3 == 2:
                    change_car()
            else:
                print("такой модели нет")
                print("_______________________")
                print("1.Вернуться на главную")
                k = 0
                while k == 0:  # проверка на буквы
                    try:
                        vvod_data4 = int(input("Для выбора действия введите его номер:"))
                        k += 1
                    except:
                        print("")
                if vvod_data4 == 1:
                    os.system('clear')
                    page_main()
        elif vvod_data==4:
            os.system('clear')
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            showtask("color")
            data_color = open('../../Desktop/cars_terminal/data_color.txt', 'r+', encoding='utf-8').readlines()
            r2=[x.strip() for x in data_color]
            vvod_color = input("Выберите цвет машины:")
            if vvod_color in r2:
                rdata[number_for_change - 1][3] = vvod_color
                os.system('clear')
                file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
                s = ["/".join(x) for x in rdata]
                for i in s:
                    file.write(str(i))
                file.close()
                print("Успешно")
                print("_______________________")
                print("1.Вернуться на главную")
                print("2.Повторная замена")
                vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                if vvod_data3 == 1:
                    os.system('clear')
                    page_main()
                elif vvod_data3 == 2:
                    change_car()
            else:
                print("такого цвета нет")
        elif vvod_data==5:
            os.system('clear')
            print("Коробка передач:")
            print("1.Автомат")
            print("2.Механика")
            print("3.Робот")
            print("4.Вариатор")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data = int(input("Для выбора коробки передач введите ее номер(1-4):"))
                    k += 1
                except:
                    print("")
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            if vvod_data == 1: KPP = "Автомат"
            elif vvod_data == 2: KPP = "Механика"
            elif vvod_data == 3: KPP = "Робот"
            elif vvod_data == 4: KPP = "Вариатор"
            rdata[number_for_change - 1][4] = KPP
            os.system('clear')
            file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
            s = ["/".join(x) for x in rdata]
            for i in s:
                file.write(str(i))
            file.close()
            print("Успешно")
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                change_car()
        elif vvod_data==6:
            os.system('clear')
            print("Привод:")
            print("1.Задний")
            print("2.Передний")
            print("3.Полный")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data = int(input("Для выбора коробки передач введите ее номер(1-4):"))
                    k += 1
                except:
                    print("")
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            if vvod_data == 1:privod = "Задний"
            elif vvod_data == 2:privod = "Передний"
            elif vvod_data == 3:privod = "Полный"
            rdata[number_for_change - 1][5] = privod
            os.system('clear')
            file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
            s = ["/".join(x) for x in rdata]
            for i in s:
                file.write(str(i))
            file.close()
            print("Успешно")
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                change_car()
        elif vvod_data==7:
            os.system('clear')
            print("Выберите тип двигателя:")
            print("1.Бензиновый")
            print("2.Дизельный")
            print("3.Инжекторный")
            print("4.Роторный")
            print("5.Гибридный")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data = int(input("Для выбора коробки передач введите ее номер(1-4):"))
                    k += 1
                except:
                    print("")
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            if vvod_data == 1:   dvig = "Бензиновый"
            elif vvod_data == 2: dvig = "Дизельный"
            elif vvod_data == 3: dvig = "Инжекторный"
            elif vvod_data == 4: dvig = "Роторный"
            elif vvod_data == 5: dvig = "Гибридный"
            rdata[number_for_change - 1][6] = dvig
            os.system('clear')
            file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
            s = ["/".join(x) for x in rdata]
            for i in s:
                file.write(i)
            file.close()
            print("Успешно")
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                change_car()
        elif vvod_data==8:
            os.system('clear')
            print("Заведена/Не заведена машина?:")
            print("1.Заведена")
            print("2.Не заведена")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data = int(input("Для выбора коробки передач введите ее номер(1-2):"))
                    k += 1
                except:
                    print("")
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            if vvod_data == 1: onoff = "Заведена"
            elif vvod_data == 2: onoff = "Не заведена"
            rdata[number_for_change - 1][7] = onoff
            os.system('clear')
            file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
            s = ["/".join(x) for x in rdata]
            for i in s:
                file.write(i)
            file.close()
            print("Успешно")
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                change_car()
        elif vvod_data==9:
            os.system('clear')
            print("Открыта/Закрыта машина?:")
            print("1.Открыта")
            print("2.Закрыта")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data = int(input("Для выбора коробки передач введите ее номер(1-2):"))
                    k += 1
                except:
                    print("")
            d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
            rdata = []
            for i in d:
                r = []
                s = [x for x in i.split("/")]
                rdata.append(s)
            if vvod_data == 1:   closeop = "Открыта"
            elif vvod_data == 2: closeop = "Закрыта"
            rdata[number_for_change - 1][8]=closeop
            file = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
            s = ["/".join(x) for x in rdata]
            for i in s:
                file.write(i)
            file.close()
            os.system('clear')
            print("Успешно")
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                change_car()
	elif vvod_data == 10:
	    os.system('clear')
	    print("Фары горят/Не горят?:")
	    print("1. Фары горят")
	    print("2. Фары не горят")
	    k = 0
	    while k == 0:
		try:
		    vvod_data = int(input("Для выбора варианта введите его номер (1-2):"))
		    k += 1
		except:
		    print("")
	    d = open('../../Dekstop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
	    rdata = []
	    for i in d:
		r = []
		s = [x for x in i.split("/")]
		rdata.append(s)
	    if vvod_data == 1:
		lights = "Фары горят"
	    elif vvod_data == 2:
		lights = "Фары не горят"
	    rdata[number_for_change - 1][9] = lights
	    for open('../../Dekstop/cars_terminal/data_source.txt', 'r+', encoding='utf-8')
	    s = ["/".join(x) for x in rdata]
	    for i in s:
		file.write(i)
	    file.close()
	    os.system('clear')
	    print("Успешно")
	    print("___________________")
	    print("1. Вернуться на главную")
	    print("2. Повторная замена")
	    vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
	    if vvod_data3 == 1:
		os.system('clear')
		page_main()
	    elif vvod_data3 == 2:
		change_car()
        else:
            os.system('clear')
            change_car()
    else:
        os.system('clear')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Изменить авто")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('clear')
            page_main()
        elif vvod_data == 2:
            change_car()
        else:
            os.system('clear')
            page_main()
def find_car(): #Page 5. Найти машину
    os.system('clear')
    d = open('../../Desktop/cars_terminal/data_source.txt', 'r+', encoding='utf-8').readlines()
    lines = len(d)
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_find=int(input(f"Для поиска машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_find<=lines:
        for i in d:
            r=[]
            s = [x for x in i.split("/")]
            if int(s[0])==number_for_find:
                r.append(s)
                print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
        print("")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Повторный поиск")
        print("3.Удалить эту машину")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-4):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('clear')
            page_main()
        elif vvod_data == 2:
            find_car()
        elif vvod_data == 3:
            delete_car_func(number_for_find)
    else:
        os.system('clear')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Повторный поиск")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except:
                print("")
        if vvod_data == 1:
            os.system('clear')
            page_main()
        elif vvod_data == 2:
            find_car()
        else:
            os.system('clear')
            page_main()

def page_tasks(): #page 6. Все параметры
    os.system('clear')
    print("1.Список производителей")
    print("2.Список моделей")
    print("3.Список цветов")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data = int(input("Для выбора действия введите его номер(1-3):"))
            k+=1
        except:
            print("")
    if vvod_data == 1 or vvod_data==3:
        os.system('clear')
        listtask(vvod_data)
    elif vvod_data == 2:
        os.system('clear')
        listmarks()
    else:
        os.system('clear')
        page_main()

def listtask(x):
    r=["proizvod","marka","color"]
    r2=["производителя","модель","цвет"]
    showtask(r[x-1])
    print("_______________________")
    print("1.Вернуться на главную")
    print(f"2.Добавить {r2[x-1]}")
    print(f"3.Удалить {r2[x-1]}")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data3 = int(input("Для выбора действия введите его номер(1-3):"))
            k += 1
        except:
            print("")
    if vvod_data3 == 1:
        os.system('clear')
        page_main()
    elif vvod_data3 == 2:
        os.system('clear')
        s=input(f"Введите {r2[x-1]} для добавления: ")
        d=open(f'../../Desktop/cars_terminal/data_{r[x-1]}.txt', 'r+', encoding='utf-8').readlines()
        r3=[x for x in d]
        r3.append(f'{s}\n')
        file = open(f'../../Desktop/cars_terminal/data_{r[x-1]}.txt', 'r+', encoding='utf-8')
        file.truncate(0)
        for i in r3:  # редачим файл
            file.write(i)
        file.close()
    elif vvod_data3 == 3:
        os.system('clear')
        s = input(f"Введите {r2[x - 1]} для удаления: ")
        d = open(f'../../Desktop/cars_terminal/data_{r[x - 1]}.txt', 'r+', encoding='utf-8').readlines()
        r3 = [x for x in d]
        r3.remove(f'{s}\n')
        file = open(f'../../Desktop/cars_terminal/data_{r[x - 1]}.txt', 'r+', encoding='utf-8')
        file.truncate(0)
        for i in r3:  # редачим файл
            file.write(i)
        file.close()
    else:
        os.system('clear')
        page_main()
    showtask(r[x - 1])
    print("_______________________")
    print("1.Вернуться на главную")
    print("2.Вернуться в списки параметров")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
            k += 1
        except:
            print("")
    if vvod_data3 == 1:
        os.system('clear')
        page_main()
    elif vvod_data3 == 2:
        os.system('clear')
        page_tasks()
    else:
        os.system('clear')
        page_main()

def listmarks():
    os.system('clear')
    d = open(f'../../Desktop/cars_terminal/data_proizvod.txt', 'r+', encoding='utf-8').readlines()
    r3=[]
    for i in d:
        r3.append(i)
    showtask("proizvod")
    print("_______________________")
    vvod_fabric = input("Введите производителя, модель которого хотите добавить/удалить: ")
    os.system('clear')
    if f'{vvod_fabric}\n' in r3:
        print(f"Модели производителя {vvod_fabric}:")
        showmarks(vvod_fabric)
        print("_______________________")
        print("1.Вернуться на главную")
        print(f"2.Добавить модель")
        print(f"3.Удалить модель")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data3 = int(input("Для выбора действия введите его номер(1-3):"))
                k += 1
            except:
                print("")
        if vvod_data3 == 1:
            os.system('clear')
            page_main()
        elif vvod_data3 == 2:
                os.system('clear')
                add_mark_again(vvod_fabric)
        elif vvod_data3==3:
            os.system('clear')
            d = open(f'../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8').readlines()
            r3 = [x for x in d]
            r4 = []
            print(f"Модели производителя {vvod_fabric}:")
            showmarks(vvod_fabric)
            vvod_marka2 = input("Введите модель для удаления: ")
            for i in r3:
                s = [x.strip() for x in i.split("/")]
                if vvod_marka2 in s:
                    s.remove(vvod_marka2)
                r4.append('/'.join(s))
            file = open(f'../../Desktop/cars_terminal/data_marka.txt', 'r+', encoding='utf-8')
            file.truncate(0)
            for i in r4:  # редачим файл
                file.write(f'{i}\n')
            file.close()
            os.system('clear')
            print(f"Модели производителя {vvod_fabric}:")
            showmarks(vvod_fabric)
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Вернуться в списки параметров")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                    k += 1
                except:
                    print("")
            if vvod_data3 == 1:
                os.system('clear')
                page_main()
            elif vvod_data3 == 2:
                os.system('clear')
                page_tasks()
            else:
                os.system('clear')
                page_main()
    else:
        print("Такого производителя нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Ввести другого производителя")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data4 = int(input("Для выбора действия введите его номер(1-2):"))
                k += 1
            except:
                print("")
        if vvod_data4 == 1:
            os.system('clear')
            page_main()
        elif vvod_data4 == 2:
            os.system('clear')
            listmarks()
        else:
            os.system('clear')
            page_main()

os.system('clear')
page_main()
