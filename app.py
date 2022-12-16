import db_helper as db
import streamlit as st

connection, cursor = db.connect_to_db()

st.title("Analysis of energy use around the world")

cursor.execute("select countryname, value from import.indicators where indicatorcode='EG.USE.COMM.FO.ZS' order by value desc;")
country_data = cursor.fetchall()
country = cursor.fetchall()[0][0]

st.write(f"The country that derives the maximum percentage of energy from fossil fuels is {country}.")