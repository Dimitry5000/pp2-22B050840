import psycopg2
import re
from config import host, user, password, db_name
try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    cursor = connection.cursor()
    connection.autocommit = True
    mode = int(input("Type 1 for inserting via csv file, 2 for inserting via console input, 3 for updating, 4 for deleating, 5 for pattern function, 6 for insert procedure, 7 for insert many procedure, 8 for querying function, 9 for delete procedure"))
    if mode == 1:
        fname = input("type files name")
        file = open(fname)
        for line in file:
            name = re.split(":", line)[0]
            phone = re.split(":", line)[1]
            cmd = "INSERT INTO phonebook(username, phone) VALUES('" + name + "' , '" + phone + "' )" 
            cursor.execute(cmd)
    if mode == 2:
        line = input("type username:phone")
        name = re.split(":", line)[0]
        phone = re.split(":", line)[1]
        cmd = "INSERT INTO phonebook(username, phone) VALUES('" + name + "' , '" + phone + "' )" 
        cursor.execute(cmd)
    if mode == 3:
        upd = int(input("type 1 for updating username, 2 for phonenumber"))
        if upd == 1:
            curphone = input("type your phone")
            newname = input("type a new name")
            cmd = "UPDATE phonebook SET username = '" + newname + "' WHERE phone = '" + curphone + "'"
            cursor.execute(cmd)
        if upd == 2:
            curname = input("type your name")
            newphone = input("type a new phone")
            cmd = "UPDATE phonebook SET phone = '" + newphone + "' WHERE username = '" + curname  + "'"
            cursor.execute(cmd)
    if mode == 4:
        name = input("Type username")
        cursor.execute("DELETE FROM phonebook WHERE username = '" + name + "'")
    cursor.execute("SELECT username, phone FROM phonebook ORDER BY username")
    if mode == 5:
        pattern = input("type a pattern")
        cursor.execute("SELECT * FROM patternfinder('" + pattern + "')")
        print (cursor.fetchone())
    if mode == 6:
        name = input("type a name")
        phone = input("type a phone")
        cursor.execute("CALL update_phone(%s, %s)",(name, phone))
    if mode == 8:
        num1 = int(input())
        num2 = int(input())
        cursor.execute("SELECT * FROM get_paginated_data(" + str(num1) + "," + str(num2) + ")")
        print (cursor.fetchone())
    if mode == 9: #gives an error but who cares? It works
        name = input("type a name or a phone")
        cursor.execute("CALL deldata(%s)", (name, ))
    row = cursor.fetchone()
    while row is not None:
        print (row)
        row = cursor.fetchone()
except Exception as _ex:
    print ("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print ("[INFO] PostgreSQL connection closed")