# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: DeliveryBoard
class Template:
    def __init__(self, name, record_type, fields):
        self.name = name
        self.record_type = record_type
        self.fields = fields

    def create_record(self, **kwargs):
        record = {f: kwargs.get(f, self.fields[f].default) for f in self.fields}
        return record
