from operator import itemgetter
d = {'Z': {'age': 1}, 'Y': {'age': 2}, 'X': {'age': 3}, 'W': {'age': 4}}
print(d)
print(sorted(d, key=itemgetter('age')))
