import numpy as np

vec1 = np.ones((5))
print(vec1)
vec1.dtype

vec1 = np.ones((5),dtype=np.int8)
print(vec1)
vec1.dtype


vec1 = np.zeros((2,2,2),dtype=np.int64)
print(vec1)
vec1.dtype


vec1 = np.random.randn(25,25)
print(vec1)
vec1.dtype



np.random.seed(0)  # seed for reproducibility
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 3))  # Two-dimensional array

print(x1)
print(x2)

x1 = np.array([1,2,3,4])
print(x1)
print(type(x1))


x2 = np.array([[1,2,3],[4,5,6]])
print(x2)
print(type(x2))


x = np.ndarray(shape=3,dtype=int, buffer = np.array([1,2,3]))
print(x)
x = np.append(x,5)
print(x)
print(type(x))


x = np.ndarray(shape=(2,2), dtype=float,buffer = np.array([[1.4,2.5],[1.3,2.4]]))
print(x)


x = np.ndarray(shape=(2,2), dtype=int,buffer = np.array([[1,2],[1,2]]))
print(x)

x2 = np.array([[1,2,3],[4,5,6]])
print("x2.ndim = ",x2.ndim)
print("x2.shape = ",x2.shape)
print("x2.size = ",x2.size)


x1 = np.array([1,2,3,4])
print("x1 = ",x1)
print("x1[0] = ",x1[0]) # just like arrays in c/c++
print("x1[-1] = ",x1[-1]) # negative indexing just like lists


x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("x2 = "); print(x2)
print("x2[0] = ",x2[0]) # will print the entire 1st row

# to print 1st element of 1st row
print("x2[0][0]= ", x2[0][0])
print("x2[0,0] = ",x2[0,0])

# to print 2nd element of 3rd row
print("x2[2][1]= ", x2[2][1])
print("x2[2,1]= ", x2[2,1])


x2[0, 0] = 12
print(x2)


x2[0][0] = 14
print(x2)


x1 = np.ndarray(5, buffer = np.array([1,2,3,4,5]),dtype = int)
print(x1)
x1[2] = 5.7
print("x1 after changing : ",x1)


x = np.ndarray(10, buffer = np.array([0,1,2,3,4,5,6,7,8,9]),dtype = int)
print(x)
print("x[:] = ",x[:])
print("x[:5] = ",x[:5])
print("x[5:] = ",x[5:])
print("x[1:5] = ",x[1:5])
print("x[1:5:2] = ",x[1:5:2])
print("x[::-1] = ",x[::-1])


np.random.seed(0)  # seed for reproducibility
x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x2)
print("x2[:2, :3] = "); print(x2[:2, :3])  # first two rows, first three columns
print("x2[:3, ::2] = "); print(x2[:3, ::2]) # all rows, every other column
print("x2[::-1, ::-1] = "); print(x2[::-1, ::-1]) #reversed 2D array
print("x2[:, 0] = ",x2[:, 0])  # first column of x2


x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.concatenate([x,y]) # Combines x and y to give one array.
# a = np.concatenate([x,y,z])
print(z)
# print(a)

x2 = np.array([[1,2,3],[2,3,4]])
y2 = np.array([[3,4,5],[4,5,6]])
z2 = np.concatenate([x2,y2])
print(z2)



x2 = np.array([[1,2,3],[2,3,4]])
y2 = np.array([[3,4,5],[4,5,6]])
print("x2 + y2 = "); print(np.add(x2,y2))
print("x2 - y2 = "); print(np.subtract(x2,y2))



x2 = np.array([[1,2,3],[2,3,4]])
y2 = np.array([[3,4,5],[4,5,6]])
print(np.matmul(x2,y2))
# This gives an error. Why?



x2 = np.array([[0,1,2],[2,1,0]])
print(x2)


print(np.cov(x2))


x = np.array([-2.1, -1,  4.3])
y = np.array([3,  1.1,  0.12])
X = np.stack((x, y))
print(np.cov(X))
# To check
print(np.cov(x))
print(np.cov(y))


x = np.array([-2.1, -1,  4.3])
y = np.array([3,  1.1,  0.12])
X = np.stack((x, y))
print(np.corrcoef(X))
