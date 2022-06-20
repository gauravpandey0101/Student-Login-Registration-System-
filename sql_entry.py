def sql_entry(fname,mname,lname):

    fname=fname
    mname=mname
    lname=lname

    import mysql.connector as msql
   
    ob = msql.connect(
    host = 'localhost',
    user = 'root',
    password = 'rekhagaurav123@',
    database ='rbl'
    )     
    print("\nconnect success")
    ob1=ob.cursor()

    print("\nEnter in DataBase Success\n")
    ob1.execute("create table if not exists ram( name varchar(20),name1 varchar(20),name2 varchar(20))")
    print("TABLE DETAILS\n")    
    ob1.execute("insert into ram values(%s,%s,%s)",(fname,mname,lname))
    ob.commit()
    ob.close()
    print("TABLE DETAILSsssssss")   
