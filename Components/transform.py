class transform:
    position = (0, 0)
    rotation = 0
    scale = (1, 1)

    name = "Transform"

    def __init__(self, position, rotation, scale):
        self.position = position
        self.rotation = rotation
        self.scale = scale