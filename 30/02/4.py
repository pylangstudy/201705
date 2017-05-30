from operator import itemgetter
d = {'Z': 1, 'Y': 2, 'X': 3, 'W': 4}
print(d)
print(sorted(d.items(), key=itemgetter(1)))
