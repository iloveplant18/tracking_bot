from bot_init import bot

class StartController:

    def start(self, message):
        bot.send_message(message.chat.id, "Привет👋, вот что я умею: \n"
                                       "/join - начать отслеживать свой прогресс\n"
                                       "/track - отметить участие за сегодня")
