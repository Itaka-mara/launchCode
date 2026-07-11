# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: DeliveryBoard
def summary_report():
    orders = get_orders()
    couriers = get_couriers()
    routes = get_routes()
    statuses = list(get_status_list())
    
    total_orders = len(orders)
    active_orders = sum(1 for o in orders if o['status'] != 'completed')
    completed_orders = total_orders - active_orders
    
    active_couriers = [c for c in couriers if c.get('active')]
    courier_count = len(active_couriers)
    
    avg_delivery = 0.0
    if routes:
        time_values = [r['time'] for r in routes]
        avg_time = sum(time_values) / len(time_values)
        avg_delivery = f"{avg_time:.1f}"
    
    status_counts = {}
    for s in statuses:
        key = s.get('key', s) if isinstance(s, dict) else s
        count = 0
        for o in orders:
            if o.get('status') == key or (isinstance(o.get('status'), dict) and o['status'].get('key') == key):
                count += 1
        status_counts[key] = count
    
    print(f"DeliveryBoard Summary:")
    print(f"Total orders: {total_orders}")
    print(f"Active orders: {active_orders}")
    print(f"Completed orders: {completed_orders}")
    print(f"Couriers on duty: {courier_count}")
    if avg_delivery:
        print(f"Avg delivery time: {avg_delivery} days")
