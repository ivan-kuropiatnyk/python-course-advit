import pypyodbc

mySQLserver = "172.17.20.191\vb-ub22"
myDatabase = "sakila"
username = "ivankurop"
password = "Test123!"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server =' + mySQLserver + ';'
                              'Database =' + myDatabase + ';'
                              'uid =' + username + ';'
                              'password =' + password + ';'
                              )

cursor = connection.cursor()
mySQLquery = ("""
            SELECT actor_id, first_name, last_name
            FROM actor
            WHERE first_name = 'MARY'
            """)

cursor.execute(mySQLquery)
results = cursor.fetchall()

for raw in results:
    actorid = raw[0]
    firstname = raw[1]
    lastname = raw[2]

    print("Welcome:" + str(firstname) + " " + str(lastname))

connection.close()