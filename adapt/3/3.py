import numpy as np
import math
import matplotlib.pyplot as plt


fs = 10000 # サンプリング周波数
fc = 2000  # カットオフ周波数
N=10000       # 入力点数


# 変数
T = 1.0 / fs
omega_d = 2.0*math.pi * fc
omega_a = 2.0/T * math.tan(omega_d*T / 2.0)
alpha = math.tan(omega_d*T / 2.0)
a1 = (alpha-1) / (alpha+1)
b0 = b1 = alpha / (alpha+1)

print('fs      = {}'.format(fs))
print('fc      = {}'.format(fc))
print('Omega_a = {}'.format(omega_a))
print('alpha   = {}'.format(alpha))
print('a1      = {}'.format(a1))
print('b0      = {}'.format(a1))


# インパルス入力
input = np.zeros(N)
input[0] = 1

# ローパスフィルタ
x1 = y1 = 0.0
output = np.array([])
for j in range(N):
	y0 = b0*input[j] + b1*x1 - a1*y1
	x1 = input[j]
	y1 = y0
	output = np.append(output, y0)


# グラフ
plt.plot(np.arange(0,N), output)
plt.xlim(0, 100)
plt.xlabel('Times[s](X1/10000)')
plt.ylabel('Amplitude')
plt.show()

amp = 20*np.log10(np.abs(np.fft.fft(output, N)))

plt.plot(np.arange(0,N), amp)
plt.xlim(0,N/2)
plt.ylim(-50,0)
plt.xlabel('Frequency[Hz]')
plt.ylabel('Amplitude spectrum[dB]')
plt.show()
