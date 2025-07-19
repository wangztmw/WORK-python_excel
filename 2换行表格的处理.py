import pandas as pd

df = pd.read_excel('2换行表格.xlsx', engine='openpyxl')

print(df[['积极\n乐观', '西瓜']])