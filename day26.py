
import numpy as np

# 1. Creating Arrays
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Zeros:", np.zeros(5))
print("Ones:\n", np.ones((2, 3)))
print("Arange:", np.arange(0, 10, 2))
print("Linspace:", np.linspace(0, 1, 5))


# 2. Array Properties
print("\n--- Array Properties ---")

for name, arr in [("a", a), ("b", b), ("c", c)]:
    print(name, "shape:", arr.shape)
    print(name, "ndim:", arr.ndim)
    print(name, "size:", arr.size)
    print(name, "dtype:", arr.dtype)


# 3. Indexing, Subsetting and Slicing
print("\n--- Indexing and Slicing ---")

a = np.array([10, 20, 30, 40, 50])

print(a[0])
print(a[-1])
print(a[[1, 2, 3]])
print(a[1:4])

# For 2D arrays
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(b[0, 1])
print(b[[0, 1], [1, 2]])
print(b[[0, 1], [0, 0]])
print(b[[0], [0, 2]])
print(b[:, 1])
print(b[1, :])
print(b[0:2, 1:3])


# 4. Array Calculations
print("\n--- Array Calculations ---")

a = np.array([1, 2, 3])

print(a + 10)
print(a * 2)
print(a ** 2)
print(a + a)

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Min:", np.min(a))
print("Max:", np.max(a))
print("Standard Deviation:", np.std(a))


# 5. Boolean Filtering
print("\n--- Boolean Filtering ---")

a = np.array([10, 20, 30, 40, 50])

print(a > 25)
print(a[a > 25])

b = (a > 15) & (a < 45)
print(a[b])


# 6. Reshaping
print("\n--- Reshaping ---")

a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(2, 3)

print("Original Array:", a)
print("Reshaped Array:\n", b)
print("Flatten:", b.flatten())

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Transpose:\n", b.T)


# 7. Matrix Operations
print("\n--- Matrix Operations ---")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Element-wise Multiplication:\n", A * B)
print("Matrix Multiplication:\n", A @ B)
print("Dot Product:\n", np.dot(A, B))
print("Determinant:", np.linalg.det(A))
print("Inverse:\n", np.linalg.inv(A))


# 8. Random Numbers
print("\n--- Random Numbers ---")

np.random.seed(1)

print("Random Numbers:", np.random.rand(3))
print("Random Integers:", np.random.randint(1, 10, 5))
print("2D Random Array:\n", np.random.rand(2, 4))


# 9. Broadcasting
print("\n--- Broadcasting ---")

a = np.array([1, 2, 3])

print(a * 10)

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A + np.array([10, 20, 30]))
