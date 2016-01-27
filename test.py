import re
r = re.match(r'^\d{3}\-\d{3,8}$','123-1234')
if r:
    print('success...')
else:
    print('error...')

# 切分字符串
s = 'a  b  c'
print(s.split(' '),re.split(r'\s+', s))