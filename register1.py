#!C:\Users\Jaswanth\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector


print("content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1><center>Sign Up Successful!!!</center></h1>")
form=cgi.FieldStorage()
fname=form.getvalue("name")
femail=form.getvalue("email")
fpassword=form.getvalue("password")
print("<h1>",fname,femail,fpassword,"</h1>")

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="brandmobiles")
mycursor=mydb.cursor()
sql="INSERT INTO brandmobiles2(name,email,password) VALUES(%s,%s,%s)"
value=(fname,femail,fpassword)
mycursor.execute(sql,value)
mydb.commit()

print("</body>")
print("</html>")