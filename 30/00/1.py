def MyFunc(title, *args):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)

MyFunc('可変引数は必須引数より前に置くこと。', 1, 'abc')
