from mysql.connector import connect, Error

def cnx():
    try:
        with connect(
            host="localhost",
            user="root",
            password= SQLpass,
            database="passmanager"
        ) as connection:
            return connection
    except Error as e:
        print(e)
    ####my cnx() function, while it works on it's own, will not transfer connection when used####
    ###I ended up writing out the connection in each function, which I'm upset about when I had a decent function running###

        
def add_account(site, email, username, password, subscription):
    try:
        with connect(
            host="localhost",
            user="root",
            password= SQLpass,
            database="passmanager"
        ) as connection:
            query= """INSERT INTO Accounts (site, email, username, password, subscription) VALUES (%s, %s, %s, %s, %s)"""
            insert_data= (site, email, username, password, subscription)
            with connection.cursor() as cursor:
                cursor.execute(query, insert_data)
                connection.commit()
                print("successfully added....")
    except Error as e:
        print(e)

    ###https://realpython.com/python-mysql/#installing-mysql-server###

def retrieve_pass(site, email):
    try:
        with connect(
            host="localhost",
            user="root",
            password= SQLpass,
            database="passmanager"
        ) as connection:
            query= """SELECT password FROM Accounts WHERE site='""" + site + "'""AND email= '""" + email + "'"
            #https://github.com/KalleHallden/pwManager/blob/master/database_manager.py## 
            #inspiration for a lot of my approach and helped with formatting SQL commands in python, like the one above.#
            with connection.cursor( buffered= True) as cursor:
                cursor.execute(query)
                connection.commit()
                dbpass = cursor.fetchone()
                print("Password is... {}".format(dbpass[0]))
    except Error as e:
        print(e)

def reset_pass(site, email, password, newpass):
    try:
        with connect(
            host="localhost",
            user="root",
            password= SQLpass,
            database="passmanager"
        ) as connection:
            passcheckprompt= """SELECT password FROM Accounts WHERE site='""" + site + "'""AND email= '""" + email + "'"
            accountidcheck= """SELECT idAccounts FROM Accounts WHERE site='""" + site + "'""AND email= '""" + email + "'"
            with connection.cursor( buffered= True) as cursor:
                cursor.execute(passcheckprompt)
                connection.commit()
                passcheck = cursor.fetchone()
                
            if password == passcheck[0]:
                with connection.cursor(buffered= True) as cursor:
                    cursor.execute(accountidcheck)
                    connection.commit()
                    accountid = cursor.fetchone()
                    
                q= """UPDATE Accounts SET password = """ "'" +  newpass + "'" """ WHERE idAccounts=""" +str(accountid[0]) + ""
                    
                with connection.cursor(buffered= True) as cursor:
                    cursor.execute(q)
                    connection.commit()
                print("Password for your {} account with the email {} was successfully changed".format(site,email))
            else:
                print("incorrect information. Please check site, username, and password are correct")
    
    except Error as e:
        print(e)







global SQLpass
SQLpass="Your SQL Pass"
