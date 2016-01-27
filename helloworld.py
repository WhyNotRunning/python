#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hello 

# 常用内建模块

# datetime
from datetime import datetime
import os
print(datetime.now())
#datetime类型转换为timestamp
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
st = dt.timestamp()
print(st)
#timestamp转换为datetime
temp = datetime.fromtimestamp(st) # 本地时间
ucttemp = datetime.utcfromtimestamp(st) # UTC时间
print(temp,ucttemp)
# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
# datetime转换为str
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import datetime, timedelta
now = now + timedelta(days=2, hours=12)
print(now)
# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，
# 所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区
from datetime import datetime, timedelta, timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)# 拿到UTC时间，并强制设置时区为UTC+0:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))# astimezone()将转换时区为北京时间


# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类。
# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x, p.y)
# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
d = deque(['1',2,'3'])
d.append('4')
print(d)
d.pop()
print(d)
d.appendleft('0')
print(d)
d.popleft()
print(d)
# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
d = defaultdict(lambda:'N/A')
d['key'] = 'val'
print(d['key'])
print(d['key2'])
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

# 如果要保持Key的顺序，可以用OrderedDict,OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
od = OrderedDict()
od['y'] = 'y'
od['x'] = 'x'
od['z'] = 'z'
print(od)
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
# Counter

# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for x in 'abcdefabc':
	c[x] = c[x] + 1
print(c)


# base64
# ase64是一种用64个字符来表示任意二进制数据的方法。

# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，
# 所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
# Base64是一种最常见的二进制编码方法。
# Base64的原理很简单，首先，准备一个包含64个字符的数组：

# ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
# 这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。
# 所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，
# 好处是编码后的文本数据可以在邮件正文、网页等直接显示。

# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
import base64
print(base64.b64encode(b'A'))
print(base64.b64decode(b'cmluZw=='))
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

# struct
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

# struct的pack函数把任意数据类型变成bytes
import struct
b = struct.pack('>I', 10240099)
print(b)
# pack的第一个参数是处理指令，'>I'的意思是：

# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# unpack把bytes变成相应的数据类型：
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。

# 首先找一个bmp文件，没有的话用“画图”画一个。

# 读入前30个字节来分析：

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：

# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# 所以，组合起来用unpack读取：

print(struct.unpack('<ccIIIIIIHH', s))
# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
# 结果显示，b'B'、b'M'说明是Windows位图，位图大小为640x360，颜色数为24。

# hashlib
# 摘要算法简介

# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，
# 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
import hashlib
md5 = hashlib.md5()
md5.update('how to used md5 in python hashlib'.encode('utf-8'))
md5.update('how to used md5 in python hashlib too'.encode('utf-8'))#more time
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
# itertools提供的几个“无限”迭代器：

import itertools
natuals = itertools.count(1)

r'''
for x in natuals:
	print(x)
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
	print(c)
ns = itertools.repeat('A', 3)
for n in ns:
	print(n)
'''
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

# itertools提供的几个迭代器操作函数chain(),groupby()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
	print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
	print(key, list(group))
# 迭代效果
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']

# XML
# DOM vs SAX

# 操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，
# 优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

# 正常情况下，优先考虑SAX，因为DOM实在太占内存。

# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，
# 准备好这3个函数，然后就可以解析xml了。
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
	"""docstring for DefaultSaxHandler"""
	def __init__(self):
		super(DefaultSaxHandler, self).__init__()
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
	def end_element(self, name):
		print('sax:end_element: %s' % name)
	def char_data(self, text):
		print('sax:char_data: %s' %text)
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，
#所以需要自己保存起来，在EndElementHandler里面再合并。

# 除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，
#因此，最简单也是最有效的生成XML的方法是拼接字符串：
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(encode('some & data'))
# L.append(r'</root>')
#return ''.join(L)

# HTMLParser
# 果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，
# 第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。

# 假设第一步已经完成了，第二步应该如何解析HTML呢？

# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。

# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
 	"""docstring for MyHTMLParser"""
 	def __init__(self):
 		super(MyHTMLParser, self).__init__()
 	def handle_starttag(self, tag, attrs):
 		print('<%s>' % tag)
 	def handle_endtag(self, tag):
 		print('</%s>' % tag)
 	def handle_startendtag(self, tag, attrs):
 		print('</%s>' % tag)
 	def handle_data(self, data):
 		print(data)
 	def handle_comment(self, data):
 		print('<!--', data, '-->')
 	def handle_entityref(self, name):
 		print('&%s;' % name)
 	def handle_charref(self, name):
 		print('&#%s;' % name)
parser = MyHTMLParser()
parser.feed('''
<html>
<head></head>
<body>
<!-- test html parser -->
<p>Some <a href=\"#\">html</a>HTMLtutorial<br>END</p>
</body>
</html>
''')
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。

# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。

# urllib
# urllib提供了一系列用于操作URL的功能。
# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
	data = f.read();
	print('Status:',f.status, f.reason)
	for k, v in f.getheaders():
		print('%s : %s' % (k, v))
	print('Data: ',data.decode('utf-8'))

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
# 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页
from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
	print('Status:', f.status, f.reason)
	for k, v in f.getheaders():
		print('%s: %s' % (k, v))
	print('Data:', f.read().decode('utf-8'))

# Post

# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

# 我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
from urllib import request, parse
r'''
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''
# Handler

# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
# proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = request.build_opener(proxy_handler, proxy_auth_handler)
# with opener.open('http://www.example.com/login.html') as f:
#     pass



# PIL
# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
# 操作图像

# 来看看最常见的图像缩放操作，只需三四行代码：

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')
# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

# 比如，模糊效果也只需几行代码：

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# virtualenv
# 在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。
# 所有第三方的包都会被pip安装到Python3的site-packages目录下。
# 首先，我们用pip安装virtualenv：

# $ pip3 install virtualenv
# 然后，假定我们要开发一个新的项目，需要一套独立的Python运行环境，可以这么做：

# 第一步，创建目录：

# Mac:~ michael$ mkdir myproject
# Mac:~ michael$ cd myproject/
# Mac:myproject michael$
# 第二步，创建一个独立的Python运行环境，命名为venv：

# Mac:myproject michael$ virtualenv --no-site-packages venv
# Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
# New python executable in venv/bin/python3.4
# Also creating executable in venv/bin/python
# Installing setuptools, pip, wheel...done.
# 命令virtualenv就可以创建一个独立的Python运行环境，我们还加上了参数--no-site-packages，这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何第三方包的“干净”的Python运行环境。

# 新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：

# Mac:myproject michael$ source venv/bin/activate
# (venv)Mac:myproject michael$
# 注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境。

# 下面正常安装各种第三方包，并运行python命令：

# (venv)Mac:myproject michael$ pip install jinja2
# ...
# Successfully installed jinja2-2.7.3 markupsafe-0.23
# (venv)Mac:myproject michael$ python myapp.py
# ...
# 在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。也就是说，venv环境是专门针对myproject这个应用创建的。

# 退出当前的venv环境，使用deactivate命令：

# (venv)Mac:myproject michael$ deactivate 
# Mac:myproject michael$
# 此时就回到了正常的环境，现在pip或python均是在系统Python环境下执行。

# 完全可以针对每个应用创建独立的Python运行环境，这样就可以对每个应用的Python环境进行隔离。

# virtualenv是如何创建“独立”的Python运行环境的呢？原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。


# 图形界面
# Python支持多种图形界面的第三方库，包括：
# Tk
# wxWidgets
# Qt
# GTK
# Tkinter
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()


















