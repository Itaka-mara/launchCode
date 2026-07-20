# === Stage 20: Добавь восстановление записей из архива ===
# Project: DeliveryBoard
def restore_from_archive(self, archive_path):
        try:
            with open(archive_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    parts = [p.strip() for p in line.split(';')]
                    if len(parts) >= 6:
                        self.orders.append({
                            'id': parts[0],
                            'customer': parts[1],
                            'address': parts[2],
                            'status': parts[3],
                            'deadline': parts[4],
                            'courier_id': parts[5] if len(parts) > 6 else ''
                        })
            print(f"[Archive] Restored {len([l for l in open(archive_path, 'r').readlines() if not l.strip().startswith('#') and l.strip()])} orders")
        except FileNotFoundError:
            print("[Archive] File not found")
