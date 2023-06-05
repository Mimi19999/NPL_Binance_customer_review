# import data
import pandas as pd
df = pd.read_csv('/Users/mimi/binance_reviews.txt', sep="\n"*2, header=None)
print(df)
df = df.rename(columns={0: 'review'})
print(df)
