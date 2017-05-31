def ReturnKey(item):
    return item['key']

l = [{'key': 300}, {'key': 200}, {'key': 100}]
print(l)
l.sort(key = ReturnKey)
print(l)
