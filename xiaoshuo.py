'''
Created on 2016年6月21日

@author: Administrator
'''
import urllib
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import re
from re import subn
from time import sleep
from datetime import datetime

class SpiderMain():
    def __init__(self):
        self.url = ''
        
    def craw(self,root_url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = request.Request(root_url,headers=headers)
        try:
            response = request.urlopen(req)
        except error.HTTPError as e:  
            print(e)
        except error.URLError as e:  
            print(e)
        except error.ContentTooShortError as e:  
            print(e)
        finally:
            return
        if response.getcode() != 200:
            print('code not success')
            return None
        context = response.read().decode('utf-8')
        print(context)
        soup = BeautifulSoup(context, 'html.parser', from_encoding='utf-8')
        title = soup.find('title').get_text()
        if title == '提示_若初文学网_若初阅读网':
            return
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'<h1 id="chapter_title')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = pattern.match(context)
        if match:
            print(match.group())
        with open(title+'.html', 'w', encoding='UTF-8') as fout:
            fout.write(context)
            fout.close()
    
    
    def setUrl(self, url):
        self.url = url
    def gerUrl(self):
        ma = re.split(r'http://www.ruochu.com/book/49479/', self.url)
        e_url = ma[1]
        if int(e_url) < 9999999:
            e_url = int(e_url)+1
            self.url = r'http://www.ruochu.com/book/49479/'+str(e_url)
            return self.url
        return None
            
            
if __name__ == '__main__':
    root_url = 'http://www.ruochu.com/book/49479/1154218'
    obj_spider = SpiderMain()
    obj_spider.setUrl(root_url)
    root_url = obj_spider.gerUrl()
    while obj_spider.gerUrl():
        print(root_url)
        obj_spider.setUrl(root_url)
        obj_spider.craw(root_url)
        root_url = obj_spider.gerUrl()