# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: DeliveryBoard
def main_menu():
    while True:
        print("\n=== DeliveryBoard Menu ===")
        print("1. View Orders")
        print("2. Add Order")
        print("3. Assign Courier")
        print("4. Update Status")
        print("5. Show Routes")
        print("6. Exit")
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            for order in orders:
                print(f"\nOrder #{order['id']}: {order['customer']} -> {order['address']} | Status: {order['status']}")
        elif choice == "2":
            cid = input("Customer ID: ")
            addr = input("Delivery Address: ")
            orders.append({"id": len(orders)+1, "customer": cid, "address": addr, "status": "pending", "deadline": None})
            print(f"Order #{len(orders)} created.")
        elif choice == "3":
            oid = input("Order ID: ")
            courier_id = input("Courier ID: ")
            for order in orders:
                if str(order['id']) == oid and order['status'] != 'delivered':
                    order['courier'] = courier_id
                    print(f"Courier {courier_id} assigned to Order #{oid}.")
                    break
        elif choice == "4":
            oid = input("Order ID: ")
            new_status = input("New Status (pending, in_transit, delivered): ")
            for order in orders:
                if str(order['id']) == oid:
                    order['status'] = new_status
                    print(f"Status updated to {new_status}.")
                    break
        elif choice == "5":
            active_orders = [o for o in orders if o['status'] != 'delivered' and o.get('courier')]
            if not active_orders:
                print("No active routes.")
            else:
                for order in active_orders:
                    print(f"Route #{order['id']}: {order['customer']} -> {order['address']} (Courier: {order['courier']})")
        elif choice == "6":
            print("Exiting...")
            break
