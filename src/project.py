import pandas as pd
import fuzzywuzzy as fuzz
from fuzzywuzzy import process

list_of_entitites = []


def fuzzy_it(old):
  match, percentage = process.extractOne(old, list_of_entitites)
  if(percentage < 75):
    # print("Appending...")
    list_of_entitites.append(old)
    return old
  else:
    return match

def fuzzy_clean(df):
  global list_of_entitites
  fields_to_clean = ["payer_name", "payer_bank", "beneficiary_name", "beneficiary_bank"]
  # fields_to_clean = ["payer_bank"]
  for f in fields_to_clean:
    df[f] = df[f].map(str) # Because of Nan  Values

  for f in fields_to_clean:
    # print(df[f])
    list_of_entitites = [df[f].get(1)]
    df[f] = df[f].transform(fuzzy_it)
    print("Cleaned %s" % f)
    # print("-------------")
    # print(df[f])
  print("END FUZZING")
  return


def clean_data(df):
  # df_isna = df.isna()
  # Create unique identifier for payers and beneficiaries
  # print("------------BEFORE CLEAN:--------------")
  # print(df.nunique())
  # print(df["payer_bank"])
  # fuzzy_clean(df)
  # print("-------AFTER CLEAN:------------")
  # print(df.nunique())
  # print(df["payer_bank"])

  # Remove data without banks information
  # result = in_df[(df_isna["payer_name"] == False) & (df_isna["beneficiary_name"] == False)]
  # Remove data without banks information
  # result = result[((df_isna["payer_bank"] == False) | (df_isna["beneficiary_bank"] == False))]
  return

def import_dataframe(df, session):
  pass

# TODO Fuzzy Matchingfor NAMES of CLIENTS AND BANKS PYTHON PANDAS + FZZYW...
# TODO Add properties to Nodes and Relationships
# TODO Algortihms
# TODO Presentation

def main():
  df = pd.read_csv("data/laundromat.csv", low_memory=False, )
  clean_data(df)
  df.to_csv("data/laundromat_cleaned.csv", index=False)
  # print(df_cleaned)
  # neo_driver = GraphDatabase.driver("bolt://localhost:7687/facrec", auth=("neo4j", "facrec"))

if __name__ == "__main__":
    main()
