from Database.make_request import make_request

def run():
    make_request("PRAGMA foreign_keys = ON;")

    make_request("create table user ("
                 "id INTEGER PRIMARY KEY,"
                 "name TEXT"
                 ");")

    make_request("create table sprint ("
                 "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "start_date TEXT,"
                 "end_date TEXT,"
                 "chat_id INTEGER"
                 ");")

    make_request("create table track ("
                 "user_id INTEGER,"
                 "sprint_id INTEGER,"
                 "date TEXT,"
                 "PRIMARY KEY (user_id, sprint_id, date),"
                 "FOREIGN KEY (user_id) REFERENCES user(id) ON UPDATE CASCADE ON DELETE CASCADE,"
                 "FOREIGN KEY (sprint_id) REFERENCES sprint(id) ON UPDATE CASCADE ON DELETE CASCADE"
                 ");")


def rollback():
    make_request("drop table if exists track;")
    make_request("drop table if exists sprint;")
    make_request("drop table if exists user;")