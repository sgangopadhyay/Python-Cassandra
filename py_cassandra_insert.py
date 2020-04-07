#PROGRAM : PYTHON PROGRAM TO CONNECT TO APACHE CASSANDRA NOSQL SERVER
#NAME OF PROGRAMMER : SUMAN GANGOPADHYAY
#EMAIL ID : linuxgurusuman@gmail
#DATE : 20-Jan-2020
#PYTHON : 3.7
#CASSANDRA : 3.11.6

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid
import datetime

auth = PlainTextAuthProvider(username='priya', password='priya@123')
cluster = Cluster(['127.0.0.1'], port = 9042, auth_provider=auth)
session = cluster.connect(keyspace='flask')

try:
    sql = "INSERT INTO customer_info(id, name, email, time_stamp) VALUES(%s, %s, %s, %s)";
    session.execute(sql,[uuid.uuid1(), 'Rinku', "rinku@rinku.com", datetime.datetime.now()])
    print("SUCCESS : DATA INSERTED SUCCESSFULLY")
except:
    print("ERROR : EITHER USERNAME / PASSWORD / KEYSPACE INCORRECT")
finally:
    cluster.shutdown()