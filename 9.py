Практическая работа № 9
import numpy as np

N = 3

A = [[1, 5, 1],[4, -1, 1],[15, 6, 44]]
print('Исходный массив A')
print(A)

B = [20, 11, 423]
print('Исходный массив B')
print(B)

Adiag = np.diag(A)
Alpha = A/Adiag
Alpha[np.diag_indices_from(Alpha)] = 0
Alpha = Alpha

print('===================')
print(Alpha)
print('===================')

Beta = B/Adiag
print(Beta)
print('===================')

x = np.zeros(N, dtype = float)
z = 100
KMAX = 100
k = 0

while (z>0.001) & (k<KMAX):
    z = 0
    for i in range(0,N):
        y=x[i]
        x[i]= Beta[i] - np.dot(Alpha[i],x)
        z=z+abs(x[i]-y)
    k+=1

print("k = ", k, "Погрешность = ", z)
print('')
print('X')

for i in range (0,N):
    print('%f'%x[i], end=' ')

print('')
