import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(max, comp):
    re, im = comp[0], comp[1]
    #実部がre、虚部がimの複素数を作成
    c = complex(re, im)

    #Z_nの初項は0
    z = complex(0, 0)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            return i
    
    return max     #無限大に発散しない場合にはmaxを返す

re = np.linspace(-2, 2, 2000)
im = np.linspace(2, -2, 2000)

#実部と虚部の組み合わせを作成
Re, Im = np.meshgrid(re, im)
comp = np.c_[Re.ravel(), Im.ravel()]

Mandelbrot = np.zeros(len(comp))

#マンデルブロ集合に属するかの計算
for i, c_point in enumerate(comp):
    Mandelbrot[i] = mandelbrot(100, c_point)

Mandelbrot = Mandelbrot.reshape((2000, 2000))

fig = plt.figure(dpi=600)
plt.axis("off")
plt.imshow(Mandelbrot, cmap="hot", extent=[-2, 2, -2, 2])
fig.set_size_inches(3, 3)        #出力される画像の大きさを調整
plt.show()

#画像を保存
fig.savefig("mandelbrot.png")