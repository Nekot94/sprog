print("Стоял старый дом. В нем жили призраки. \
Ты захотел это проверить. Твои действия\n\n \
    1.войти через окно\n \
    2.войти через двер.")
num = input()
if  num == "1":
    print("на тебя на пали два злобных призрака. \
К сожалению они выпили душу\n Конец.")
else:
    print("Ты входишь в дверь и вокруг тебя появляются \
три призрака. Ты сжимаешь кулаки и призраки пропадают.\n \
    1.Войти в соседнюю дверь\n \
    2.Подняться по лестнице.")
    num = input()
    if num == "1":
        print("Тебя встречают три добрых зомби. Ты умер.")
    else:
        print("В комнате появляется джин. Я исполню любое \
твое желание.\n \
    1. прибрести меч.\n \
    2. дай мне пылесос!!!\n \
    3. Порше панамера")
        num = input()
        if num == "1":
            print("Сверху появляется мечь и пронзает тебя насквозь")
        elif num == "2":
            print("Вас засасывает в огромный пылесос.\n конец")
        else:
            print("Перед домом появляется ноенькая машина. \
Вы живете счастливо.\n \
Правда всего 3 дня. \n Конец")
