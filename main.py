import numpy as np

#challenge1
a=np.array([11,15,40,43,48])
print(np.mean(a))
print(np.median(a))
print(np.std(a))

#challenge2
a=np.array([11,15,40,43,48])
b=np.mean(a)
c=np.std(a)
print(b)
print(c)
tab_normalise=(a-b)/c
print(f'le tableau normalise est: {tab_normalise}')

#challenge3
a=np.array([11,15,40,43,48])
d=np.array([11,15,40,43,41])
y=np.where(a != d)[0]
print(y)
print(a[y])
print(d[y])
for i in y :
     print(f"A[{i}]={a[i]}/D[{i}]={d[i]}")

#challenge4
A= np.array([[1,2,3],[4,5,6],[7,8,9]])
B= np.array([[3,1,2],[6,4,5],[8,7,9]])
print(np.dot(A,B))
print(np.transpose(A))
print(np.linalg.inv(B))

#challenge5
a=np.array([11,15,40,43,48])
z=np.where(a>20)
for i in z:
    print(a[i])











