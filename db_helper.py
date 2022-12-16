import psycopg2
import os

host = os.environ.get("RDS_HOSTNAME")
user = "postgres"
password = os.environ.get("RDS_PASSWORD")
database = "titanic"


def connect_to_db():

    connection = psycopg2.connect(
        host=host, port=5432, user=user, password=password, database="titanic"
    )
    cursor = connection.cursor()

    return connection, cursor