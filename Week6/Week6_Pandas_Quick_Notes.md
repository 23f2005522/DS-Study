<!-- markdownlint-disable MD024 MD060 -->

# Week 6: pandas Quick Notes

pandas provides labeled data structures for cleaning, analyzing, and transforming tables.

```python
import numpy as np
import pandas as pd
```

## 1. Series

A `Series` is like one labeled column.

```python
pd.Series(data, index=labels, name="name", dtype="...")
```

### Simple example

```python
marks = pd.Series([67, 90, 89], index=["maths", "english", "science"])
print(marks["maths"])
print(marks.mean())
```

### Complex example

```python
students = pd.Series(
    {"Anish": 82, "Riya": 91, "Kabir": 74},
    name="marks", dtype="int16"
)
print(students[students >= 80].sort_values(ascending=False))
```

Useful Series properties and methods:

```python
s.index; s.values; s.dtype; s.shape; s.size; s.ndim
s.head(); s.tail(); s.describe(); s.value_counts()
s.unique(); s.nunique(); s.isna(); s.notna()
s.to_list(); s.to_dict(); s.to_numpy(); s.to_frame()
```

## 2. DataFrame

A DataFrame is a two-dimensional table; each column is a Series.

```python
pd.DataFrame(data, index=..., columns=...)
```

### Simple example

```python
data = [[100, 80, 10], [90, 70, 7]]
students = pd.DataFrame(data, columns=["iq", "marks", "package"])
print(students)
```

### Complex example

```python
students = pd.DataFrame({
    "name": ["Anish", "Riya", "Kabir"],
    "iq": [100, 115, 90],
    "marks": [80, 92, 70],
    "package": [10, 14, 7]
}).set_index("name")
print(students)
```

## 3. Reading and Inspecting Data

```python
df = pd.read_csv("file.csv")
df = pd.read_csv(url)
df.head(n); df.tail(n); df.sample(n)
df.shape; df.columns; df.index; df.dtypes
df.info(); df.describe(include="all")
```

### Simple example

```python
df = pd.read_csv("students.csv")
print(df.head())
print(df.shape)
df.info()
```

### Complex example

```python
summary = df.describe().T
summary["range"] = summary["max"] - summary["min"]
print(summary.sort_values("range", ascending=False))
```

## 4. Selecting Columns and Rows

```python
df["marks"]                              # one column as Series
df[["iq", "marks"]]                      # several columns
df.loc[row_labels, column_labels]         # labels
df.iloc[row_positions, column_positions] # positions
df.at[row_label, column_label]            # one labeled cell
df.iat[row_position, column_position]    # one positional cell
```

### Simple example

```python
print(students["marks"])
print(students[["iq", "package"]])
print(students.loc["Anish", ["iq", "package"]])
```

### Complex example

```python
result = students.loc[
    (students["marks"] >= 80) & (students["package"] >= 10),
    ["iq", "marks", "package"]
]
print(result)
```

Without `loc` or `iloc`:

```python
students.reindex(index=["Anish", "Riya"], columns=["iq", "package"])
students.take([0, 1])[["iq", "package"]]
```

## 5. Filtering and `isin`

```python
df[df["marks"] > 80]
df[(df["marks"] > 80) & (df["package"] >= 10)]
df[df["city"].isin(["Delhi", "Mumbai"])]
df[~df["status"].isin(["inactive"])]
```

### Simple example

```python
high_scorers = students[students["marks"] >= 80]
```

### Complex example

```python
selected = students[
    students["iq"].between(90, 120) &
    students["package"].isin([7, 10, 14])
]
print(selected)
```

Use `&`, `|`, and `~` with parentheses. Do not use Python `and`, `or`, or `not` for Series conditions.

## 6. Counting Unique Values

```python
s.value_counts()
df["Team"].value_counts()
df.value_counts()                 # complete-row combinations
df["Team"].unique()
df["Team"].nunique()
```

### Simple example

```python
teams = pd.Series(["A", "A", "B", "C", "A"])
print(teams.value_counts())
print(teams.unique())
print(teams.nunique())
```

### Complex example

```python
home = matches["Team1"].value_counts().rename("home_matches")
away = matches["Team2"].value_counts().rename("away_matches")
summary = pd.concat([home, away], axis=1).fillna(0)
summary["total"] = summary.sum(axis=1).astype(int)
print(summary.sort_values("total", ascending=False))
```

## 7. Sorting and Ranking

```python
df.sort_values("marks", ascending=False)
df.sort_values(["marks", "name"], ascending=[False, True])
df.sort_index()
s.rank(method="average", ascending=False)
s.rank(method="first", ascending=False)
```

### Simple example

```python
print(students.sort_values("marks", ascending=False))
students["rank"] = students["marks"].rank(
    method="first", ascending=False
).astype("int16")
```

### Complex example

```python
table = students.sort_values(
    ["marks", "package"], ascending=[False, False]
).copy()
table["rank"] = table["marks"].rank(
    method="first", ascending=False
).astype("int16")
print(table)
```

`method="average"` gives ties an average rank. `method="first"` breaks ties by order.

## 8. Index Management

```python
df.set_index("name", inplace=True)
df.reset_index(inplace=True)
df.rename(index={old: new})
df.rename(columns={"old": "new"})
df.reindex(index=[...], columns=[...])
```

### Simple example

```python
students = students.reset_index()
students = students.set_index("name")
students = students.rename(columns={"package": "salary_lakh"})
```

### Complex example

```python
ranked = students.copy()
ranked["Rank"] = ranked["marks"].rank(
    method="first", ascending=False
).astype(np.int16)
ranked = ranked.set_index("Rank").sort_index()
print(ranked)
```

## 9. Missing Values

```python
df.isna(); df.isnull()
df.notna(); df.notnull()
df.isna().sum()          # per column
df.isna().sum(axis=1)    # per row
df.isna().sum().sum()     # whole DataFrame
df.dropna()
df.dropna(subset=["Age"])
df.fillna(value)
df["Age"].fillna(20)
```

### Simple example

```python
df = pd.DataFrame({"age": [20, np.nan, 25], "marks": [80, 90, np.nan]})
print(df.isna().sum())
df["age"] = df["age"].fillna(df["age"].mean())
df = df.dropna(subset=["marks"])
```

### Complex example

```python
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)
```

For permanent changes, assign the result back or use `inplace=True` where appropriate.

## 10. Duplicates and Dropping Data

```python
df.duplicated()
df.duplicated(subset=["name"], keep="first")
df.duplicated(keep=False)
df.drop_duplicates()
df.drop_duplicates(inplace=True)
df.drop(columns=["col1", "col2"])
df.drop(index=[row1, row2])
```

### Simple example

```python
marks = pd.DataFrame({"iq": [100, 90, 90], "marks": [80, 70, 70]})
print(marks.duplicated())
marks = marks.drop_duplicates()
```

### Complex example

```python
duplicate_people = students[students.duplicated(subset=["iq"], keep=False)]
students = students.drop_duplicates(subset=["iq"], keep="last")
students = students.drop(columns=["rank"], errors="ignore")
```

`duplicated()` checks complete rows by default. A row becomes `True` when the same values appeared earlier.

## 11. Applying Functions and Adding Columns

```python
df["new"] = df["old"].apply(function)
df["new"] = df.apply(function, axis=1)
df.insert(position, "column_name", values)
```

### Simple example

```python
students["passed"] = students["marks"].apply(lambda mark: mark >= 50)
```

### Complex example

```python
def performance(row):
    if row["marks"] >= 90 and row["package"] >= 12:
        return "excellent"
    if row["marks"] >= 75:
        return "good"
    return "needs improvement"

students["performance"] = students.apply(performance, axis=1)
students.insert(0, "record_id", range(1, len(students) + 1))
```

## 12. Data Types, Copying, and Correlation

```python
df.astype({"marks": "int16"})
df["marks"] = df["marks"].astype(np.int16)
copy_df = df.copy()
df.corr(numeric_only=True)
```

### Simple example

```python
students["marks"] = students["marks"].astype(np.int16)
safe_copy = students.copy()
```

### Complex example

```python
numeric = students.select_dtypes(include="number")
correlation = numeric.corr()
print(correlation)
```

Use `.copy()` before changing a filtered DataFrame so you do not accidentally modify a view.

## 13. String Column Methods

String methods are accessed through `.str`.

```python
df["name"].str.lower()
df["name"].str.upper()
df["name"].str.strip()
df["name"].str.contains("word", na=False)
df["name"].str.startswith("A")
df["name"].str.split(", ")
df["name"].str.replace("old", "new", regex=False)
```

### Simple example

```python
names = pd.Series([" Anish ", "Riya"])
print(names.str.strip().str.upper())
```

### Complex example

```python
df["Team"] = df["Team"].str.strip().str.replace(
    "Daredevils", "Capitals", regex=False
)
df["is_final"] = df["MatchNumber"].str.contains("Final", na=False)
```

## 14. Combining Series and DataFrames

```python
pd.concat([df1, df2], axis=0, ignore_index=True)  # stack rows
pd.concat([s1, s2], axis=1)                       # align columns
```

### Simple example

```python
first = pd.Series([1, 2])
second = pd.Series([3, 4])
combined = pd.concat([first, second], ignore_index=True)
```

### Complex example

```python
team1 = matches["Team1"].rename("team")
team2 = matches["Team2"].rename("team")
all_teams = pd.concat([team1, team2], ignore_index=True)
print(all_teams.value_counts().head())
```

Use `pd.concat`, not `Series.append` or `DataFrame.append`; append was removed in pandas 2.0.

## 15. IPL Point Table Pattern

### Simple example: wins per team

```python
wins = matches["WinningTeam"].value_counts().rename("wins")
print(wins)
```

### Complex example

```python
def point_table(matches, season):
    season_df = matches[matches["Season"] == season].copy()
    teams = pd.unique(season_df[["Team1", "Team2"]].values.ravel())
    rows = []

    for team in teams:
        played = ((season_df["Team1"] == team) |
                  (season_df["Team2"] == team)).sum()
        won = (season_df["WinningTeam"] == team).sum()
        no_result = (
            season_df["WinningTeam"].isna() &
            ((season_df["Team1"] == team) |
             (season_df["Team2"] == team))
        ).sum()
        rows.append([team, played, won, no_result, won * 2 + no_result])

    result = pd.DataFrame(rows, columns=[
        "TeamName", "MatchesPlayed", "MatchesWon", "NoResult", "Points"
    ])
    return result.sort_values(
        ["Points", "TeamName"], ascending=[False, True]
    ).set_index("TeamName")

point_table(matches, "2022")
```

## 16. Parsing a String List of Players

When a CSV stores a list as text, clean it before counting.

### Simple example

```python
text = "['A', 'B', 'C']"
players = [item.strip(" '") for item in text.strip("[]").split(", ")]
print(players)
```

### Complex example

```python
def get_players(text):
    return [item.strip(" '") for item in text.strip("[]").split(", ")]

final = matches[matches["MatchNumber"] == "Final"]
player_lists = pd.concat([
    final["Team1Players"].map(get_players).explode(),
    final["Team2Players"].map(get_players).explode()
], ignore_index=True)

print(player_lists.value_counts().head())
```

## 17. Practical Cleaning Pipeline

```python
df = pd.read_csv("file.csv")
df = df.copy()
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.dropna(subset=["required_column"])
df = df.rename(columns={"old": "new"})
df = df.sort_values("new")
```

## Fast Revision: Common Traps

- `df.isna().sum()` is column-wise because default `axis=0`; `axis=1` is row-wise.
- `df["col"]` returns a Series; `df[["col"]]` returns a DataFrame.
- `loc` uses labels; `iloc` uses integer positions.
- `dropna(subset=["Age"])` drops rows where Age is missing.
- `fillna` returns a result; assign it back for a permanent change.
- `duplicated()` checks complete rows unless `subset` is given.
- `sort_values` sorts columns; `sort_index` sorts labels.
- `method="first"` gives tied ranks distinct positions.
- Use `pd.concat()` in current pandas; `append()` is removed.
- Use `.copy()` before modifying a filtered DataFrame.
