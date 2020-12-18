from twilio.rest import Client
from global_collection import *

import pymysql


conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
curs = conn.cursor()

sql = "SELECT phone FROM twiliousers order by ID"
curs.execute(sql) # 쿼리문 실행

rows = curs.fetchall()


def sendMessage(comment,conn, curs):
    account_sid = "AC91236f5ec23492627dc1dec070bfac25"
    auth_token = "d81c82507207ef7a857f52274caa135d"
    
    
    
    client = Client(account_sid, auth_token)

    for row in rows:
        message = client.messages.create(
        to=row,
        from_="+13342316869",
        body=comment)
        print(row)
    
    print(message.sid)
    conn.close()
