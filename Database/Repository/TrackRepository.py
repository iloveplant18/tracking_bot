from Database.Repository.Repository import Repository


class TrackRepository(Repository):
    def store(self, user_id, sprint_id, date):
        self.make_request(f"insert into track (user_id, sprint_id, date) values ({user_id}, {sprint_id}, \"{date}\")")

    def get_user_tracks_at_sprint(self, user_id, sprint_id):
        return self.make_request(f"select count(*) from track where user_id={user_id} and sprint_id={sprint_id}")[0][0]

    def get_track(self, user_id, sprint_id, date):
        return self.make_request(f"select * from track where user_id={user_id} and sprint_id={sprint_id} and date=\"{date}\"")