
import sys, shelve

file = shelve.open("data.dat")
data = {}
data['key1'] = '123456'
data['key2'] = 'abcdefg'
data['key3'] = 'ABCDEFG'
data['key4'] = {'test': 1, 'key': 123}
dataKey = 'test'
file[dataKey] = data
file.close()


