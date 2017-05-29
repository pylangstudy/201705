def Append(value, l=None):
    if l is None:
        l = []
    l.append(value)
    return l

print(Append(1))
print(Append(2))
print(Append(3))
print(Append(7,[1,3,5]))
