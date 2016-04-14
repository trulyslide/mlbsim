import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="mlb",         # your username
                     passwd="mlb",  # your password
                     db="mlb")        # name of the data base


cur = db.cursor()
cur.execute("SELECT * FROM gd_atbat2015 GROUP BY event")
i=1
for row in cur.fetchall():
    event = str(row[14])
   
    print str(i) + ": " + event
    i+=1
db.close()