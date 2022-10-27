import psycopg2
import sys
import boto3
import os

ENDPOINT="stc-teste-db.ciypzm2myz4i.us-east-2.rds.amazonaws.com"
PORT="5432"
USER="postgres"
REGION="us-east-2"
DBNAME="stc-teste-db"

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=token, sslrootcert="SSLCERTIFICATE")
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))                
                