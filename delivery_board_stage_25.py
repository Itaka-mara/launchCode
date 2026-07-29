# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: DeliveryBoard
def validate_date(date_str):
    """Проверяет дату в формате YYYY-MM-DD. Возвращает строку или ошибку."""
    try:
        parts = date_str.split('-')
        if len(parts) != 3:
            return "Ошибка: дата должна быть в формате ГГГГ-ММ-ДД."
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        if not (1 <= year <= 9999):
            return "Ошибка: год должен быть от 1 до 9999."
        if not (1 <= month <= 12):
            return f"Ошибка: месяц должен быть от 1 до 12, а не {month}."
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_month[1] = 29
        if not (1 <= day <= days_in_month[month - 1]):
            return f"Ошибка: в {month}-м месяце нет {day} дня."
        return date_str
    except Exception as e:
        return f"Ошибка: не удалось распарсить дату. Попробуйте ещё раз."
