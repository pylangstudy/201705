l = [{'key': 300}, {'key': 200}, {'key': 100}]
print(l)
l.sort(key = lambda x: x['key'])
print(l)
