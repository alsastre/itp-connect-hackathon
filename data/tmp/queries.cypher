LOAD CSV WITH HEADERS FROM 'file:///cleaned.csv' AS line
CREATE (:Payer {id: line.pid,
                name: line.payer_name,
                bank: line.payer_bank})
CREATE (:Beneficiary {id: line.bid,
                      name: line.beneficiary_name, 
                      bank: line.beneficiary_bank});
