# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: DeliveryBoard
class Tag:
    def __init__(self, name):
        self.name = str(name).strip().lower()
        if not self.name or len(self.name) > 50: raise ValueError("Tag name must be 1-50 chars")

    def __repr__(self): return f"<Tag {self.name!r}>"


class TagManager:
    _tags = {}

    @classmethod
    def get(cls, tag_name):
        return cls._tags.get(tag_name)

    @classmethod
    def add(cls, tag_name):
        t = Tag(tag_name)
        if t.name in cls._tags: raise KeyError(f"Tag {t.name!r} already exists")
        cls._tags[t.name] = t
        return t

    @classmethod
    def remove(cls, tag_name):
        t = cls.get(tag_name)
        if not t: raise KeyError(f"Tag {tag_name!r} does not exist")
        del cls._tags[tag_name]
        return t

    @classmethod
    def list_all(cls):
        return [t for t in cls._tags.values()]
