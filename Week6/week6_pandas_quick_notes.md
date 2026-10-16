# Week 6 Quick Revision - Pandas (Syntax + Simple/Complex Examples)

## 1) Core classes
- `pd.Series` -> 1D labeled data
- `pd.DataFrame` -> 2D tabular data

---

## 2) Class: `pd.Series`

### A) Create / load

| Method/Function | Syntax | Simple example | Complex example |
|---|---|---|---|
| `pd.Series` | `pd.Series(data, index=...)` | `s = pd.Series([10,20,30])` | `s = pd.Series({'a':10,'b':20}, dtype='float64')` |
| `pd.read_csv` + squeeze | `pd.read_csv(path).squeeze()` | `s = pd.read_csv('subs.csv').squeeze()` | load, cast, and clean in one flow |

### B) Attributes / inspection

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `head` / `tail` | `s.head(n)` | `s.head()` | `s.tail(10)` |
| `dtype` / `shape` / `size` | `s.dtype`, `s.shape` | `s.dtype` | memory checks before pipeline |
| `count` | `s.count()` | `s.count()` | count after filtering |
| `isnull` / `notnull` | `s.isnull()` | `s.isnull().sum()` | null rate per stage |
| `value_counts` | `s.value_counts()` | `s.value_counts()` | `s.value_counts(normalize=True)` |
| `nunique` / `unique` | `s.nunique()`, `s.unique()` | `s.nunique()` | cardinality checks for IDs |

### C) Transform / clean

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `astype` | `s.astype(dtype)` | `s.astype(int)` | `s.astype('category')` |
| `apply` | `s.apply(func)` | `s.apply(str.upper)` | `s.apply(lambda x: x.strip().title())` |
| string split | `s.str.split(...)` | `s.str.split(' ')` | `s.str.split(',', expand=True)` |
| `between` | `s.between(lo, hi)` | `s[s.between(10,20)]` | combined with other masks |
| `clip` | `s.clip(lower, upper)` | `s.clip(0,100)` | cap extreme outliers |
| `drop_duplicates` | `s.drop_duplicates()` | `s.drop_duplicates()` | keep last duplicate: `keep='last'` |
| `duplicated` | `s.duplicated()` | `s[s.duplicated()]` | mark duplicate keys for QA |

### D) Math / aggregation

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `sum` / `mean` | `s.sum()`, `s.mean()` | `s.mean()` | `s[s>0].mean()` |
| `quantile` | `s.quantile(q)` | `s.quantile(0.5)` | `s.quantile([0.25,0.5,0.9])` |
| `rank` | `s.rank()` | `s.rank()` | `s.rank(method='dense', ascending=False)` |

### E) Indexing

| Type | Syntax | Simple | Complex |
|---|---|---|---|
| label | `s.loc[label]` | `s.loc['Virat']` | `s.loc[['A','B']]` |
| position | `s.iloc[idx]` | `s.iloc[0]` | `s.iloc[5:15:2]` |
| boolean filter | `s[mask]` | `s[s>3000]` | `s[(s>1000) & (s<5000)]` |

---

## 3) Class: `pd.DataFrame`

### A) Create / load

| Method/Function | Syntax | Simple example | Complex example |
|---|---|---|---|
| `pd.DataFrame` | `pd.DataFrame(data)` | `df = pd.DataFrame({'a':[1,2]})` | `df = pd.DataFrame(records, columns=[...])` |
| `pd.read_csv` | `pd.read_csv(path)` | `df = pd.read_csv('movies.csv')` | with parse/rename/select pipeline |
| `pd.concat` | `pd.concat([df1, df2], axis=...)` | `pd.concat([a,b])` | row union + `ignore_index=True` |

### B) Inspect quickly

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `head` | `df.head(n)` | `df.head()` | `df.head(20)` |
| `info` | `df.info()` | `df.info()` | validate nulls + dtypes |
| `describe` | `df.describe()` | `df.describe()` | include categorical: `include='all'` |
| `isnull` / `isna` | `df.isnull()` | `df.isnull().sum()` | null audit by selected columns |
| `duplicated` | `df.duplicated(subset=...)` | `df.duplicated().sum()` | duplicate check by business key |

### C) Select rows/cols

| Type | Syntax | Simple | Complex |
|---|---|---|---|
| columns | `df['col']`, `df[['c1','c2']]` | `df['team']` | `df[['team','winner']]` |
| label-based | `df.loc[row_sel, col_sel]` | `df.loc[0:5, 'team']` | `df.loc[df['season']==2011, ['team1','team2']]` |
| position-based | `df.iloc[row_sel, col_sel]` | `df.iloc[:3, :2]` | `df.iloc[::2, [0,3,5]]` |
| filter | `df[condition]` | `df[df['runs']>50]` | multiple conditions with `&` / `|` |

### D) Clean / transform

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `astype` | `df[col].astype(dtype)` | `df['age']=df['age'].astype(int)` | convert many columns via dict |
| `fillna` | `df.fillna(value)` | `df.fillna(0)` | `df.fillna({'city':'Unknown','age':df['age'].mean()})` |
| `dropna` | `df.dropna(...)` | `df.dropna()` | `df.dropna(subset=['winner'])` |
| `drop` | `df.drop(labels, axis=...)` | `df.drop('temp', axis=1)` | `df.drop(['c1','c2'], axis=1)` |
| `rename` | `df.rename(columns={...})` | `df.rename(columns={'old':'new'})` | rename rows + columns together |
| `apply` | `df.apply(func, axis=...)` | `df.apply(len)` | row-wise score calc `axis=1` |
| `reset_index` | `df.reset_index(drop=...)` | `df.reset_index(drop=True)` | after sorting/filtering pipelines |
| `set_index` | `df.set_index(col)` | `df.set_index('team')` | multi-index: `df.set_index(['season','team'])` |

### E) Sort / aggregate

| Method | Syntax | Simple | Complex |
|---|---|---|---|
| `sort_values` | `df.sort_values(by=...)` | `df.sort_values('runs')` | `df.sort_values(['season','points'], ascending=[True,False])` |
| `sort_index` | `df.sort_index()` | `df.sort_index()` | sort multi-index levels |
| `value_counts` | `df[col].value_counts()` | `df['team'].value_counts()` | normalized share by team |
| `sum` / `mean` | `df[col].sum()` | `df['runs'].sum()` | grouped-like summaries after filters |
| `nunique` | `df[col].nunique()` | `df['player'].nunique()` | per-column uniqueness checks |
| `sample` | `df.sample(n=...)` | `df.sample(5)` | `df.sample(frac=0.2, random_state=42)` |

---

## 4) Fast syntax templates

```python
# Series
s = pd.Series(data, index=...)
s = pd.read_csv(path).squeeze()
s2 = s.astype('int64').drop_duplicates()
out = s[(s > a) & (s < b)].value_counts()
```

```python
# DataFrame
df = pd.read_csv(path)
df = (df.dropna(subset=['col'])
        .assign(new_col=lambda x: x['a'] + x['b'])
        .sort_values(['col1','col2'], ascending=[True, False])
        .reset_index(drop=True))
```

---

## 5) Quick remember rules
- Use `.loc` for labels, `.iloc` for positions.
- Use `&` and `|` for multiple conditions (with brackets).
- Prefer method chaining for clean, readable complex pipelines.
