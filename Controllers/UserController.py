from bot_init import bot

class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def store(self, message):
        is_user_exists = self.user_repository.get(message.from_user.id)

        if is_user_exists:
            bot.send_message(message.chat.id, "Ты уже в базе, расслабься ☕️")
            return

        self.user_repository.store(message.from_user.id, message.from_user.first_name)
        bot.send_message(message.chat.id, "+1 сюда")


