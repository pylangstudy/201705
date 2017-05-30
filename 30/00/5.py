def MyFunc(*args, option='オプション引数値です。'):
    print('----- option={0}'.format(option))
    for arg in args:
        print(arg)

MyFunc(*[1, 'abc'])
MyFunc(*[1, 'abc'], option='abc')
#MyFunc(*[1, 'abc'], 'abc') # SyntaxError: only named arguments may follow *expression
