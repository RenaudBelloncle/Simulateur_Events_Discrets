class Dictionary:
    dictionary = {}

    def __init__(self):
        pass

    def get_components(self, event):
        return self.dictionary[event]

    # Appeler dans main pour définir les liens
    def add_link_component(self, event, component):
        self.dictionary[event] = component
