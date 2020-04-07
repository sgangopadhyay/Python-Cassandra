#PROGRAM : PYTHON PROGRAM TO CONNECT TO APACHE CASSANDRA NOSQL SERVER
#NAME OF PROGRAMMER : SUMAN GANGOPADHYAY
#EMAIL ID : linuxgurusuman@gmail
#DATE : 20-Jan-2020
#PYTHON : 3.7
#CASSANDRA : 3.11.6

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid
import time

auth = PlainTextAuthProvider(username='priya', password='priya@123')
cluster = Cluster(['127.0.0.1'], port = 9042, auth_provider=auth)
session = cluster.connect(keyspace='flask')

try:
    table_create = "CREATE TABLE IF NOT EXISTS customer_info(id UUID PRIMARY KEY, name TEXT, email TEXT, time_stamp TEXT)"
    session.execute(table_create)
    print("SUCCESS : TABLE CREATED SUCCESSFULLY")
except:
    print("ERROR : EITHER USERNAME / PASSWORD / KEYSPACE INCORRECT")
finally:
    cluster.shutdown()