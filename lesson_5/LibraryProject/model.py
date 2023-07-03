from dataclasses import dataclass

from lesson_5.LibraryProject.db import DB


@dataclass
class User(DB):
    id : int = None
    name : str = None
    username : str = None
    password : str = None
    role : str = None
    created_at : str = None



    def check_username(self):
        query = """ select id from users where username = ?  """
        parametr = (self.username,)
        self.cur.execute(query, parametr)
        if self.cur.fetchone():
            return True
    def save_user(self):
        query = """insert into users(name, username, password)
        values(?, ?, ?)"""
        parametrs = (self.name,self.username, self.password)# noqa
        self.cur.execute(query, parametrs)
        self.con.commit()

    def login_check(self):
        query = """ select * from users where username = ? and password = ?  """
        parametr = (self.username,self.password) # noqa
        self.cur.execute(query, parametr)
        # user: list[tuple] = self.cur.fetchall()
        user: tuple = self.cur.fetchone()

        if user:
            obj = User(*user)
            return obj # noqa


@dataclass
class Book(DB):
    id: int = None
    name: str = None
    category_id: int = None
    count : int = None
    created_at: str = None

@dataclass
class BooksUsers(DB):
    id: int = None
    user_id: int = None
    book_id: int = None
    status: int = None
    created_at: str = None
