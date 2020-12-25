import pandas as pd
from cassandra.cluster import Cluster
import csv
cluster = Cluster()
xl = open("NON_CAN_data_28July_03Aug_new.csv","r").read().split("\n") # input file
session = cluster.connect('practice') # Name of database 
for i in xl[:10]:
    data = i.split(",")
    print(data)
    # query = "insert into damdata (p_id, altitude, analog, createdate, devicetype, direction, gpsstutes, ignition, internal, lat, lon, mainpower, modifieddate, odemeter, speed, timeflag, tracktime, unitno, vehicleb) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"    
    # put table in the quary and defind the tables. And it show the output and will sort it automatically. 
    session.execute("insert into dampdata (p_id, altitude, anallog2, analog1, createdate, devicetype, direction, gpsstutes, ignition, internal, lat, lon, mainpower, modifieddate, odemeter, speed, timeflag, tracktime, unitno, vehicleb) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19]))
    