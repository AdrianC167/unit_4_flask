import pymysql
import pymysql.cursors
from pprint import pprint as print

conn = pymysql.connect(
    database = "world",
    user = "achen",
    password = "232126110",
    host = "10.100.33.60",
    cursorclass = pymysql.cursors.DictCursor

)

cursor = conn.cursor()

cursor.execute("SELECT `Name`,`HeadOfState` FROM `country`")

results = cursor.fetchall()

print(results[0]['HeadOfState'])

for x in results:
    print(x['HeadOfState'])