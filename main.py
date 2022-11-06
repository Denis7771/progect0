import sys


def StructVision(GetStruct1):
    for SubStruct in GetStruct1:
        print(SubStruct)


def StructDel(GetStruct):
    DelWord = input("Видалити слово: ")
    for SubStruct in GetStruct:
        if SubStruct['English'] == DelWord:
            GetStruct.pop(GetStruct.index(SubStruct))

def StructAdd(GetStruct):
    items = ['параграф', 'English', 'Українська']
    SubStructDict = dict.fromkeys(items)
    EngWord = input("Введите слово:")
    UaWord = input("Введите перевод слова:")
    SubStructTuple = ("Еnglish-Українська", EngWord[0])
    SubStructDict['параграф'] = SubStructTuple
    SubStructDict['English'] = EngWord
    SubStructDict['Українська'] = UaWord
    GetStruct.append(SubStructDict)


def SortStruct(e):
    return e['параграф'][1]


MainStruct = list()

while True:
    print('''----------
    додати слово -- add
    показати словник -- vision
    видалити слово -- del
    сортувати -- sort
    вихід -- exit
    ''')
    EventMenu = input("Виберіть потрібний пункт меню: ")
    if EventMenu == "add":
        StructAdd(MainStruct)
        print()
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    elif EventMenu == "exit":
        MainStruct.clear()
        del MainStruct
        print("Бувай!!!")
        break
    elif EventMenu == "vision":
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    elif EventMenu == "sort":
        MainStruct.sort(key=SortStruct)
    elif EventMenu == "del":
        StructDel(MainStruct)
        print()
        StructVision(MainStruct)
        print(f"\n Розмір словника: {sys.getsizeof(MainStruct)} байт")
    else:
        continue
