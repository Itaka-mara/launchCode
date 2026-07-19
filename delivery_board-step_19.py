# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: DeliveryBoard
def archive_old_records(orders, max_age_days=365):
    """Archive orders older than max_age_days or with status 'delivered'."""
    import datetime
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=max_age_days)
    archived = []
    for order in orders:
        if hasattr(order, 'status') and order.status == 'delivered':
            archived.append(order)
        elif hasattr(order, 'created_at'):
            if order.created_at < cutoff:
                order.status = 'archived'
                archived.append(order)
    return archived
