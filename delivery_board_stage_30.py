# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: DeliveryBoard
def add_profile(name, role, email, avatar_url=None):
    profiles = {
        "admin": {"name": "Администратор", "role": "admin", "email": "admin@deliveryboard.local", "avatar_url": None},
        "user": {"name": "Пользователь", "role": "user", "email": "user@deliveryboard.local", "avatar_url": None},
        "courier": {"name": "Курьер", "role": "courier", "email": "courier@deliveryboard.local", "avatar_url": None},
    }
    profiles[name] = {"name": name, "role": role, "email": email, "avatar_url": avatar_url}
    return profiles
