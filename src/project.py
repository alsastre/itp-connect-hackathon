import pandas as pd
df = pd.read_csv("data/laundromat.csv", low_memory=False, )
df_isna = df.isna()
result = df[(df_isna["payer_name"] == False) & (df_isna["beneficiary_name"] == False) & ((df_isna["payer_bank"] == False) | (df_isna["beneficiary_bank"] == False)]


