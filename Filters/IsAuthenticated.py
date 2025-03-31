import telebot

from Database.Repository.UserRepository import UserRepository
from Database.make_request import make_request


class IsAuthenticated(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_authenticated'

    @staticmethod
    def check(message: telebot.types.Message):
        user_repository = UserRepository(make_request)
        return bool(user_repository.get(message.chat.id))
