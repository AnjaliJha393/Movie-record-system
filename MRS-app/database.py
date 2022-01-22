import pymysql
from models import Movie

db = pymysql.connect(host="Localhost", user='anjali',passwd='test', database='project')
# db = pymysql.connect(host="127.0.0.1",user='root',passwd='Mumbai@123',database='project', port=3306, unix_socket='/var/run/mysqld/mysqld.sock')
cursor = db.cursor()

# here we are feaching all data from table and store into list \
# in object form.


def all():
    movielist = []
    query = "select * from movie"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        movie = Movie(row[0], row[1], row[2], row[4], row[3])
        movielist.append(movie)
    return movielist


def delete(mid):
    query = "delete from movie where mid=%s "
    cursor.execute(query, (mid))
    db.commit()
    return True


def get(mid):
    query = "select * from movie where mid=%s"
    cursor.execute(query, (mid))
    row = cursor.fetchone()
    movieobj = Movie(row[0], row[1], row[2], row[4], row[3])
    db.commit()
    return movieobj


def update(mid,mname,mdirector,mboxoffice ,mimg):
    query = "update movie set mname=%s , mdirector=%s , mboxoffice= %s , mimg=%s  where mid=%s"
    cursor.execute(query, (mname,mdirector,mboxoffice ,mimg, mid))
    db.commit()
    return True


def add(mname,mdirector,mboxoffice ,mimg):
    query = "insert into movie (mname,mdirector,mboxoffice,mimg) values (%s,%s,%s,%s)"
    cursor.execute(query, (mname,mdirector,mboxoffice,mimg))
    db.commit()
    return True

