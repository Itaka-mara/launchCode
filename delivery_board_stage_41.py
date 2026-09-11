# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: DeliveryBoard
class DryRunMode:
    """Mode for dry-run operations: logs changes without applying them."""

    def __init__(self, enabled=False):
        self.enabled = enabled
        self.changes = []

    def log(self, operation, details):
        if self.enabled:
            entry = {
                "timestamp": datetime.now().isoformat(),
                "operation": operation,
                "details": details,
            }
            self.changes.append(entry)
            print(f"[DRY-RUN] {operation}: {details}")

    def reset(self):
        self.changes = []
        print("[DRY-RUN] Reset changes log.")

    @property
    def change_count(self):
        return len(self.changes)

    def __enter__(self):
        self.enabled = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.enabled = False
        if exc_type is not None:
            raise exc_val
        return False
