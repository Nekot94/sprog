import random

player1 = {"Имя":"Магомед","Деньги":1000,"Ставка":0,"Бросок":0}
player2 = {"Имя":"Магомед","Деньги":1000,"Ставка":0,"Бросок":0}

player1["Имя"] = input("Введите имя 1-го игрока: ")
player2["Имя"] = input("Введите имя 2-го игрока: ")

while True:
    player1["Ставка"] = int(input(player1["Имя"] + " введите ставку: "))
    if player1["Ставка"] > player1["Деньги"]:
        player1["Ставка"] = player1["Деньги"]

    # print(player1["Ставка"])
    player2["Ставка"] = int(input(player2["Имя"] + " введите ставку: "))
    if player2["Ставка"] > player2["Деньги"]:
        player2["Ставка"] = player2["Деньги"]

    player1["Бросок"] = random.randint(1,6);
    player2["Бросок"] = random.randint(1,6);
    print(player1["Имя"],"выбросил",player1["Бросок"])
    print(player2["Имя"],"выбросил",player2["Бросок"])

    if player1["Бросок"] > player2["Бросок"]:
        print(player1["Имя"],"победил")
        player1["Деньги"] += player2["Ставка"]
        player2["Деньги"] -= player2["Ставка"]
    elif player2["Бросок"] > player1["Бросок"]:
        print(player2["Имя"],"победил")
        player2["Деньги"] += player1["Ставка"]
        player1["Деньги"] -= player1["Ставка"]
    else:
        print("Ничья")

    print(player1["Имя"],"Деньги:",player1["Деньги"])
    print(player2["Имя"],"Деньги:",player2["Деньги"])

    if player1["Деньги"] <= 0:
        print(player2["Имя"],"разорил",player1["Имя"])
        break
    elif player2["Деньги"] <= 0:
        print(player1["Имя"],"разорил",player2["Имя"])
        break
