import sys


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


def StructVision(GetStruct):
    for SubStruct in GetStruct:
        print(SubStruct)
    print(f"\n Розмір словника: {sys.getsizeof(GetStruct)} байт")


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
    elif EventMenu == "exit":
        MainStruct.clear()
        del MainStruct
        print("Бувай!!!")
        break
    elif EventMenu == "vision":
        StructVision(MainStruct)
    elif EventMenu == "sort":
        MainStruct.sort(key=SortStruct)