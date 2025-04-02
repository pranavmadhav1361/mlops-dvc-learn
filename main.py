import pandas as pd
import os

data = {'Name': ['Alice', 'bob', 'charlie'],
        'Age': [20,35,65],
        'city': ['new york','los angeles', 'chicago']
        }

df = pd.DataFrame(data)

newloc = {'Name':'priya',
          'Age': 20,
          'city': 'chennai'}
newloc2 = {'Name':'harsh',
          'Age': 20,
          'city': 'chennai'}
df.loc[len(df.index)] = newloc
df.loc[len(df.index)] = newloc2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index = False)
