import pandas as pd
import json
import os
import re

df = pd.read_excel("Excel_files/MARCH.xlsx", usecols = "B:G",encoding='utf-8' )


data = df.dropna(axis = 0, how= "any")
data.columns = data.iloc[0]

data2 = data.iloc[1:,].reindex()


#data2 = data2[~data2.B.str.contains("Unnamed: 1")]
#data3 = data2.to_dict()
date = data2.columns[2]
data2.columns = data2.columns.map(lambda x: x.replace('\n', ''))
# Turning 
da = data2.rename(columns = {
    "Name":"sector",
    'BUDGET AMOUNT  ': "budget",
    "March" : "allocation",
    "YR PMTS TO DATE" : "total_allocation",
    "BUDGET BALANCE": "balance"

})
print(da.columns)
