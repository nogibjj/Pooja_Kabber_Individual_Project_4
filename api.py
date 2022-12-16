from fastapi import FastAPI, Response
import db_helper as db
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/country")
def get_countries_list():
    connection, cursor = db.connect_to_db()
    cursor.execute("select countryname, value from import.indicators where indicatorcode='EG.USE.COMM.FO.ZS' order by value desc;")
    country_data = cursor.fetchall()[0][0]
    country = country_data[0]
    connection.close()
    cursor.close()
    return Response(content=json.dumps({"result": country}), media_type="application/json")