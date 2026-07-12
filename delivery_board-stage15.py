# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: DeliveryBoard
def weekly_stats(stats, start_date):
    """Расчёт недельной статистики по дням."""
    week = {}
    for date_str, count in stats.items():
        d = datetime.fromisoformat(date_str)
        w_start = (d - timedelta(days=d.weekday())).date()
        key = w_start.isoformat()
        if key not in week:
            week[key] = 0
        week[key] += count
    return week

def compute_stats():
    """Вычисление статистики по дням."""
    stats = {}
    for order in orders:
        d = order["date"]
        stats.setdefault(d, 0)
        stats[d] += 1
    return stats

def print_weekly(stats):
    """Вывод недельной статистики."""
    if not stats:
        return
    dates = sorted(stats.keys())
    current_date = datetime.fromisoformat(dates[0]) - timedelta(days=current_date.weekday())
    while current_date <= max(datetime.fromisoformat(d) for d in stats):
        week_start = current_date.isoformat()
        week_end = (current_date + timedelta(weeks=1)).date().isoformat()
        count = sum(stats.get(d, 0) for d in dates if week_start <= d < week_end)
        print(f"Неделя {week_start} - {week_end}: {count}")
        current_date += timedelta(days=7)

if __name__ == "__main__":
    stats = compute_stats()
    weekly = weekly_stats(stats, datetime.now().date())
    print_weekly(weekly)
