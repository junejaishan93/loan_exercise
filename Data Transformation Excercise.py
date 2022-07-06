#import required packages
import pandas as pd
import psycopg2

#setup conection to database
conn = psycopg2.connect(
    host="f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud",
    port=30835, 
    database="q2c",
    user="q2c_user",
    password="passw0rd")

#read data from database
db_input = pd.read_sql("select * from loan_data",conn)

#create required columns as per exercise
db_input["int_rates_add_2pct"] = db_input["int_rate"] + 2 # add 2 percent to existin percentage
db_input["new term"] = db_input["term"]
db_input.loc[(db_input["term"] == "36 months") & (db_input["loan_status"]!="Fully Paid"),"new term"] = "48 months"  #add 12 months to 36

db_input.to_csv(r"OUTPUT.csv")