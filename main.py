#Apple(a) - "english": "Apple", "Українська": "Яблоко"


lol = []
while True:
    rer = input("Введите слово:")
    rer_1 = input("Введите перевод слова:")
    a = {"English:": rer, "Українська:": rer_1}
    c = ('Еnglish-Українська', rer[0])
    ter = (f'{c} - {a}')
    lol.append(ter)
    print(ter)

   # drr = input("Хотите вызвать меню?")
  #  if drr == "Да":
  #      q1 = input("Показать весь словарь?")
 #       if q1 == 'Да':
  #          for red in rer:
