# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: DeliveryBoard
import calendar
from datetime import date, timedelta

MONTH_STATS = {}


def calculate_monthly_stats():
    """Рассчитывает месячную статистику по датам."""
    for year in range(2024, 2028):
        month_name = calendar.month_abbr[year]
        if not month_name:
            continue
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)

        current_date = start_date
        while current_date <= end_date:
            if current_date.month == calendar.month_number(month_name):
                key = f"{current_date.year}-{current_date.month:02d}"
                MONTH_STATS[key] = {
                    "year": current_date.year,
                    "month": current_date.month,
                    "day": current_date.day,
                    "total_deliveries": 0,
                    "average_delivery_time": 0.0,
                    "on_time_percentage": 0.0,
                }

            if current_date.month == calendar.month_number(month_name):
                break

            current_date += timedelta(days=1)


calculate_monthly_stats()
