# Week 5 Quick Revision - NumPy (Syntax + Simple/Complex Examples)

## 1) Core classes
- `np.ndarray` -> main NumPy array object
- `np.nditer` -> efficient iterator over arrays

---

## 2) Class: `np.ndarray`

### A) Create arrays

| Method/Function | Syntax | Simple example | Complex example |
|---|---|---|---|
| `np.array` | `np.array(obj, dtype=...)` | `a = np.array([1,2,3])` | `a = np.array([[1,2],[3,4]], dtype=np.float32)` |
| `np.arange` | `np.arange(start, stop, step)` | `a = np.arange(5)` | `a = np.arange(10, 0, -2)` |
| `np.linspace` | `np.linspace(start, stop, num)` | `a = np.linspace(0, 1, 5)` | `x = np.linspace(-2*np.pi, 2*np.pi, 1000)` |
| `np.zeros` | `np.zeros(shape)` | `a = np.zeros(3)` | `a = np.zeros((2,3,4), dtype=np.int32)` |
| `np.ones` | `np.ones(shape)` | `a = np.ones(4)` | `a = np.ones((3,3), dtype=np.float64)` |
| `np.empty` | `np.empty(shape)` | `a = np.empty(5)` | `a = np.empty((1000,1000), dtype=np.float32)` |
| `np.identity` / `np.eye` | `np.eye(n, M=None)` | `i = np.eye(3)` | `i = np.eye(3, 4)` |

### B) Attributes (no `()`)

| Attribute | Syntax | Use |
|---|---|---|
| shape | `a.shape` | dimensions |
| ndim | `a.ndim` | number of axes |
| size | `a.size` | total elements |
| dtype | `a.dtype` | data type |
| itemsize | `a.itemsize` | bytes per element |
| nbytes | `a.nbytes` | total memory bytes |

### C) Type conversion

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `astype` | `a.astype(new_dtype)` | `a.astype(int)` | `a = a.astype(np.float32)` |

### D) Reshape / transpose / flatten

| Method | Syntax | Simple example | Complex example |
|---|---|---|---|
| `reshape` | `a.reshape(new_shape)` | `a.reshape(2,3)` | `a.reshape(-1, 4)` |
| `transpose` / `.T` | `a.transpose(...)` | `a.T` | `a.transpose(1,0,2)` |
| `flatten` | `a.flatten()` | `a.flatten()` | `a.flatten(order='F')` |
| `expand_dims` | `np.expand_dims(a, axis)` | `np.expand_dims(a, 0)` | `np.expand_dims(img, axis=-1)` |

### E) Math / stats

| Method/Function | Syntax | Simple example | Complex example |
|---|---|---|---|
| `sum` | `a.sum(axis=None)` | `a.sum()` | `a.sum(axis=1)` |
| `mean` | `a.mean(axis=None)` | `a.mean()` | `a.mean(axis=0)` |
| `min` / `max` | `a.min()`, `a.max()` | `a.max()` | `a.max(axis=1)` |
| `prod` | `a.prod(axis=None)` | `a.prod()` | `a.prod(axis=0)` |
| `median` | `np.median(a, axis=None)` | `np.median(a)` | `np.median(a, axis=1)` |
| `var` / `std` | `a.var()`, `a.std()` | `a.std()` | `a.var(axis=1)` |
| `round` | `np.round(a, decimals)` | `np.round(a)` | `np.round(a, 3)` |
| trig/log/exp | `np.sin(a)`, `np.log(a)`, `np.exp(a)` | `np.exp(a)` | `y = np.sin(x) + np.log(x+1)` |
| `dot` | `np.dot(a, b)` | `np.dot([1,2],[3,4])` | `np.dot(A, B)` (matrix multiply) |

### F) Indexing / filtering

| Concept | Syntax | Simple | Complex |
|---|---|---|---|
| Slicing | `a[start:end:step]` | `a[1:4]` | `a[::2]` |
| 2D indexing | `a[row, col]` | `a[1,2]` | `a[:, [0,2]]` |
| Boolean mask | `a[mask]` | `a[a>5]` | `a[(a%2==0) & (a>10)]` |
| Fancy indexing | `a[[i1,i2,...]]` | `a[[0,2,4]]` | `a[[0,2], [1,3]]` |

### G) Stack / split / combine

| Function | Syntax | Simple | Complex |
|---|---|---|---|
| `hstack` | `np.hstack((a,b))` | `np.hstack((a,b))` | join feature blocks by columns |
| `vstack` | `np.vstack((a,b))` | `np.vstack((a,b))` | stack batches row-wise |
| `concatenate` | `np.concatenate((a,b), axis=...)` | `np.concatenate((a,b))` | `np.concatenate((a,b), axis=1)` |
| `split` | `np.split(a, sections)` | `np.split(a, 2)` | `np.split(a, [3,7])` |
| `hsplit` / `vsplit` | `np.hsplit(a,n)` | `np.hsplit(m,2)` | `np.vsplit(m,[2,5])` |

### H) Useful Week-15 tricks

| Function | Syntax | Simple | Complex |
|---|---|---|---|
| `sort` | `np.sort(a, axis=...)` | `np.sort(a)` | `np.sort(a, axis=1)` |
| `unique` | `np.unique(a, return_counts=...)` | `np.unique(a)` | `vals,c = np.unique(a, return_counts=True)` |
| `where` | `np.where(cond, x, y)` | `np.where(a>0,1,0)` | `np.where((a>10)&(a<20), a, -1)` |
| `argmax` / `argmin` | `np.argmax(a)` | `np.argmax(a)` | `np.argmin(a, axis=1)` |
| `cumsum` / `cumprod` | `np.cumsum(a)` | `np.cumsum(a)` | `np.cumsum(a, axis=0)` |
| `percentile` | `np.percentile(a, q)` | `np.percentile(a, 50)` | `np.percentile(a, [25,50,90], axis=1)` |
| `histogram` | `np.histogram(a, bins=...)` | `np.histogram(a, bins=5)` | `hist,b = np.histogram(a, bins=[0,10,20,50])` |
| `corrcoef` | `np.corrcoef(x, y)` | `np.corrcoef(x,y)` | correlation matrix for many features |
| `isin` / `in1d` | `np.isin(a, vals)` | `np.isin(a,[1,3])` | filter rows by allowed IDs |
| `flip` | `np.flip(a, axis=...)` | `np.flip(a)` | `np.flip(img, axis=1)` |
| `put` | `np.put(a, ind, vals)` | `np.put(a,[0],99)` | replace specific flat indices |
| `delete` | `np.delete(a, ind, axis=...)` | `np.delete(a, 0)` | `np.delete(a, [1,3], axis=1)` |
| `clip` | `np.clip(a, lo, hi)` | `np.clip(a,0,1)` | cap outliers: `np.clip(a,p1,p99)` |
| set ops | `np.union1d`, `np.intersect1d`, `np.setdiff1d`, `np.setxor1d` | `np.union1d(a,b)` | compare large ID lists |

### I) Missing values + broadcast

| Function | Syntax | Example |
|---|---|---|
| `np.isnan` | `np.isnan(a)` | `mask = np.isnan(a)` |
| `np.nan_to_num` | `np.nan_to_num(a, nan=...)` | `clean = np.nan_to_num(a, nan=0)` |
| `np.broadcast_to` | `np.broadcast_to(a, shape)` | `np.broadcast_to([1,2,3], (4,3))` |

---

## 3) Class: `np.nditer`

| Method/Use | Syntax | Example |
|---|---|---|
| Iterate element-wise | `for x in np.nditer(a): ...` | `for x in np.nditer(a): print(x)` |
| Read/write iterator | `np.nditer(a, op_flags=['readwrite'])` | update every element in-place |

---

## 4) Quick remember rules
- Use vectorized ops (NumPy functions) instead of Python loops.
- Prefer `axis` correctly: `axis=0` -> column-wise, `axis=1` -> row-wise.
- For boolean filters in NumPy, use `&` and `|`, not `and` / `or`.
