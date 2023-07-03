import sqlite3

con = sqlite3.connect('test.sqlite')
cur = con.cursor()

query1 = """
create table if not exists city(
    id integer primary key autoincrement,
    city varchar(255) not null,
    last_update timestamp default current_date

);
-- primary key(not null , unique, created index)
"""
query2 = """
create table if not exists country(
    id integer primary key autoincrement,
    country varchar(255) not null,
    last_update timestapm default current_date 
);
"""

cur.execute(query1)
cur.execute(query2)
con.commit()
