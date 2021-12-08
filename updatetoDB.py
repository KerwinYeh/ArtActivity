import mysql.connector
from crawlArtData import crawlFun


def uploadDB(df):

    artDB = mysql.connector.connect(host = "localhost", user = "root", password = "chou0212", database = "Art", auth_plugin='mysql_native_password')
    mycursor = artDB.cursor()

    importsql = "INSERT INTO ArtData (UID, Category, EditModifyDate, StartDate, EndDate, HitRate, Time, LocationName, OnSale, Latitude, Longitude, EndTime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = []
    for i in range(len(df)):
        val.append(tuple(df.iloc[i]))

    mycursor.executemany(importsql, val)
    artDB.commit() 


uploadDB(crawlFun(url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all"))