def MyFunc(option='オプション引数値です。', *args):
    print('----- option={0}'.format(option))
    for arg in args:
        print(arg)

MyFunc(*[1, 'abc'])
#MyFunc(option='abc', *[1, 'abc']) # TypeError: MyFunc() got multiple values for argument 'option'
MyFunc('abc', *[1, 'abc'])
