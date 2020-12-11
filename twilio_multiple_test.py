from twilio.rest import Client
from global_collection import *

import pymysql


conn = pymysql.connect(host = HOST,port=PORT,password=PASSWORD, user = USER,db = DB, charset=CHARSET)
curs = conn.cursor()

sql = "SELECT phone_number FROM users order by ID"
curs.execute(sql) # 쿼리문 실행

rows = curs.fetchall()


def sendMessage(comment):
    account_sid = "AC91236f5ec23492627dc1dec070bfac25"
    auth_token = "261137fc8646f13fd1d24c8d48024cce"
    
    
    
    client = Client(account_sid, auth_token)

    for row in rows:
        message = client.messages.create(
        to=row,
        from_="+13342316869",
        body=comment)
        print(row)
    
    print(message.sid)
    conn.close()
