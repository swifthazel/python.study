# 图形化程序设计
'''import turtle
turtle.showturtle()
turtle.write("石洪菱")
'''
import matplotlib.pyplot as plt

'''t=turtle.Pen()
for x in range(360):
     t.forward(x)
     t.left(59)


'''
import matplotlib.pyplot as plt
plt.plot([1,4],[2,8])  #直线
x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,linewidth=5)
plt.xlabel('x轴')
plt.ylabel('y')#
plt.rcParams['font.san-serf']=['simhel'] #
plt.show()
'''
‘’‘
import matplotlib.pyplot as plt
import numpy as np
x=range(-100,100)  #取两百个点
y=[i**2 for i in x]   #遍历的结果是列表
plt.plot(x,y)
plt.show()
plt.savefig('一元二次方程.jpg')  #保存图片
'''

'''
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100) #等差数列
#sin_y=np.sin(x)
plt.subplot(2,2,1)#两列两行的一号画布故只有四块可选择
plt.plot(x,np.sin(x))
plt.xlim(-1, 5)     #选择x的坐标范围
#cos_y=np.cos(x)
plt.subplot(2,2,4)#四号画布
plt.plot(x,np.cos(x))
plt.scatter(x,np.sin(x))#绘制散点图用scatter
plt.xlim(-1,5)
#tan_y=np.tan(x)

#plt.plot(x,sin_y)
#plt.plot(x,cos_y)
#plt.plot(x,tan_y)
plt.show()
plt.savefig('三角函数')

'''
'''
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
size = np.random.rand(100)*1000  # 生成十种大小
color = np.random.rand(100) #颜色和点数要相同
plt.scatter(x, y, c=color,s=size,alpha=0.7)

plt.savefig('散点图')  #注意一定得是先保存后展示，不然展示个大白纸
plt.show()
'''

'''
#绘制不同颜色不同样式的线条
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,100,20)
plt.plot(x,x+10,':c',label=':r')
plt.plot(x,x+20,'_m',label='^b')
plt.plot(x,x+1,'*k',label='-g')
plt.legend(loc='lower right',fancybox=True,framealpha=0.5,shadow=False,borderpad=0.5)
#添加图例legend，参数补充回前面label
plt.show()
#-实线  --短横线  -.点划线  :虚线  .像素  o圆圈  v倒三角  ^正三角
# 1下箭头  2上箭头  3左  4右  s正方形  p五边形  *星形  H或h 六边形
#+  x  D菱形  d窄菱形  _水平线
#b  g  r  c薄荷蓝  m紫色  y  k黑色  w白色
'''
'''
#解决乱码问题
#绘制柱状图 bar
import matplotlib.pyplot as plt
import numpy as np
x=[1980,1985,1990,1995]
x_labels=[1980,1985,1990,1995]
y=[1000,200,3000,4000]
y_labels=['1000元',200,3000,4000]
plt.bar(x,y,width=3)
plt.xticks(x,x_labels)#只在轴上显示对的量
plt.yticks(y,y_labels)
plt.xlabel('年份')
plt.ylabel('销量')
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(1) #指定数字如0可固定后续输出那套随机数
#x=np.random.rand(10) #输出任意随机数
y=np.random.randint(-5,5,5) #输出范围内的五个随机数
x=np.arange(5)

plt.subplot(1,2,1)
plt.bar(x,y)
plt.axhline(0,color='red',linewidth=1)#在0位置添加水平线条

plt.subplot(1,2,2)
vbar=plt.barh(x,y,color='red',linewidth=0.5) #垂直方向建立坐标系
#对y小于0的部分设置蓝色，大于0的部分设置为红色 
for bar,height in zip(vbar,y):   #一定是bar，xxx的格式
    if height <0:
        bar.set(color='blue')  #

plt.axvline(0,color='yellow',linewidth=0.5)#添加垂直线条
plt.show()
print(x,y)
'''


'''
#柱状图
import matplotlib.pyplot as plt
import numpy as np
name=['爱丽丝1','玩具总动员','爱死机']
ticket1=[100,200,500] #指的是玩具总动员三天的票房
ticket2=[104,58,78]
ticket3=[52,75,89]
x=np.arange(len(name))
#绘制柱状图
plt.bar(x,ticket1,width=0.3,label='爱丽丝1')
plt.bar([i+0.3 for i in x],ticket2,width=0.3,alpha=0.8,label='玩具总动员')
plt.bar([i+0.6 for i in x],ticket1,width=0.3,alpha=0.5,label='爱死机')
#设置x的坐标
#x_label=['第{}天',format(i+1) for i in x]
#print(x_label)
#plt.xticks(x+0.3,x_label)
#设置y的
plt.ylabel('票房数')
#设置标题
plt.title('中国票房')
#添加图例
plt.legend()
#避免乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()
'''

'''
#绘制饼状图
import matplotlib.pyplot as plt
import numpy as np
man=74448
wonman=54687
man_per=man/(man+wonman)
wonman_per=wonman/(man+wonman)
#用列表储存
label=['男生','女生']
#改颜色
color=['blue','yellow']
#使用pie绘制饼状图，关键词为labels
#explode分裂  autopct显示百分比
paches,texts,autotexts=plt.pie([man_per,wonman_per],labels=label,colors=color,explode=(0,0.05),autopct='%0.lf%%')
#设置饼状图中的字体颜色,autotexts指的是百分比
for text in texts:
    text.set_color('green')
for text in autotexts:
    text.set_color('purple')
#设置字体大小,用fontsize
for text in texts+autotexts:
    text.set_fontsize(20)
#避免乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

'''
'''
#绘制直方图
#使用randn函数生成1000个正太分布的随机数，使用hist函数绘制这1000个随机数的分布状态
import matplotlib.pyplot as plt
import numpy as np
#x=np.random.randn(100)#生成标准的正太
x=np.random.normal(-2,2,1000)
y=np.random.normal(0,1,1000)#指定均值和方差的正态分布
z=np.random.normal(-1,2,1000)
#一个字典的参数，关键字参数
kw=dict(bins=100,alpha=0.2)
#hist函数绘制
plt.hist(y,**kw)
plt.hist(x,**kw)
#plt.hist(x,bins=100)#使用bins修改宽度
plt.hist(z,**kw)
plt.show()
'''

'''
#绘制等高线图
import matplotlib.pyplot as plt
import numpy as np
#创建xy
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
#计算交点
X,Y=np.meshgrid(x,y)
#计算Z
Z=np.sqrt(X**2+Y**2)
#plt.contour(X,Y,Z)
plt.contourf(X,Y,Z) #填充版
plt.show()
'''

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #导入3d包
#创建xyz
x=[1,2,3,9]
y=[1,4,5,6]
z=[4,6,5,7]
fig=plt.figure()
#创建Axe3D对象后放入figuer画布内
p=Axes3D(fig)
p.plot_trisurf(x,y,z)
plt.show()