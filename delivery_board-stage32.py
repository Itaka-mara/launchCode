# === Stage 32: Добавь журнал действий пользователя ===
# Project: DeliveryBoard
class ActionLog:
    def __init__(self):
        self.entries = []
        self._counter = 0

    def log(self, action, user, detail=""):
        self._counter += 1
        self.entries.append({"id": self._counter, "action": action, "user": user, "detail": detail, "timestamp": datetime.now()})

    def get_recent(self, limit=10):
        return self.entries[-limit:]

    def clear(self):
        self.entries.clear()
        self._counter = 0

    def __len__(self):
        return len(self.entries)
