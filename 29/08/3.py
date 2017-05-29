def Sum(value1, value2=200, value3=300):
    return value1 + value2 + value3

print(Sum(10))
print(Sum(10, 20))
print(Sum(10, 20, 30))
print(Sum(10, value2=20))
print(Sum(10, value3=30))
print(Sum(10, value2=20, value3=30))
