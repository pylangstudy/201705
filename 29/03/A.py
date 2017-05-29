from collections import OrderedDict
d = OrderedDict( (('key1'), ('key2','value2'), ('key3','value3')) )
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
