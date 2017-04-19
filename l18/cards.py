from random import shuffle

def get_card(player):
    while True:
        yield player["Колода"].pop()

def step(player1, player2):
    k = 0
    for card1, card2 in zip(get_card(player1),get_card(player2)):
        print(card1, card2)
        k += 2
        if card1[1] > card2[1]:
            player1["Счет"] += k
            break
        if card2[1] > card1[1]:
            player2["Счет"] += k
            break




suit = ["Червы","Крести","Бубны", "Пики"]
deck = [(s,n) for s in suit for n in range(6,15)]
# print(deck)
shuffle(deck)
# print(deck)
player1, player2 = {}, {}
player1["Колода"] = deck[:len(deck) // 2]
player2["Колода"] = deck[len(deck) // 2:]
player1["Счет"] = 0
player2["Счет"] = 0

print(player1["Колода"], player2["Колода"])

while player1["Колода"] and player2["Колода"]:
    step(player1,player2)
    print(player1["Счет"],player2["Счет"])
    input()
