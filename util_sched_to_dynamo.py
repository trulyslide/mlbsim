import MySQLdb
import boto3


dynamo = boto3.resource('dynamodb')
table = dynamo.Table('mlbsim_schedule')

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="mlb",         # your username
                     passwd="mlb",  # your password
                     db="traunch")        # name of the data base


cur = db.cursor()
cur.execute("SELECT * FROM sched")
i=1
for row in cur.fetchall():
    team =  row[0]
    opp = row[1]
    field = row[2]
    gdate = row[5]

    #format date 
    dynamoDate = int(gdate.strftime('%Y%m%d'))
    dynamoTime = int(gdate.strftime('%H%M'))
    table.put_item(
        Item={
            'gameID': i,
            'gameDate': dynamoDate,
            'team': team,
            'opp': opp,
            'gameTime': dynamoTime
        }
    )
    i+=1
db.close()