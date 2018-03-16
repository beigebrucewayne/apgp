# Handling Column Names from PG

```python
import re
import itertools

# response from PG query
df

# grab first list from returned query
cols = df[0]

# convert response to str
cols = str(cols).split(" ")

# split based on "="
cols_str = [c for c in cols if c.__contains__("=")]

# list of list with correct column names
col_names = [re.findall(r'^(.*?)=', col) for col in cols_str]

# iterator returning elements from nested list
chain = itertools.chain(*col_names)

# return final list of correct column names
final_col_names = list(chain)

# replace df column names
df.columns = final_col_names
```
