# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: DeliveryBoard
class DeliveryBoard:
    def __init__(self):
        self.profiles = {}
        self.active_profile = None

    def add_profile(self, username, role='user'):
        self.profiles[username] = {'role': role}
        return self.profiles[username]

    def set_active_profile(self, username):
        if username in self.profiles:
            self.active_profile = username
        return self.active_profile

    def get_active_profile(self):
        return self.active_profile
