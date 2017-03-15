name = input("Введите ваше имя: ")
number = int(input("Введите любое число: "))

if name == "Арсен" and not number >= 10: 
    print("Арсен молодец")
    print("и все...")
elif name == "Омар" or name == "Магомед":
    print("123")
else:
    print("это имя неизвестно")