#! /usr/bin/ENV python

import json

PRE = '{"scoring_id": '
INPUT = ' , "request":{"fields":["CHECKINGSTATUS","LOANDURATION","CREDITHISTORY","LOANPURPOSE","LOANAMOUNT","EXISTINGSAVINGS","EMPLOYMENTDURATION","INSTALLMENTPERCENT","SEX","OTHERSONLOAN","CURRENTRESIDENCEDURATION","OWNSPROPERTY","AGE","INSTALLMENTPLANS","HOUSING","EXISTINGCREDITSCOUNT","JOB","DEPENDENTS","TELEPHONE","FOREIGNWORKER"],"values":['
OUTPUT = '},"response":{"fields":["CHECKINGSTATUS","LOANDURATION","CREDITHISTORY","LOANPURPOSE","LOANAMOUNT","EXISTINGSAVINGS","EMPLOYMENTDURATION","INSTALLMENTPERCENT","SEX","OTHERSONLOAN","CURRENTRESIDENCEDURATION","OWNSPROPERTY","AGE","INSTALLMENTPLANS","HOUSING","EXISTINGCREDITSCOUNT","JOB","DEPENDENTS","TELEPHONE","FOREIGNWORKER","CHECKINGSTATUS_IX","CREDITHISTORY_IX","EMPLOYMENTDURATION_IX","EXISTINGSAVINGS_IX","FOREIGNWORKER_IX","HOUSING_IX","INSTALLMENTPLANS_IX","JOB_IX","LOANPURPOSE_IX","OTHERSONLOAN_IX","OWNSPROPERTY_IX","SEX_IX","TELEPHONE_IX","features","rawPrediction","probability","prediction","predictedLabel"],"values":['
POST = ']}, "response_time": 267},'

NEW_STRING_REQ= '{"request":{"fields":'
NEW_STRING_VAL = ',"values":['

IN_FILE="payload_history_0.json"
OUT_FILE="new_payload_history_0.json"

with open(IN_FILE, "r") as reader:
    with open(OUT_FILE, "w") as writer:
        json_obj = json.load(reader)
        for obj in json_obj:
            j,k,v,m = obj.items()
            x,y = k[1].items()
            w,z = v[1].items()
            line = PRE + '"' + j[1] + '"' + INPUT + str(y[1][0]) + ']' + OUTPUT + str(z[1][0]) + POST + '\n'
            #line = PRE + str(j[1]) + INPUT + str(y[1][0]) + ']' + OUTPUT + str(z[1][0]) + POST + '\n'
            #sub_line = INPUT + str(y[1][0]) + ']' + OUTPUT + str(z[1][0]) + POST + '\n'
            #sub_line = sub_line.replace("'", '"')

            #line = PRE,  j[1], sub_line
            line = line.replace("'", '"')
            
            print(line)
            writer.write(line)
                
