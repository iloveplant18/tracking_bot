from Controllers.SprintController import SprintController
from Controllers.StartController import StartController
from Controllers.TrackController import TrackController
from Controllers.UserController import UserController
from Database.Repository.SprintRepository import SprintRepository
from Database.Repository.TrackRepository import TrackRepository
from Database.Repository.UserRepository import UserRepository
from Database.make_request import make_request
from Filters.IsAuthenticated import IsAuthenticated
from bot_init import bot

bot.add_custom_filter(IsAuthenticated())

user_repository = UserRepository(make_request)
track_repository = TrackRepository(make_request)
sprint_repository = SprintRepository(make_request)

start_controller = StartController()
user_controller = UserController(user_repository)
track_controller = TrackController(track_repository, sprint_repository)
sprint_controller = SprintController(sprint_repository)


@bot.message_handler(commands=["start"])
def start(message):
    start_controller.start(message)

@bot.message_handler(commands=["join"])
def join(message):
    user_controller.store(message)

@bot.message_handler(commands=["track"], is_authenticated=True)
def track(message):
    track_controller.store(message)

@bot.message_handler(commands=["sprint"], is_authenticated=True)
def sprint(message):
    sprint_controller.store(message)

@bot.message_handler(commands=["track", "sprint"], is_authenticated=False)
def ask_to_join(message):
    bot.send_message(message.chat.id, "Чтобы отслеживать прогресс залогинься: /join ☝️😇")


if __name__ == "__main__":
    bot.infinity_polling()