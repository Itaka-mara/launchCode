# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: DeliveryBoard
import time


def check_expired_reminders(board):
    now = time.time()
    expired = [
        r for r in board.get("reminders", [])
        if r["type"] == "delivery" and r["deadline"] is not None
        and now > r["deadline"] and r["status"] != "delivered"
    ]
    return expired
