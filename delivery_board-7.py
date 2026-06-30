# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: DeliveryBoard
def sort_deliveries(deliveries, key='date', reverse=False):
    if not deliveries: return []
    order_map = {'status': 0, 'priority': 1, 'name': 2}
    def get_sort_key(d):
        try:
            val = d[key]
            if isinstance(val, str) and key == 'date':
                from datetime import datetime
                return datetime.strptime(val, '%Y-%m-%d').timestamp()
            elif isinstance(val, int):
                return -val if reverse else val
            elif isinstance(val, str):
                return (0, len(val), val.lower())
        except Exception:
            return 0
    sorted_deliveries = sorted(deliveries, key=get_sort_key)
    if key in order_map and order_map[key] == 1 and reverse:
        priority_order = {3: 'high', 2: 'medium', 1: 'low'}
        def get_priority_val(d): return priority_order.get(d['priority'], 0)
        sorted_deliveries = sorted(sorted_deliveries, key=get_priority_val, reverse=True)
    return sorted_deliveries
