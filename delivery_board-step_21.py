# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: DeliveryBoard
import datetime

def notify_user(recipient, message):
    print(f"[{recipient}] {message}")

def check_reminders():
    today = datetime.date.today()
    reminders = [
        {"name": "Анна", "due_date": "2024-10-15", "task": "Доставить заказ #341"},
        {"name": "Петр", "due_date": "2024-10-20", "task": "Подготовить отчёт по маршруту B"},
    ]
    for r in reminders:
        if today == datetime.date.fromisoformat(r["due_date"]):
            notify_user(r["name"], f"Не забудьте: {r['task']}")

check_reminders()
