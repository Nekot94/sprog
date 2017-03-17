number = 4  # int - целое
number2 = 5.1 # float - везественное
b = True # bool - логический
name = "Гаджикурбан" # str - строка
print(name[0])
print(name[5:10]) # срез
print(name[5:]) # срез
print(name[0:5]) # срез
print(name[-5:-1]) # срез
print(name[-5:-1]) # срез
print(name[0:10:3]) # срез c шагом
print(name[10:4:-1]) 
print(len(name)) # длна строки
stiho = """Мороз и солнце день чудесный,
У лукоморья дуб зеленый.
Я с губ любимой нежность пью,
Пора красавица проснись""" 
print(stiho)
print(stiho.find(",")) # поиск
print(stiho.rfind(",")) # поис с обратной стороны
print(stiho.count("у")) # колличество вхождений

print(stiho.upper()) # к большим буквам
print(stiho.lower()) # к маленьким буквам  
print(stiho.title()) # каждое слово с большой буквы

print(stiho.replace("дуб","губ")) # замена



