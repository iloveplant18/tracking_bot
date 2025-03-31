from datetime import date
from bot_init import bot

class TrackController:
    def __init__(self, track_repository, sprint_repository):
        self.track_repository = track_repository
        self.sprint_repository = sprint_repository

    def store(self, message):
        user_id = message.from_user.id
        current_date = date.today()
        sprint_id = self.sprint_repository.get_last_sprint_id()

        is_track_exists = self.track_repository.get_track(user_id, sprint_id, current_date)
        if is_track_exists:
            bot.send_message(message.chat.id, "Сорян, отмечаться можно только раз в день 🔫🤠`")
            return

        result = self.track_repository.store(user_id, sprint_id, current_date)
        tracks_count = self.track_repository.get_user_tracks_at_sprint(user_id, sprint_id)
        reply_message = self._create_reply_from_tracks_count(tracks_count)
        bot.send_message(message.chat.id, reply_message)

    def _create_reply_from_tracks_count(self, tracks_count):
        message = ''
        for i in range(tracks_count):
            message += '🌟'
        message += '\n'
        if tracks_count > 3:
            message += f"Неплох, уже {tracks_count} отметки в этом спринте"
        elif tracks_count > 6:
            message += f"Харош брат, уже {tracks_count} дней ебашишь!"
        elif tracks_count > 10:
            message += f"Пиздец че за монстр, {tracks_count} подряд, ахуй"
        else:
            message += f"Отличное начало"
        return message
