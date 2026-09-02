# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: DeliveryBoard
def next_action_suggestion(current_state: dict) -> str:
    """
    Recommends the next action based on the current state of the delivery board.
    
    Args:
        current_state (dict): Contains keys like 'orders', 'routes', 'couriers', 'statuses'.
            Each value is a list of dicts with relevant attributes.
    
    Returns:
        str: A suggestion string for the next action.
    """
    if 'orders' not in current_state:
        return "No orders data available. Please provide order information."
    
    orders = current_state.get('orders', [])
    if not orders:
        return "No orders to process. Add orders to the delivery board."
    
    orders_needing_action = []
    for order in orders:
        status = order.get('status', 'pending')
        deadline = order.get('deadline', None)
        
        if status == 'pending':
            orders_needing_action.append("Pending orders: {}".format(len([o for o in orders if o.get('status') == 'pending'])))
        elif status == 'in_progress' and deadline:
            now = datetime.datetime.now()
            deadline_dt = datetime.datetime.fromisoformat(deadline)
            if now > deadline_dt:
                orders_needing_action.append("Overdue orders: {}".format(order.get('id', 'unknown')))
    
    if orders_needing_action:
        return "Action needed: " + "; ".join(orders_needing_action)
    
    if 'couriers' in current_state and not current_state['couriers']:
        return "No couriers available. Add couriers to handle orders."
    
    return "All orders are in good standing. Consider updating order statuses or adding new orders."
