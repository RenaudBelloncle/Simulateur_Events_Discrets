class Event:
    name = None
    data = None

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def get_name(self):
        return self.name

    def get_data(self):
        return self.data

    def set_data(self, n):
        self.name = n
