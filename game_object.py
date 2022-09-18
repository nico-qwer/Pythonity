# Other files
from Components import transform

class game_object:
    components = {
        transform.name : transform()
    }

    def add_component(to_add, self):
        self.components[to_add.name] = to_add