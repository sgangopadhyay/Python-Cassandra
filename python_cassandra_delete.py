#PROGRAM : PYTHON PROGRAM TO DELETE DATA IN A TABLE
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

cur = conn.connect(keyspace='flask')
id = uuid.UUID('2a06e2b0-7a53-11ea-b49f-bf92b0301db9')

sql = "DELETE FROM suman_blog WHERE id = {0}".format(id)
cur.execute(sql)
print("SUCCESS : Record Deleted Succcessfully !!!")
cur.shutdown()
