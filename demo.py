import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="",
    database="encuesta"
)
mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM encuesta")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)