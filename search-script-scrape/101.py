import pandas as pd
CSVURL = 'http://unitedstates.sunlightfoundation.com/legislators/legislators.csv'
df = pd.read_csv(CSVURL)
print (len(df[(df['gender'] == 'F') & (df['in_office'] == 1)]))
