#! /usr/bin/ENV python

import json

INPUT = '{"request":{"fields":["CHECKINGSTATUS","LOANDURATION","CREDITHISTORY","LOANPURPOSE","LOANAMOUNT","EXISTINGSAVINGS","EMPLOYMENTDURATION","INSTALLMENTPERCENT","SEX","OTHERSONLOAN","CURRENTRESIDENCEDURATION","OWNSPROPERTY","AGE","INSTALLMENTPLANS","HOUSING","EXISTINGCREDITSCOUNT","JOB","DEPENDENTS","TELEPHONE","FOREIGNWORKER"],"values":['
OUTPUT = '},"response":{"fields":["CHECKINGSTATUS","LOANDURATION","CREDITHISTORY","LOANPURPOSE","LOANAMOUNT","EXISTINGSAVINGS","EMPLOYMENTDURATION","INSTALLMENTPERCENT","SEX","OTHERSONLOAN","CURRENTRESIDENCEDURATION","OWNSPROPERTY","AGE","INSTALLMENTPLANS","HOUSING","EXISTINGCREDITSCOUNT","JOB","DEPENDENTS","TELEPHONE","FOREIGNWORKER","CHECKINGSTATUS_IX","CREDITHISTORY_IX","EMPLOYMENTDURATION_IX","EXISTINGSAVINGS_IX","FOREIGNWORKER_IX","HOUSING_IX","INSTALLMENTPLANS_IX","JOB_IX","LOANPURPOSE_IX","OTHERSONLOAN_IX","OWNSPROPERTY_IX","SEX_IX","TELEPHONE_IX","features","rawPrediction","probability","prediction","predictedLabel"],"values":['

NEW_STRING_REQ= '{"request":{"fields":'
NEW_STRING_VAL = ',"values":['

IN_FILE="payload_history_7.json"
OUT_FILE="new_payload_history_7.json"

with open(IN_FILE, "r") as reader:
    with open(OUT_FILE, "w") as writer:
        json_obj = json.load(reader)
        for obj in json_obj:
            k,v = obj.items()
            x,y = k[1].items()
            w,z = v[1].items()
            line = INPUT + str(y[1][0]) + ']' + OUTPUT + str(z[1][0]) + ']}},' + '\n'
            line = line.replace("'", '"')
            
            #print(line)
            writer.write(line)
                
