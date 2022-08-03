import random

import numpy as np
import matplotlib.pyplot as plt

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# Create a new subplot from a grid of 1x1
plt.subplot(221)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Set x limits
plt.xlim(-4.0, 4.0)

# Set x ticks
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Set y limits
plt.ylim(-1.0, 1.0)

# Set y ticks
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

# 让画面没那么逼仄
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# 使坐标轴出现我们想要的数字，并置于一个列表里,使用latex作为记号标签
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1])
# 加个坐标系，并且此坐标已在第一画布内
ax = plt.gca()
# plt.gca().spines['right'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle="--")  # 搞出线
plt.scatter([t, ], [np.cos(t), ], 50, color='green')  # 搞出点

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 搞箭头和式子

plt.plot([t, t], [0, np.sin(t)], color='red', linewidth=1.5, linestyle="--")
plt.scatter([t, ], [np.sin(t), ], 50, color='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 加粗各个点，使之更明显
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor=None, alpha=0.65))

#子图
plt.subplot(222)
'''plt.figure().add_subplot(222)
或fig=plt.figure() ax=fig.add_subplot(222)
表示新建一个画布，并放在分为四份的画布的第二块区域'''
plt.plot(X,X**2)
plt.legend(['ax legend'])
#ax.grid(color='r',linestyle='-',linewidth='1')第一画布
plt.grid(color='r',linestyle='-',linewidth='1')

#子图三
plt.subplot(223)
z=a(1,10,1)
plt.plot([1,1],[2,3])
ax=plt.gca()#绘制坐标轴
#ax.locator_params(nbins=5)

# Save figure using 72 dots per inch
plt.savefig('正余弦函数')

# Show result on screen
plt.show()
