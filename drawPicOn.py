from PIL import Image,ImageDraw,ImageFont
import time
import numpy as np
import matplotlib.pyplot as plt
import os
sourceimg = "E:/workspace/python_ttf_to_pic/white.bmp"
savepath = "E:/workspace/python_ttf_to_pic/img/"

def imgaddnum(img,text,txtType):

	# 将img添加到画板 
	imgdraw = ImageDraw.Draw(img)
	# 设置需要绘制的字体 参数：字体名，字体大小
	imgfont = ImageFont.truetype(txtType,size=30)
	# 字体颜色
	fillcolor = "#dd1c5c"
	# 获取img的宽和高
	imgw,imgh = img.size
	# 开始将文字内容绘制到img的画板上 参数：坐标，绘制内容，填充颜色，字体
	imgdraw.text((imgw/4,imgh/4),text,fill=fillcolor,font=imgfont)
	# 设置img的保存路径和文件名
	txtTypeStr = str(txtType)
	tempName = text + '_' +os.path.basename(str(txtType))
	print('tempName = ',tempName)
	imgsavetarget = savepath + tempName + ".bmp"
	#旋转 
	img = img.rotate(45) 
	img=np.array(img.convert('L'))
	rows,cols=img.shape
	for i in range(rows):
		for j in range(cols):
			if (img[i,j]==0):
				img[i,j]=1
			else:
				img[i,j]=img[i,j]
	# 开始保存
	plt.figure("sample")
	plt.imshow(img,cmap='gray')
	plt.axis('off')
	plt.show()
	#res = img.save(imgsavetarget, "bmp")
	# 返回保存结果
	return res
class wordToPic:

	# 初始化一个img对象 为None
	targetimg = None
	# 判断需要打开的img对象路径是否存在
	def createManyWords(self,text,textType):
		if os.path.exists(sourceimg):
		    targetimg = Image.open(sourceimg)
		    rig = imgaddnum(targetimg,text,textType)
		    print(rig)
		else:
		    print("Image Not Found!")