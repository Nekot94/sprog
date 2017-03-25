ru_eng = {
    "и":"and",
    "лягушка":"frog",
    "зло":"evil",
    "лисица": "fox"
} # словарь - dict
print(ru_eng)
print(ru_eng["лисица"])
ru_eng["зло"] = "harm" # изменить значение
print(ru_eng["зло"])
ru_eng["компьютер"] = "computer"
print(ru_eng["компьютер"])

word = input("Введите руское слово: ")
translate = input("Введите перевод на английский: ")
ru_eng[word] = translate
print(ru_eng)

word = input("Введите русское слово: ")
if word in ru_eng: # проверить наличие в словаре
    print(ru_eng[word])
else:
    print("Не знаю")