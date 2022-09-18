
class game_object:
    name = "Unnamed"

    components = {}

    def add_component(self, to_add):
        for name in self.components.keys():
            if name == to_add.name:
                print("Component \"" + name + "\" already added.")
                return

        self.components[to_add.name] = to_add

    def __init__(self, name, components_to_add):
        self.name = name

        for component in components_to_add:
            self.add_component(component)