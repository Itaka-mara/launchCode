# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: DeliveryBoard
import sys

try:
    import colorama
    colorama.init()
except ImportError:
    pass

ANSI_ENABLED = True

def enable_ansi():
    global ANSI_ENABLED
    ANSI_ENABLED = True
    if 'colorama' in globals():
        colorama.init()

def disable_ansi():
    global ANSI_ENABLED
    ANSI_ENABLED = False

def color(text, color, bold=False):
    if not ANSI_ENABLED:
        return text
    codes = []
    if bold:
        codes.append("1")
    codes.append(color)
    return f"\033[{','.join(codes)}m{text}\033[0m"

class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"

def print_delivery_board():
    print(color("╔══════════════════════════════════════════════════════╗", Colors.CYAN, bold=True))
    print(color("║         📦  DeliveryBoard  —  Доска доставок       ║", Colors.CYAN, bold=True))
    print(color("╚══════════════════════════════════════════════════════╝", Colors.CYAN, bold=True))
    print()
    print(color(f"  Статус ANSI: {'ВКЛЮЧЕН' if ANSI_ENABLED else 'ВЫКЛЮЧЕН'} | Курьеров: 3 | Заказов: 6", Colors.WHITE))
    print()
    print(color(f"  {color('🟢', Colors.GREEN)}  Курьер: Алексей — {color('Доставляет', Colors.YELLOW)} {color('📦 Заказ #101 (Пицца)', Colors.RED)} {color('→', Colors.WHITE)} {color('🏠 Дом клиента', Colors.GREEN)}", Colors.WHITE))
    print(color(f"  {color('🟡', Colors.YELLOW)}  Курьер: Мария  — {color('Доставляет', Colors.YELLOW)} {color('📦 Заказ #102 (Суши)', Colors.RED)} {color('→', Colors.WHITE)} {color('🏠 Дом клиента', Colors.GREEN)}", Colors.WHITE))
    print(color(f"  {color('🔵', Colors.BLUE)}  Курьер: Иван   — {color('Доставляет', Colors.YELLOW)} {color('📦 Заказ #103 (Бургер)', Colors.RED)} {color('→', Colors.WHITE)} {color('🏠 Дом клиента', Colors.GREEN)}", Colors.WHITE))
    print()
    print(color(f"  {color('📊 Статистика:', Colors.BOLD)} {color('✅', Colors.GREEN)} 5 доставлено, {color('⏳', Colors.YELLOW)} 1 в пути", Colors.WHITE))
    print()
    print(color("  Нажмите Ctrl+C, чтобы завершить", Colors.MAGENTA))
