class Robot:
    def __init__(self, initial_x_position, initial_y_position, initial_x_velocity, initial_y_velocity, x_acceleration, y_acceleration):
        self.x = initial_x_position
        self.y = initial_y_position
        self.velocity_x = initial_x_velocity
        self.velocity_y = initial_y_velocity
        self.acceleration_x = x_acceleration
        self.acceleration_y = y_acceleration
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
    def accelerate(self):
        self.x += self.velocity_x
        self.y += self.velocity_y 
        self.velocity_x += self.acceleration_x
        self.velocity_y += self.acceleration_y
        self.x += 0.5 * self.acceleration_x
        self.y += 0.5 * self.acceleration_y 

robot1 = Robot(0, 0, 1, 0, 1, 1) 

print(robot1.acceleration_x, robot1.acceleration_y)
robot1.accelerate()
print(robot1.x, robot1.y)