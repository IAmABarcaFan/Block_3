import math

class Vector:
    def __init__(self, vector_x, vector_y):
        self.x = vector_x
        self.y = vector_y
        self.vector = [vector_x, vector_y]
    def vector_length(self):
        return math.sqrt(sum(x ** 2 for x in self.vector))
    def vector_addition(self, vector1 , vector2):  # This works ... 
        return [x + y for x, y in zip(vector1, vector2)]
    def dot_product(self, vector1, vector2):
        return sum(x * y for x, y in zip(vector1, vector2))
    def vector_length_else(self, other_vector):  # But this could work as well.
        x_component = self.x + other_vector.x
        y_component = self.y + other_vector.y
        return Vector(x_component, y_component)

def test_vectors():
    vector1 = Vector(3, 4)
    vector2 = Vector(1, 2)
    assert(vector1.vector_length() == 5)
    assert(vector2.vector_length() == math.sqrt(5))
    assert(vector1.vector_addition(vector1.vector, vector2.vector) == [4, 6])
    assert(vector1.dot_product(vector1.vector, vector2.vector) == 11)

def main():
    test_vectors()

if __name__ == "__main__":
    main()