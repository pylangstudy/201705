def IsContains(item):
    for i in ['abc','def','ghi']:
        if i == item:
            break
    else:
        return False
    return True
print(IsContains('ghi'))

