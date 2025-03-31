from Database.Repository.Repository import Repository
from Database.make_request import make_request


class SprintRepository(Repository):

    def get_last_sprint_id(self):
        result =  make_request("select max(id) from sprint;")
        if not result: return None
        return result[0][0]

    def get_all(self):
        return make_request("select * from sprint;")

    def get_last_sprint_in_chat(self, chat_id):
        result = make_request(f"select * from sprint where chat_id = {chat_id} and end_date = (select max(end_date) from sprint);")
        if not result: return None
        return result[0]

    def store(self, start_date, end_date, chat_id):
        make_request(f"insert into sprint (start_date, end_date, chat_id) values (\"{start_date}\", \"{end_date}\", {chat_id})")
