def intro(name: str='default', age: int=100) -> str:
    print(intro.__annotations__)
    return "私は{0}です。{1}歳です。".format(name, age)

print(intro(None, 'abc'))
print(intro())
