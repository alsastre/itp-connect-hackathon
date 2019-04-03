# LAUNDROMAT
## RELATIONSHIPS
### ACCOUNT_IN Relates Clients to Banks

### TRANSACTION Transaction between two clients
  date
  amount
  currency
  amount_eur
  amount_usd
  purpose
  reference_no
  sequence_no

## Nodes

### 2 X NODE-CLIENT
  payer_name
  payer_name_original
  payer_jurisdiction
  payer_core
  payer_account

  beneficiary_name
  beneficiary_name_original
  beneficiary_jurisdiction
  beneficiary_core
  beneficiary_account


### 2X NODE-BANK
  payer_bank NODE_BANK
  payer_bank_country NODE_BANK_attr
  beneficiary_bank
  beneficiary_bank_country


## TRANSACTIONS
step
type
amount
nameOrig
oldbalanceOrg
newbalanceOrig
nameDest
oldbalanceDest
newbalanceDest
isFraud
isFlaggedFraud
