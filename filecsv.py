from os import write
import csv
import pandas as pd
acme=pd.read_csv("acme_worksheet.csv")
df=pd.pivot_table(acme,
               index=["Employee_Name"],
               values=["Work_Hours"],
               columns=["Date"])
print(df)
df.to_csv('out.csv', encoding='utf-8')