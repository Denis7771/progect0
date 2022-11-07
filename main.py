import sys


def StructVision(GetStruct1):
    for SubStruct in GetStruct1:
        print(SubStruct)


def StructDel(GetStruct):      #Функция удаление слова из словаря
    DelWord = input("Видалити слово: ")
    for SubStruct in GetStruct:
        if SubStruct['English'] == DelWord:
            GetStruct.pop(GetStruct.index(SubStruct))


def StructAdd(GetStruct):     #Создание Словаря
    items = ['параграф', 'English', 'Українська']
    SubStructDict = dict.fromkeys(items)
    EngWord = input("Введите слово:")
    UaWord = input("Введите перевод слова:")
    SubStructTuple = ("Еnglish-Українська", EngWord[0])
    SubStructDict['параграф'] = SubStructTuple
    SubStructDict['English'] = EngWord
    SubStructDict['Українська'] = UaWord
    GetStruct.append(SubStructDict)


def SortStruct(e):       #Функия сортировать словарь
    return e['параграф'][1]


MainStruct = list()

while True:    #Меню
    print('''----------
    додати слово -- add
    показати словник -- vision    
    видалити слово -- del
    сортувати -- sort
    вихід -- exit
    ''')
    EventMenu = input("Виберіть потрібний пункт меню: ")
    if EventMenu == "add":  #Добавить слово в Словарь
        StructAdd(MainStruct)
        print()
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    elif EventMenu == "exit":  #Выйти из Словаря
        MainStruct.clear()
        del MainStruct    #Удаляем для очистки памяти
        print("Бувай!!!")
        break
    elif EventMenu == "vision":   #Показать Словарь
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    elif EventMenu == "sort":  #Сортировать Словарь
        MainStruct.sort(key=SortStruct)
    elif EventMenu == "del":  #Удаление слова из Словаря
        StructDel(MainStruct)
        print()
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    else:
        continue
