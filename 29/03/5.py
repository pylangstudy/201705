from collections import OrderedDict
d = OrderedDict()
d['key1'] = 'value1'
d['key2'] = 'value2'
d['key3'] = 'value3'
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
