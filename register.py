#!C:\Users\Jaswanth\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector


print("content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1><center>Login Successful!!!</center></h1>")
form=cgi.FieldStorage()
fname=form.getvalue("name")
femail=form.getvalue("email")
fpassword=form.getvalue("password")
fdob=form.getvalue("dob")
fcity=form.getvalue("city")
fmodel=form.getvalue("model")
print("<h1>",fname,femail,fpassword,fdob,fcity,fmodel,"</h1>")

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="brandmobiles")
mycursor=mydb.cursor()
sql="INSERT INTO brandmobiles1(name,email,password,dob,city,model) VALUES(%s,%s,%s,%s,%s,%s)"
value=(fname,femail,fpassword,fdob,fcity,fmodel)
mycursor.execute(sql,value)
mydb.commit()

print("</body>")
print("</html>")