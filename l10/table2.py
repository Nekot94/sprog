import random

random_number = random.randint(1,10)

answer = "2 * " + str(random_number) + " = "

while True:
    number = int(input(answer))
    if number == 2 * random_number:
        print("Ответил верно")
        break
    else:
        print("Ты ошибся") 