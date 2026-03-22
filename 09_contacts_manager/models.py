import uuid
class Contact:
    def __init__(self, name, number):
        self.id = str(uuid.uuid4())
        self.name = name
        self.number = number

    def to_dict(self):
        return self.__dict__