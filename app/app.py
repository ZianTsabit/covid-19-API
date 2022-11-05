from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
from codecs import open
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app\credentials.json"
app = FastAPI()
client = bigquery.Client()


@app.get("/")
def read_root():
    return {"message": "Hello World !"}

@app.get("/api/bq_v1/answer_sql1")
def answer_sql1():

    sqlfile = "sql/answer_sql1.sql"
    query = open(sqlfile, mode='r', encoding='utf-8-sig').read() 
    query_job = client.query(query)
    rows = query_job.result()   
    data = None
    for row in rows:
        data = row[0]
    
    if data is None:
        return {"message": "No data found"}
    else:
        return {
            "message": "Successfully retrieved data total persons cumulatively vaccinated in Indonesia on June 1, 2022 ",
            "data": data
        }

@app.get("/api/bq_v1/answer_sql2")
def answer_sql2():
    
    sqlfile = "sql/answer_sql2.sql"
    query = open(sqlfile, mode='r', encoding='utf-8-sig').read() 
    query_job = client.query(query)
    rows = query_job.result()   
    data = None
    for row in rows:
        data = row[0]

    if data is None:
        return {"message": "No data found"}
    else:
        return {
            "message": "Successfully retrieved data total confirmed case in Indonesia during January 1, 2022",
            "data": data
        }