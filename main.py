#Apple(a) - "english": "Apple", "Українська": "Яблоко"

#[{параграф: ('Еnglish-Українська','А'), "english": "point", "українська": "точка"},

MainStruct = []
while True:
    items = ['параграф', 'English', 'Українська']
    SubStructDict = dict.fromkeys(items)
    EngWord = input("Введите слово:")
    if EngWord == 'stop':
        break
    UaWord = input("Введите перевод слова:")
    if UaWord == 'stop':
        break
    SubStructTuple = ("Еnglish-Українська", EngWord[0])
    SubStructDict['параграф'] = SubStructTuple
    SubStructDict['English'] = EngWord
    SubStructDict['Українська'] = UaWord
    MainStruct.append(SubStructDict)
    print(MainStruct)





   # drr = input("Хотите вызвать меню?")
  #  if drr == "Да":
  #      q1 = input("Показать весь словарь?")
 #       if q1 == 'Да':
  #          for red in rer:
