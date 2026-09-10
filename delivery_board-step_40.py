# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: DeliveryBoard
import argparse

def main():
    parser = argparse.ArgumentParser(description="DeliveryBoard CLI")
    sub = parser.add_subparsers(dest="command")

    p_order = sub.add_parser("order", help="Create a new order")
    p_order.add_argument("--id", required=True)
    p_order.add_argument("--customer", required=True)
    p_order.add_argument("--items", nargs="+")
    p_order.add_argument("--deadline", type=float, default=None)
    p_order.add_argument("--status", choices=["pending", "in_progress", "delivered", "cancelled"], default="pending")

    p_route = sub.add_parser("route", help="Create a delivery route")
    p_route.add_argument("--id", required=True)
    p_route.add_argument("--orders", nargs="+")
    p_route.add_argument("--driver", required=True)

    p_status = sub.add_parser("status", help="Update order status")
    p_status.add_argument("--id", required=True)
    p_status.add_argument("--status", required=True)

    args = parser.parse_args()

    if args.command == "order":
        print(f"Order {args.id} created for {args.customer}")
    elif args.command == "route":
        print(f"Route {args.id} created with driver {args.driver}")
    elif args.command == "status":
        print(f"Order {args.id} status updated to {args.status}")
    else:
        parser.print_help()
