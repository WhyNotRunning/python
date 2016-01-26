import math
mList = ['Tom','Joy','Mal']
mTuple = (1,2,'Tom')
mDict = {'Tom':99,'Joy':88,'Mal':77}
mSet = set([1,2,3])
mStr = 'ABCD'
mGenerator = (x * x for x in range(1,10))
#切片
l = mList
print(l)
print(l[0:3])
print(l[0:2])
print(l[-2:-1]) #支持最后一个节点为-1
print(l[:1]) #默认为0时可以省略

#迭代
for x in mList:
	print(x)
for x in mStr:
	print(x)
from collections import Iterable
print(isinstance('abc', Iterable)) # str是否可迭代
#同时引用了两个变量，在Python里是很常见的
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(mList):
	print(i,value)

#列表生产式
#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
l = []
for x in range(1,10):
	l.append(x)
print(l)
#2
l = []
for x in range(1,10):
	l.append(x*x)
print(l)
#3
l = [x*x for x in range(1,10)]
print(l)
#4 包含if判断
l = [x*x for x in range(1,10) if x % 2 == 0 ]
print(l)
#5 双层循环
l=[m + n for m in 'ABC' for n in 'abc']
print(l)
#6 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os #导入os模块
l = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
#7for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
for k,v in mDict.items():
	print(k,'=',v)

#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
#不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

#所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
l = [x * x for x in range(1,10)] #list
g = (x * x for x in range(1,10)) #generator
#一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(mGenerator)) 
for x in mGenerator:
	print(x)
#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib(max):
	n, a, b = 0, 0, 1
	while n<max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(3)
o = odd()
print(next(o),next(o),next(o))
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break
