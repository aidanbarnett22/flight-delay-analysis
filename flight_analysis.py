import pandas as pd


df = pd.read_parquet("data/Combined_Flights_2022.parquet")

sample_df = df.sample(100000)

print(sample_df.shape)

