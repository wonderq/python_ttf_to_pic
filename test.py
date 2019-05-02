import sys  
print('目前系统的编码为：',sys.getdefaultencoding())  
name='小明'  
print(type(name))#首先我们来打印下转码前的name类型，因为它是str，所以可以通过encode来进行编码  
name1=name.encode('utf-8')  
print(name1)  


name2=name1.decode('utf-8')  
print(type(name2))  
print(name2)