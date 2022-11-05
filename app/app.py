from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery
from codecs import open
import os

def authenticate(credentials_path):
    # Authenticate to Google Cloud
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "app\\" + credentials_path
    client = bigquery.Client()
    return client

app = FastAPI()
client = authenticate("credentials.json")

@app.get("/")
def read_root():
    return {"message": "Hello, this is ghazian submission for the Data Engineer Internship at Merkle"}

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