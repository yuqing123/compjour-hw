import pandas as pd

a = pd.read_csv("YA_1980_050.csv")
b = pd.read_csv("YA_2009_2013_050.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='fips')
merged.to_csv("output.csv", index=False)