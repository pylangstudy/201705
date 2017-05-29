def func(arg, opt=1, *args, **kwargs):
    print(arg, opt, args, kwargs)

func(0)
func(0, 10)
func(0, 10, 20)
func(0, 10, 20, 30)
func(0, 10, 20, 30, key='value')
func(0, 10, 20, 30, key='value', key2='v2')
