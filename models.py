import pymysql

def createTable():
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "rss")
    cur = con.cursor()
    cur.execute("drop table if exists rssfeed;")
    cur.execute("CREATE TABLE rssfeed (title VARCHAR(200), link VARCHAR(200), up_date VARCHAR(200));")
    con.commit()
    con.close()

def insertDetail(title,link,up_date):
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "rss",charset='utf8')
    cur = con.cursor()
    cur.execute("INSERT INTO rssfeed (title,link,up_date) VALUES (%s,%s,%s)", (title,link,up_date))
    con.commit()
    con.close()

def retrieveDetails():
    con = pymysql.connect(host="localhost",user = "root",passwd = "qwertyy", db = "rss",charset='utf8')
    cur = con.cursor()
    cur.execute("SELECT * FROM rssfeed")
    users = cur.fetchall()
    con.close()
    return users

