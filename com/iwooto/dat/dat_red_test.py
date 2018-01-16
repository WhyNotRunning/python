
import sys, shelve

# file = shelve.open("d:\\test.dat")
file = shelve.open("data.dat")
dataKey = 'test'
print(file[dataKey])
file.close()


