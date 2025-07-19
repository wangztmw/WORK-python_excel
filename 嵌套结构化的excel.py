import pandas as pd

df = pd.read_excel('~/Downloads/Book1.xlsx')

print(df.head())

print("————")

print(df[[1, 23]])