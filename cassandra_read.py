from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

user_credentials = PlainTextAuthProvider(username='priya', password='priya@123')

conn = Cluster(['10.31.79.1'], port = 9042, auth_provider=user_credentials)

cur = conn.connect(keyspace='flask')

def display_all():
    sql = "SELECT * FROM suman_blog"
    row = cur.execute(sql)
    for row in row:
        print (row.id, row.name, row.mobile)
    cur.shutdown()

def display_by_id(id):
    id = uuid.UUID(id)
    sql = "SELECT * FROM suman_blog WHERE id = {0}".format(id)
    row = cur.execute(sql)
    for row in row:
        print([row[0], row[1], row[2]])
    cur.shutdown()

print(display_by_id('dd02adf0-7a89-11ea-a1ef-cf37c72223b8'))
print('=========================')






