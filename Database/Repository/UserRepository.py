from Database.Repository.Repository import Repository


class UserRepository(Repository):

    def store(self, userId, userName):
        request = f"insert into user (id, name) values (\"{userId}\", \"{userName}\")"
        self.make_request(request)

    def get(self, userId):
        request = f"select * from user where id={userId}"
        result = self.make_request(request)
        return result

    def get_names_and_tracks_in_sprint(self, sprint_id):
        request = ("select name, count(*) "
                   "from sprint join track "
                   "on sprint.id = track.sprint_id "
                   "join users "
                   "on users.id = track.user_id "
                   f"where sprint.id = {sprint_id} "
                   f"group by name")
        return self.make_request(request)
