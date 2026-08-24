<!-- markdownlint-disable MD024 MD060 -->

# Week 5: NumPy Quick Notes

NumPy is used for fast numerical work on homogeneous, multidimensional arrays.

```python
import numpy as np
```

## 1. Creating Arrays

| Tool | Use | Syntax |
|---|---|---|
| `np.array` | Convert a list/nested list | `np.array(data, dtype=...)` |
| `np.arange` | Values with a step | `np.arange(start, stop, step)` |
| `np.linspace` | Fixed number of equally spaced values | `np.linspace(start, stop, num)` |
| `np.zeros` | Array filled with zero | `np.zeros(shape, dtype=...)` |
| `np.ones` | Array filled with one | `np.ones(shape, dtype=...)` |
| `np.identity` | Square identity matrix | `np.identity(n)` |
| `np.random.random` | Random floats in `[0, 1)` | `np.random.random(shape)` |
| `np.random.randint` | Random integers | `np.random.randint(low, high, size)` |
| `np.random.normal` | Normal distribution values | `np.random.normal(loc, scale, size)` |
| `np.random.seed` | Repeat random results | `np.random.seed(number)` |

### Simple example

```python
a = np.array([1, 2, 3])
b = np.arange(1, 10, 2)       # [1 3 5 7 9]
c = np.zeros((2, 3), dtype=int)
d = np.ones((2, 2))
```

### Complex example

```python
np.random.seed(7)
scores = np.random.randint(40, 101, size=(4, 3))
students = np.arange(1, 5).reshape(4, 1)
report = np.hstack((students, scores))
print(report)
```

Important: NumPy arrays normally contain one compatible dtype. If one string is present, numbers may be converted to strings.

## 2. Attributes and Data Types

For an array `a`:

```python
a.ndim       # number of dimensions
a.shape      # length of each dimension
a.size       # total number of elements
a.dtype      # data type
a.itemsize   # bytes per element
a.astype(np.float32)  # converted copy
```

### Simple example

```python
a = np.arange(12).reshape(3, 4)
print(a.ndim)       # 2
print(a.shape)      # (3, 4)
print(a.size)       # 12
print(a.astype(np.float32).dtype)
```

### Complex example

```python
values = np.array([1.2, 3.8, 5.1])
integers = values.astype(np.int32)
print(integers)     # decimal part is removed
print(integers.itemsize)
```

## 3. Reshaping and Flattening

`reshape` changes the shape but keeps the values. The product of the new dimensions must equal `size`.

```python
a.reshape(rows, columns)
a.reshape(-1, columns)  # NumPy infers one dimension
a.ravel()             # flattened view when possible
a.flatten()           # flattened copy
a.T                   # transpose for 2D arrays
```

### Simple example

```python
a = np.arange(12)
matrix = a.reshape(3, 4)
print(matrix)
print(matrix.reshape(-1))
```

### Complex example

```python
images = np.arange(24).reshape(2, 3, 4)
batch_for_model = images.reshape(2, -1)  # two images, 12 features each
print(batch_for_model.shape)              # (2, 12)
```

## 4. Indexing, Slicing, and Fancy Indexing

Indexes start at zero. For a 2D array use `a[row, column]`.

```python
a[row, column]
a[row_start:row_stop:step, col_start:col_stop:step]
a[[row1, row2], [col1, col2]]       # paired positions
a[[row1, row2]][:, [col1, col2]]    # rows then columns
```

### Simple example

```python
a = np.arange(12).reshape(3, 4)
print(a[1, 2])       # one value
print(a[0, :])       # first row
print(a[:, 2])       # third column
print(a[1:, 1:3])    # selected block
```

### Complex example

```python
a = np.arange(20).reshape(4, 5)
selected = a[[0, 2, 3]][:, [1, 4]]
corners = a[::3, ::4]
print(selected)
print(corners)
```

## 5. Boolean Filtering and Conditional Replacement

Comparisons produce Boolean arrays. Use `&` for AND, `|` for OR, and parentheses around each condition.

```python
a[a > 50]
a[(a >= 10) & (a <= 20)]
np.where(condition)             # indexes where true
np.where(condition, yes, no)    # choose values element by element
np.isin(a, allowed_values)
```

### Simple example

```python
a = np.array([10, 25, 60, 80])
print(a[a > 50])
print(np.where(a > 50, 0, a))
```

### Complex example

```python
marks = np.array([35, 48, 72, 91, 66])
status = np.where(marks >= 50, "pass", "fail")
status = np.where(marks >= 85, "distinction", status)
print(status)
print(np.isin(marks, [48, 66]))
```

## 6. Arithmetic, Broadcasting, and Matrix Operations

Arithmetic on arrays is element by element. Broadcasting allows compatible shapes to work together.

```python
a + 10
a * 2
a ** 2
a + b
a @ b                  # matrix multiplication
np.dot(a, b)             # dot product / matrix multiplication
```

### Simple example

```python
a = np.array([1, 2, 3])
print(a * 10)
print(a + 5)
```

### Complex example

```python
prices = np.array([[100, 200], [150, 250]])
tax_rates = np.array([0.05, 0.10])
final_prices = prices * (1 + tax_rates)  # rate broadcasts across rows
print(final_prices)

left = np.arange(6).reshape(2, 3)
right = np.arange(6).reshape(3, 2)
print(left @ right)
```

## 7. Aggregations and Statistics

`axis=0` reduces down rows and returns one result per column. `axis=1` reduces across columns and returns one result per row.

```python
a.sum(); a.mean(); a.min(); a.max(); a.prod()
a.std(); a.var(); np.median(a)
np.percentile(a, 50)
np.argmax(a); np.argmin(a)
np.cumsum(a); np.cumprod(a)
np.count_nonzero(a)
```

### Simple example

```python
a = np.array([[10, 20], [30, 40]])
print(a.sum())          # all values
print(a.sum(axis=0))   # each column
print(a.mean(axis=1))  # each row
print(np.argmax(a))
```

### Complex example

```python
scores = np.array([[70, 80, 90], [60, 75, 85], [95, 88, 92]])
student_average = scores.mean(axis=1)
subject_average = scores.mean(axis=0)
top_student = np.argmax(student_average)
print(student_average, subject_average, top_student)
```

## 8. Sorting, Unique Values, and Searching

```python
np.sort(a)                    # sorted copy
np.sort(a, axis=0)            # sort each column
np.sort(a)[::-1]              # descending 1D sort
np.unique(a)
np.unique(a, return_counts=True)
np.where(a == value)
```

### Simple example

```python
a = np.array([4, 2, 4, 1, 2])
print(np.sort(a))
print(np.unique(a, return_counts=True))
```

### Complex example

```python
table = np.array([[90, 40], [70, 80], [95, 60]])
order = np.argsort(table[:, 0])[::-1]
print(table[order])
```

## 9. Array Manipulation Helpers

```python
np.append(a, values, axis=...)
np.concatenate((a, b), axis=...)
np.expand_dims(a, axis=0)
np.squeeze(a)
np.swapaxes(a, axis1, axis2)
np.transpose(a)
np.flip(a, axis=...)
np.repeat(a, repeats)
np.tile(a, repetitions)
np.clip(a, minimum, maximum)
```

### Simple example

```python
a = np.array([1, 2, 3])
print(np.expand_dims(a, axis=0).shape)  # (1, 3)
print(np.flip(a))
print(np.clip(np.array([-2, 5, 12]), 0, 10))
```

### Complex example

```python
cube = np.arange(24).reshape(2, 3, 4)
swapped = np.swapaxes(cube, 0, 2)
flipped = np.flip(swapped, axis=1)
print(cube.shape, swapped.shape, flipped.shape)
```

`swapaxes` changes axis order; `reshape` changes the shape while reading values in order. They are not the same operation.

## 10. Random Sampling

```python
np.random.seed(0)
np.random.shuffle(a)                       # modifies a in place
np.random.choice(a, size=3, replace=False)
np.random.uniform(low, high, size)
```

### Simple example

```python
np.random.seed(1)
print(np.random.choice([10, 20, 30, 40], 2, replace=False))
```

### Complex example

```python
np.random.seed(10)
sample = np.random.normal(loc=50, scale=8, size=1000)
print(sample.mean(), sample.std())
```

## 11. Correlation and Histograms

```python
np.corrcoef(x, y)                 # Pearson correlation matrix
counts, edges = np.histogram(a, bins=[0, 50, 100])
```

### Simple example

```python
hours = np.array([1, 2, 3, 4])
marks = np.array([40, 50, 70, 85])
print(np.corrcoef(hours, marks))
```

### Complex example

```python
data = np.array([12, 18, 25, 42, 55, 63, 80])
counts, edges = np.histogram(data, bins=[0, 25, 50, 75, 100])
print("frequency:", counts)
print("bin edges:", edges)
```

## 12. Structured Arrays and Saving Arrays

Structured arrays allow named fields with different types.

```python
dtype = np.dtype([("name", "U20"), ("iq", np.int32), ("cgpa", np.float64)])
students = np.array([("A", 100, 8.2)], dtype=dtype)
students["iq"]
np.save("students.npy", students)
loaded = np.load("students.npy")
```

### Simple example

```python
dt = np.dtype([("name", "U10"), ("score", np.int32)])
data = np.array([("Anish", 90), ("Riya", 85)], dtype=dt)
print(data["score"])
```

### Complex example

```python
dt = np.dtype([
    ("name", "U20"), ("iq", np.int32),
    ("cgpa", np.float64), ("placed", "U5")
])
students = np.array([
    ("Anish", 100, 8.1, "Yes"),
    ("Riya", 115, 9.0, "Yes"),
    ("Kabir", 90, 7.2, "No")
], dtype=dt)
print(students[students["cgpa"] >= 8.5])
```

## Fast Revision: Common Traps

- `stop` is excluded in `np.arange`, but included in `np.linspace` by default.
- `axis=0` gives column-wise results; `axis=1` gives row-wise results.
- `*` is element-wise multiplication; `@` is matrix multiplication.
- Use `&` and `|` for array conditions, not Python `and` and `or`.
- Check `shape` before combining arrays or multiplying matrices.
- `np.append` returns a new array; reassign it if you need to keep the change.
- Mixed values may force an array to string dtype, preventing numerical operations.
