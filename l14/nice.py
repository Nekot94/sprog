a = 8
b = 4.8
n = "Омар"
print(n + " хороший человек. У него " + str(a) + " зверей и его средний бал:" + str(b))

print("%10.2s хороший человек. У него %10.5d зверей и его средний бал: %10.1f%%" %(n, a, b))

print("{0} хороший человек. У него {0} зверей и его средний бал:{0}".format(n, a, b))
print("{0:*^10s} хороший человек. У него {1:3d} зверей и его средний бал:{2:2.2f}".format(n, a, b))

today = {"день":10, "месяц":4,"год":2017}
print("Cегодня {0[день]} число {0[месяц]} месяца {0[год]} года.".format(today))