def IsContains(item):
    for i in ['abc','def','ghi']:
        if i == item:
            return True
    return False
print(IsContains('ghi'))
