def intro(name: str, age: int) -> str:
    print(intro.__annotations__)
    return "私は{0}です。{1}歳です。".format(name, age)

print(intro('山田', 999))
