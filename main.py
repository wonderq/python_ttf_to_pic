#-*-coding:utf-8-*-
#from ttfToPic import Win32Font
from drawPicOn import wordToPic


#f = Win32Font("C:/Windows/Fonts/simsun.ttc", 15)
#im = f.renderText(u"宋")
#im.save("E:/workspace/python_ttf_to_pic/hope1.png")

#变量参数
text = "防"
textType = "C:/Windows/Fonts/simsun.ttc"

#调用下面的方法
w = wordToPic()
w.createManyWords(text,textType)
