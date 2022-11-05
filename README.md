# covid-19-API
API to covid 19 data using big query

# Requirements

- Python
- fastapi
- bigquery
- codecs
- os

# How to run

first, you have to upload you google service account credentials json file in the app
directory.
<br>
<br>
After that, you have to change your crendentials filename to credentials.json
<br>
<br>
After that, run this command on your terminal

``` python -m uvicorn app.app:app --reload ```