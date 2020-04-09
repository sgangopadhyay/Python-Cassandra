#PROGRAM : PYTHON PROGRAM TO UPDATE DATA IN A TABLE
#NAME OF PROGRAMMER : SUMAN GANGOPADHYAY
#EMAIL ID : linuxgurusuman@gmail
#DATE : 20-Jan-2020
#PYTHON : 3.7
#CASSANDRA : 3.11.6

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credential = PlainTextAuthProvider(username='priya', password='priya@123')

conn = Cluster(['127.0.0.1'], port = 9042, auth_provider=user_credential)

try:
    cur = conn.connect(keyspace='flask')
    id = 'e70583f0-7a42-11ea-b49f-bf92b0301db9'
    id = uuid.UUID(id)
    sql = "UPDATE suman_blog SET name = %s  WHERE id = %s"
    cur.execute(sql, ('Nitin Shukla Ji', id))
    print("Success !!!")
except:
    print("ERROR : Unable to Update due to unknow reasons !")
finally:
    cur.shutdown()
