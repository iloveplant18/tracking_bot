import telebot
import os
from dotenv import load_dotenv

load_dotenv()

_token = os.getenv("BOT_KEY")
bot = telebot.TeleBot(_token)