# -*- coding: utf-8 -*-
from hanziYanzhengma import ImageChar 
ic = ImageChar(fontColor=(100,211, 90))
ic.randChinese(4)
ic.save("1.jpeg")