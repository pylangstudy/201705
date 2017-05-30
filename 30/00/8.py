def MyFunc(req, *args, **kwargs):
    print('----- MyFunc -----')
    print('req={0}'.format(req))
    print('*args')
    for arg in args:
        print(arg)
    print('**kwargs')
    for key, value in kwargs.items():
        print(key, value)

MyFunc('必須引数値', *[1, 'abc'], **{'key1': 'value1', 'key2': 'value2'})
a = [1, 'abc']
d = {'key1': 'value1', 'key2': 'value2'}
MyFunc('必須引数値', *a, **d)
