from apscheduler.schedulers.background import BackgroundScheduler
import datetime

from bot_init import bot


class ScheduleManager:
    def __init__(self, sprint_repository, user_repository):
        self.sprint_repository = sprint_repository
        self.user_repository = user_repository
        self.scheduler = BackgroundScheduler()

    def kill_old_sprints(self):
        sprints = self.sprint_repository.get_all()
        if not sprints:
            return
        current_date = datetime.date.today()
        for i in sprints:
            if i[2] == current_date:
                self.kill_sprint(i[0], i[3])

    def kill_sprint(self, sprint_id, chat_id):
        users_and_tracks_count = self.user_repository.get_names_and_tracks_in_sprint(sprint_id)
        message = "ЙОУ ПАРНИ спринт закончился!\n\n"
        for i in users_and_tracks_count:
            message += f"{i[0]}: {i[1]}"
        message += "Красавцы аще 🤌"
        bot.send_message(chat_id, message)
        bot.send_sticker(chat_id, "CAACAgIAAxkBAAENfsZn1cx3Sq-1Z3YNWgAB9OsiE6j9HpgAAk4YAALmGrhLO3XgRUFJdn42BA")
        # TODO Пользователи должны создавать спринты, не более спринта на чат
