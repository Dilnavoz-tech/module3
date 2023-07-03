from dataclasses import dataclass

from db import DB


@dataclass
class User(DB):
    id: int = None
    name: str = None
    username: str = None
    password: str = None
    role: str = None
    created_at: str = None

    def check_username(self):
        query = """select id from users where username = ?"""
        parametr = (self.username,)
        self.cur.execute(query, parametr)
        if self.cur.fetchone():
            return True

    def save_user(self): # noqa
        query = """insert into users(name , username , password)
        values (? , ? , ?)"""
        parametrs = (self.name , self.username , self.password) # noqa
        self.cur.execute(query, parametrs)
        self.con.commit()

    def login_check(self):
        query = """select * from users where username = ? and password = ?"""
        parametr = (self.username, self.password)
        self.cur.execute(query, parametr)
        # user: list[tuple] = self.cur.fetchall()
        user: tuple = self.cur.fetchone()
        if user:
            obj = User(*user)
            return obj

    def change_info(self, col_name, val):
        query = f"""
            update users set {col_name} = ? where id = ?
        """
        params = (val, self.id)
        self.cur.execute(query, params)
        self.con.commit()

    def add_new_admin(self, new_admin):
        query = """update users set role = ?  where username = ?"""
        param = ("ADMIN", new_admin)

        self.cur.execute(query, param)
        self.con.commit()

    def delete_account(self , name):
        query ="""delete from users where username = ?"""
        param = (name,)
        self.cur.execute(query, param)
        self.con.commit()

    def change_name(self, name):
        query_new = """update users set name = ? where username = ?"""
        param = (name, self.username)
        self.cur.execute(query_new, param)
        self.con.commit()

    def change_username(self, username):
        query = """select * from users where username = ?"""
        param = (username,)
        self.cur.execute(query, param)
        self.con.commit()
        if not self.cur.fetchone():
            query_new = """update users set username = ? where password = ?"""
            paramert = (username, self.password)
            self.cur.execute(query_new, paramert)
        else:
            print('The username you entered has already been taken!!')


    def change_password(self, password):
         query_new = """update users set password = ? where username = ?"""
         param = (password, self.username)
         self.cur.execute(query_new, param)
         self.con.commit()

    def delate_self_account(self):
        query = """delete from users where username = ?"""
        param = (self.username,)
        self.cur.execute(query, param)
        self.con.commit()









@dataclass
class Book(DB):
    id: int = None
    name: str = None
    category_id: int = None
    count: int = None
    created_at: str = None



    def save_book(self):  # noqa
        query = """insert into books(name , category_id , count)
                values (? , ? , ?)"""
        parametrs = (self.name, self.category_id, self.count)  # noqa
        self.cur.execute(query, parametrs)
        self.con.commit()

    def update_book(self, update_item, data_type):
        query = f"""update books set {data_type} = ? where id = ?"""
        param = (update_item, self)
        self.cur.execute(query, param)
        self.con.commit()

    def delete_book(self, name):
        query = """delete from books where name = ?"""
        param = (name,)
        self.cur.execute(query, param)
        self.con.commit()

    def select_books(self):
        query = """select * from books"""
        self.cur.execute(query)
        self.con.commit()
        return self.cur.fetchall()

    def search_book(self, item):
        query = """select * from books where name = ?"""
        param = (item,)

        self.cur.execute(query, param)
        self.con.commit()
        return  self.cur.fetchall() # noqa

@dataclass
class Category(DB):
    id: int = None
    name: str = None
    created_at: str = None


@dataclass
class BooksUsers(DB):
    id: int = None
    user_id: int = None
    book_id: int = None
    status: int = None
    created_at: str = None
