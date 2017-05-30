def MyFunc(*args, title):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)

MyFunc(1, 'abc', '可変引数は必須引数より前に置くこと。')
