import pandas as pd

def main():
  df = pd.read_csv("data/laundromat.csv", low_memory=False, )
  df_isna = df.isna()
  result = df[(df_isna["payer_name"] == False) & (df_isna["beneficiary_name"] == False) & ((df_isna["payer_bank"] == False) | (df_isna["beneficiary_bank"] == False))]
  print(result)

if __name__ == "__main__":
    main()
