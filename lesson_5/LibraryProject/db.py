import sqlite3

class DB:
    con = sqlite3.connect("library_db.sqlite")
    cur = con.cursor()

    query_table1 = """ 
    create table if not exists users(
    id integer primary key autoincrement,
    name varchar(40),
    username varchar(40) not null unique,
    password varchar(20) not null,
    role varchar(20) not null default "USER", 
    created_at date default current_date 
    )
    """
    query_table2 = """ 
        create table if not exists books(
        id integer primary key autoincrement,
        name varchar(40) not null,
        created_at date default current_date 
        )
        """
    query_table3 = """ 
            create table if not exists books(
            id integer primary key autoincrement,
            name varchar(40) not null,
            category_id integer,
            count integer not null default 1,
            created_at date default current_date 
            )
            """
    query_table4 = """
      create table if not exists books(
            id integer primary key autoincrement,
            user_id integer,
            book_id integer,
            status integer default 1,
            created_at timestap default current_timestamp 
            )
    
    
    """
    cur.execute(query_table1)
    cur.execute(query_table2)
    cur.execute(query_table3)
    cur.execute(query_table4)
    con.commit()