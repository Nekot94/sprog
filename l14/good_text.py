import random

adjective = ["Милый", "Добрый", "Глупый"]
subjects = ["Омар", "Магомед", "пистолет", "помидор"]
predicates = ["пошел", "убил", "полетел", "был сьеден"]
circumstances = ["в горы","на море", "коровой"]

for i in range(3):
    a = random.choice(adjective)
    s = random.choice(subjects)
    p = random.choice(predicates)
    c = random.choice(circumstances)
    print("{0} {1} {2} {3}.".format(a,s, p, c))