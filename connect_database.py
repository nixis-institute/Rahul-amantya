import mysql.connector
f = open('giving_final_product.csv','r').read().split('\n')

con = mysql.connector.connect(user='root',password="rahul",host="localhost",auth_plugin="mysql_native_password",database="cars")
cur = con.cursor()

for data in f:
    dt = data.split(',')
    print(dt)
    cur.execute('insert into used_cars values ("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8]))    
con.commit()
