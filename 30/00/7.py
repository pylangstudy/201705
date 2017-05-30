def MyFunc(**kwargs):
    print('----- MyFunc -----')
    for key, value in kwargs.items():
        print(key, value)

MyFunc(**{'key1': 'value1', 'key2': 'value2'})
d = {'key1': 'value1', 'key2': 'value2'}
MyFunc(**d)
