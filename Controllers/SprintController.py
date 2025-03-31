import datetime

from bot_init import bot


class SprintController:
    def __init__(self, sprint_repository):
        self.sprint_repository = sprint_repository

    def store(self, message):
        # проверить есть ли незаконченный спринт в чате
        sprint = self.sprint_repository.get_last_sprint_in_chat(message.chat.id)
        current_date = datetime.date.today()
        if (sprint and sprint[2] > current_date):
        # если есть - сообщить об ошибке
            bot.send_message(message.chat.id, "в этом чате уже есть спринт, подождите пока закончится че вы 🫵😂")
            return
        # если нет - создать спринт и сообщить о создании
        end_date = current_date + datetime.timedelta(weeks=2)
        self.sprint_repository.store(current_date, end_date, message.chat.id)
        bot.send_message(message.chat.id, f"Спринт создан, побежали парни ✌️😔🫦.\nНачало: {current_date}\nКонец: {end_date}")

