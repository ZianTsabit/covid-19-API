from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import bigquery



app = FastAPI()
client = bigquery.Client()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/bq_v1/answer_sql1")
def answer_sql1():
    return {"Hello": "World"}

@app.get("/api/bq_v1/answer_sql2")
def answer_sql2():
    return {"Hello": "World"}