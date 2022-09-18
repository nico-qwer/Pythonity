from operations import *

class rigid_body:
    linear_velocity = (0, 0)
    rotational_velocity = 0
    do_gravity = True

    forces_next_frame = []
    torques_next_frame = []

    gravity = 10.0
    name = "RigidBody"

    def __init__(self, gravity):
        if type(gravity) != bool: raise Exception("type must be bool")
        
        self.do_gravity = gravity

    def update_body(self, object):
        
        from main import delta_time

        # Add gravity to all forces
        if self.gravity == True:
            self.forces_next_frame.append((0, rigid_body.gravity * delta_time))

        # Apply forces
        for force in self.forces_next_frame:
            self.linear_velocity = add_tuples(
                self.linear_velocity[0] + force[0],
                self.linear_velocity[1] + force[1]
            )

        # Apply torques
        for torque in self.torques_next_frame:
            self.rotational_velocity = self.rotational_velocity + torque

        self.forces_next_frame = []
        self.torques_next_frame = []

        # Apply linear velocity
        object.Transform.position = add_tuples(
            object.Transform.position, 
            multiply_tuple(
                self.linear_velocity, 
                delta_time
            )
        )
        
        # Apply rotational velocity
        object.Transform.rotation += self.rotational_velocity * delta_time

    def apply_force(self, amount):
        self.forces_next_frame.append(amount)

    def apply_torque(self, amount):
        self.torques_next_frame.append(amount)

    