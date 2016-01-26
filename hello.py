#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
mList = ['Tom','Joy','Mal']
mTuple = (1,2,'Tom')
mDict = {'Tom':99,'Joy':88,'Mal':77}
mSet = set([1,2,3])
mStr = 'ABCD'
mInt = int(123)
mGenerator = (x * x for x in range(1,10))
r'''
print('hello world')

1000+1000+2333
print(22+33)
print('100 + 200 =', 100 + 200)
'''
r'''
用户输入字符串 其中name是变量名可以直接输入name打印变量信息or print(name)

name = input() 
name
print(name)

name = input('赶快输入的你姓名:')
print('你好啊，',name)
'''

r'''
print('1024 * 768 = xxx')
print('1024 * 768 = ',1024*768)
'''

#以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。
#其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
r'''
#print("please input some world:")
a = 100
if a>0:
    print(a)
else:
    print(-a)
'''

r'''
#打印出I'm "OK" 的写法.转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m "OK"\nI\'m "OK" too')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试
print('\\\t\\')
print(r'\\\t\\')
'''
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''内容内容'''的格式表示多行内容

#print('''line1
#line2
#line3''')
#好像r'''...'''与'''...'''无法前途使用

#布尔值写法大小写敏感
r'''
True
5>3 #True
True or False #True
not True      #False
#python中的空值Null,0是有意义的
'''

#变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
r'''
a=1
t_007='t_007'
true='hahaha'
answer=True
print(answer)
answer=true
print(answer)
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，赋值语句如下（// 表示注释）：
int a = 123; // a是整数类型变量
a = "ABC"; // 错误：不能把字符串赋给整型变量
'''

#常量:但事实上Python根本没有任何机制保证PI不会被改变，
#所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
r'''
PI= 3.14159265359
print(PI)
#除法
print(10/3)              #答案：3.33333333333
#底板除，只保留整数位
print(10//3)               #答案：3
#余数
print(10%3)               #答案：1
'''
#编码：对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
r'''
print(ord('A'),
ord('中'),
chr(66),
chr(25991),'\u4e2d\u6587')
#如果知道字符的整数编码，还可以用十六进制这么写str
print('\u4e2d\u6587') #中文
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

#Python对bytes类型的数据用带b前缀的单引号或双引号表示
x= b'ABC'
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
abc = 'ABC'.encode('ascii') #b'ABC
print(abc)
'中文'.encode('utf-8')
#'中文'.encode('ascii') #含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#在bytes中，无法显示为ASCII字符的字节，用\x##显示。

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
test = b'ABC'.decode('ascii') #ABC
print(test)

#字符长度函数len()
print(len('中文'.encode('utf-8')))

#格式化：最后一个常见的问题是如何输出格式化的字符串。在Python中，采用的格式化方式和C语言是一致的，用%实现
print('hello , %s' %'world') #如果只有一个%?，括号可以省略。
print('Hi, %s, you have $%d.' %('zhangshan',10000))
#%d 整数
#%f 浮点数
#%s 字符串
#%x 十六进制整数
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate : %d%%' %7)
print('growth rate : 7%')
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d - %02d' %(3,1))
print('%.2f' %3.1415926)

add = 85 - 72
rate = add/72*100
print('%.1f%%' %rate)
'''

#list和tuple
r'''
#要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
classMates = ['Tom','Patter','Joy']
print(classMates)
print(len(classMates),classMates[0],classMates[2],classMates[-1]
    )
#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classMates.append('Test')
print(classMates)
print(len(classMates),classMates[0],classMates[2],classMates[-1]
    )
#也可以把元素插入到指定的位置，比如索引号为1的位置
classMates.insert(1,'index1')
print(classMates)
#要删除list末尾的元素，用pop()方法
classMates.pop()
print(classMates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classMates.pop(1)
print(classMates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classMates[0] = 'tom'
#list里面的元素的数据类型也可以不同
classMates = ['sss',111,True]
print(classMates)
#list元素也可以是其他list
classMates = ['sss',['ite','ites']]
print(len(classMates),classMates)

#tuple另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改.
classMates = ('Tom','Patter','Joy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，
#你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

#如果要定义一个空的tuple，可以写成()：
t = ()
print(t)
#定义一个元素
t = (1)
print(t)
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
#因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)
print(t)
##可变的tuple
t = ('a', 'b',['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。
#tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
'''

#条件判断
r'''
temp = input('输入你的年龄吧:\n')
age = int(temp)
if age<16:
    print('你是小学生吗？')
    print('你真的不是小学生吗？')
elif age<30:
    print('小伙子要努力工作啦!')
    print('我会的啦')
else:
    print('生活什么的才是最重要的啦')
'''

#循环
r'''
names = ['Tom','Joy','Mal']
for x in names:
    print(x)
print('-------------------------------')
for x in names:
    if x == 'Tom':
        print(x)
#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，
#再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数
temp = list(range(5))
print(temp)
#range(101)就可以生成0-100的整数序列，计算如下
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
#第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 1
while n<99:
    sum = sum + n
    n = n +2
print(sum)
'''

#字典dict和set
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
r'''
names = ['Tom','Joy','Mal']
soures = [99,88,77]
#如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
di = {'Tom':99,'Joy':88,'Mal':77}
print(di['Tom'])
di['Tom'] = 100
print(di['Tom'])
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Test' in di,'Tom' in di)
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(di.get('Test'))
print(di.get('Test',-1))
#注意：返回None的时候Python的交互式命令行不显示结果。
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
di.pop('Tom')
print(di)
'''
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而增加；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：


#set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
r'''
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.add(1)
print(s)
s.remove(4)
print(s)

#再议不可变对象

#上面我们讲了，str是不变对象，而list是可变对象。

#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
a = ['c','b','a']
a.sort() #对元素进行排序
print(a)

#而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b = a.replace('a','A')
print(b,a)
'''
#要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，
#但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'

#函数S=π*r*r
#当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。
#有了函数，我们就不再每次写s = 3.14 * x * x，
#而是写成更有意义的函数调用s = area_of_circle(x)，而函数area_of_circle本身只需要写一次，就可以多次调用。

#抽象
r'''
计算数列的和，比如：1 + 2 + 3 + ... + 100，写起来十分不方便，于是数学家发明了求和符号∑，可以把1 + 2 + 3 + ... + 100记作：
100
∑n
n=1
'''


#函数
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
r'''
print(abs(100))
print(abs(-100))
'''
#数据类型转换
r'''
print(int('123'),
#int('12.35'), 不能直接转换
int(float('12.35')),
float('12.35'),
str(12.3),
bool(1),
bool(''))
'''

#定义函数
r'''
def my_abs(x):
    if x>0:
        return x
    else:
        return -x
'''
#请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
#因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
#如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
#return None可以简写为return。
#Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下
#如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
#用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）

#空函数
#如果想定义一个什么事也不做的空函数，可以用pass语句：
r'''
def nop():
    pass
'''
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
#比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#参数检查
#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
#但是如果参数类型不对，Python解释器就无法帮我们检查。

#返回多个值
#函数可以返回多个值吗？答案是肯定的。
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：
r'''
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(11,33,3,math.pi/6))
'''
#但其实这只是一种假象，Python函数返回的仍然是单一值
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

#函数的参数
#定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，
#以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。
#Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
#使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。

#位置参数
r'''
def power(x):
    return x * x

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''
#修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
#默认参数
#新的power(x, n)函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用
#这个时候，默认参数就排上用场了。由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
r'''
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
'''
#这样，当我们调用power(5)时，相当于调用power(5, 2)
#
#先定义一个函数，传入一个list，添加一个END再返回：
r'''
def add_end(L=[]):
    L.append('END')
    return L
'''
r'''
#当你正常调用时，结果似乎不错：
add_end([1, 2, 3]) #[1, 2, 3, 'END']
#当你使用默认参数调用时，一开始结果也是对的：
add_end() #['END']
#但是，再次调用add_end()时，结果就不对了：  
add_end() #['END', 'END']
'''
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：
r'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
'''

#可变参数
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
#要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，
r'''
def calc(numbers):
    sum = 0
    for x in numbers:
        sum = sum + x*x
    return sum
calc([1,2,3])
'''
#但是调用的时候，需要先组装出一个list或tuple
#所以，我们把函数的参数改为可变参数：
r'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1,2,3)
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？
nums = [1, 2, 3]
calc(*nums)
'''

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
r'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
'''
#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
#仍以person()函数为例，我们希望检查是否有city和job参数：
r'''
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
'''
#但是调用者仍可以传入不受限制的关键字参数：
r'''
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
'''
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
r'''
def person(name, age, *, city, job):
    print(name, age, city, job)
'''
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
r'''
person('Jack', 24, city='Beijing', job='Engineer')
#Jack 24 Beijing Engineer
'''

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，
#除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
r'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
'''
#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
r'''
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
'''
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


#递归表达式
r'''
def fact(n):
    if n == 1:
        return 1
    return n*n-1
print(fact(99))
'''
#递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
#每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
#所以，递归调用的次数过多，会导致栈溢出。
#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

#上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。
#要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
r'''
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
'''
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


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

#迭代器
#我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#可以使用isinstance()判断一个对象是否是Iterable对象：
from collections import Iterable
print(isinstance([], Iterable),isinstance(mList,Iterable),isinstance(mStr,Iterable),isinstance(mInt,Iterable))
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator),isinstance(mList,Iterator),isinstance(mStr,Iterator),isinstance(mInt,Iterator))
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))
#这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
#直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
#只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


#函数式编程
'''
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''

#高阶函数
#变量可以指向函数
abs(-1) #1
abs     #<built-in function abs>
#可见，abs(-10)是函数调用，而abs是函数本身。

#要获得函数调用结果，我们可以把结果赋值给变量：
'''
f = abs
f(-1) #1
# 函数名也是变量
abs = 10
print(abs(-10))
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not callable
'''
##注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

#传人函数，把函数当做变量传人函数中
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))

#map/reduce
#Python内建了map()和reduce()函数。
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
	return x * x
r = map(f, [1,2,3])
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，
#因此通过list()函数让它把整个序列都计算出来并返回一个list。

#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
#reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#把序列[1, 3, 5, 7, 9]变换成整数13579
from functools import reduce
def fn(x, y):
	return x*10 + y
print(reduce(fn,[1, 3, 5, 7, 9]))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
#还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


##filter
#Python内建的filter()函数用于过滤序列。
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_old(x):
	return x % 2 == 1
list(filter(is_old, [0,1,2,3,4]))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，
#需要用list()函数获得所有结果并返回list。

#sorted
#排序算法
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
#如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
#因此，比较的过程必须通过函数抽象出来。
sorted(['bob', 'about', 'Zoo', 'Credit'])
#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f1 = lazy_sum(1, 3, 5, 7, 9)
#print(f1) <function lazy_sum.<locals>.sum at 0x101c6ed90>
#调用函数f1时，才真正计算求和的结果：
f1()
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1()==f2())
print(f1==f2)
#f1()和f2()的调用结果互不影响。
#闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
#所以，闭包用起来简单，实现起来可不容易。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，
#因此最终结果为9。

#返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
#已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())
#缺点是代码较长，可利用lambda函数缩短代码。


#匿名函数
#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
#在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x*x时，除了定义一个f(x)的函数外，还可以直接传入匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。

#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，
#也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))
#同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y


#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2016-01-26')
f = now
f()
#函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__,f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下
def log(func):
	def wapper(*args, **kw):
		print('call function %s()' %func.__name__)
		return func(*args, **kw)
	return wapper
#观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，
#把decorator置于函数的定义处：
@log
def now():
	print('2016-01-26')
now()
#把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
#于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，
#首先打印日志，再紧接着调用原始函数。

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#这个3层嵌套的decorator用法如下：
@log('execute')
def now():
    print('2015-3-25')
now()
print(now.__name__)
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：
now = log('execute')(now)
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
#否则，有些依赖函数签名的代码执行就会出错。

#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
#所以，一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()
print(now.__name__,'sssssss')
#只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。有先后顺序之分，装饰器比赛位于函数之前才能起作用

#偏函数
#Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
#要注意，这里的偏函数和数学意义上的偏函数不一样。

#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print( int('12345'))
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345', base=8))
def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
#调用这个新函数会更简单。

#注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(int2('1000000', base=10))
#
max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
#相当于：

args = (10, 5, 6, 7)
print(max(*args))
#结果为10。

#模块
#在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。

#为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
#很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。

#一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。

#请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
#否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，
#因为__init__.py本身就是一个模块，而它的模块名就是mycompany

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'pyl'

import sys

def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
#最常见的就是运行测试。

#作用域
'''
正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
'''
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
'''
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，
调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''

#安装第三方库
#，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
#比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#pip install Pillow                #
from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)
#PNG (400, 300) RGB
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
#pip install mysql-connector-python
#Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中

sys.path












