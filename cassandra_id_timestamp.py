#PROGRAM : PYTHON PROGRAM TO INSERT ID & TIMESTAMP INTO APACHE CASSANDRA DATABASE
#NAME OF PROGRAMMER : SUMAN GANGOPADHYAY
#EMAIL ID : linuxgurusuman@gmail
#DATE : 20-Jan-2020
#PYTHON : 3.7
#CASSANDRA : 3.11.6

import uuid
import datetime
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

auth = PlainTextAuthProvider(username='priya', password='priya@123')
cluster = Cluster(['127.0.0.1'], port = 9042, auth_provider=auth)
session = cluster.connect(keyspace='flask')

try:
    time_stamp = datetime.datetime.now()
    id = uuid.uuid1()
    sql = "INSERT INTO calendar(id, time_stamp) VALUES(%s, %s)";
    session.execute(sql,[uuid.uuid1(), datetime.datetime.now()])
    print("SUCCESS : ", id, " ", time_stamp," INSERTED SUCCESSFULLY")
except:
    print("ERROR : EITHER USERNAME / PASSWORD / KEYSPACE INCORRECT")
finally:
    cluster.shutdown()
    print("CONNECTION CLOSED !")


