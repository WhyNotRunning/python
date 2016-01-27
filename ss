[33mcommit 1347e1f246f4cdf523573e0b13e5742b94ffc0e0[m
Author: running <799038015@qq.com>
Date:   Tue Jan 26 20:05:57 2016 +0800

    add jpg

[1mdiff --git a/hello.py b/hello.py[m
[1mindex 5753bdb..a407bcb 100644[m
[1m--- a/hello.py[m
[1m+++ b/hello.py[m
[36m@@ -1020,7 +1020,7 @@[m [mdef greeting(name):[m
 #比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：[m
 #pip install Pillow                #[m
 from PIL import Image[m
[31m-im = Image.open('test.png')[m
[32m+[m[32mim = Image.open('test.jpg')[m
 print(im.format, im.size, im.mode)[m
 #PNG (400, 300) RGB[m
 im.thumbnail((200, 100))[m
[1mdiff --git a/test.jpg b/test.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..15cd09f[m
Binary files /dev/null and b/test.jpg differ
[1mdiff --git a/thumb.jpg b/thumb.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..8e865c4[m
Binary files /dev/null and b/thumb.jpg differ
