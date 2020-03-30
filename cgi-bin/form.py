#!/usr/bin/env python3

import cgi
form = cgi.FieldStorage()
#text1 = form.getfirst("TEXT_1", "не задано")
#text2 = form.getfirst("TEXT_2", "не задано")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Processing</title>
        </head>
        <body>""")

data_names = ['name','e_mail','year','sex','hands','abilities','biography','agreed']
#print(data_names)
data = {}
f = True
for x in data_names:
    if form.getvalue(x) is None: 
        print('''
        <h1>You mustn't hide anything from us! Try again please! You didn't pass data into {}</h1>
        <a href='/'> Try again </a>
        '''.format(x))
        f = False
        break
if f:
    for x in data_names:
        if form.getvalue(x)=='on': data[x]=True
        elif form.getvalue(x)=='on': data[x]=False
        else: data[x]=form.getvalue(x)
    print("""
    <h1> We're proud to see you in our command! </h1>
        <a href='/'> Get back </a>
    """)
print(data.keys(),data.values())
print("""</body>
        </html>""")

import pymysql.cursors  
print(5)
def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',                             
                                 db='back',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
connection = getConnection()
cursor = connection.cursor()
sql="""Insert back.heroes (name, e_mail, year, sex, hands, abilities, biography, agreed) 
values {};""".format(tuple(data.values()))
cursor.execute(sql)
connection.commit()
connection.close()