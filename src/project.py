import pandas as pd

def clean_data(in_df):
  df_isna = in_df.isna()
  # Create unique identifier for payers and beneficiaries
  result =
  # Remove data without banks information
  result = in_df[(df_isna["payer_name"] == False) & (df_isna["beneficiary_name"] == False)]
  # Remove data without banks information
  # result = result[((df_isna["payer_bank"] == False) | (df_isna["beneficiary_bank"] == False))]
  return result

def import_dataframe(df):
  pass

def main():
  df = pd.read_csv("data/laundromat.csv", low_memory=False, )
  df_cleaned = clean_data(df)
  print(df_cleaned)

if __name__ == "__main__":
    main()
