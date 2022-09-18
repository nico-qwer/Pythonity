
class circle_collider:
    width = 2
    bounding_box = (-1, 1, -1, 1) # Left, Right, Bottom, Top

    name = "CircleCollider"

    def generate_bounding_box(self, position, new_width):
        self.width = new_width
        
        self.bounding_box[0] = position[0] - (new_width / 2)
        self.bounding_box[1] = position[0] + (new_width / 2)

        self.bounding_box[3] = position[1] - (new_width / 2)
        self.bounding_box[4] = position[1] + (new_width / 2)

class box_collider:
    width = 1
    height = 1
    rotation = 0
    bounding_box = (-1, 1, -1, 1) # Left, Right, Bottom, Top

    name = "BoxCollider"

    def generate_bounding_box(self, position, new_width, new_height, new_rotation):
        self.width = new_width
        self.height = new_height
        self.rotation = new_rotation


        
        

class collision_checks:

    def bounding_box():
        print("he he he haw")
