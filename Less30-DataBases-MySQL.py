import pymysql

mySQLserver = "172.17.20.191\vb-ub22"
myDatabase = "sakila"
username = "ivankurop"
password = "Test123!"

con = pymysql.connect('Driver={SQL Server};'#for connection to SQL server
                              'Server =' + mySQLserver + ';'
                              'Database =' + myDatabase + ';'
                              'uid =' + username + ';'
                              'password =' + password
                              )

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM actors")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))