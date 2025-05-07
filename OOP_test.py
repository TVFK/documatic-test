class Animal:
    """Base class representing an animal."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self) -> str:
        """Return the sound the animal makes."""
        return "Some generic sound"

    def __str__(self) -> str:
        return f"{self.name} ({self.age} years old)"

    def __repr__(self) -> str:
        return f"Animal(name='{self.name}', age={self.age})"

class Dog(Animal):
    """Class representing a dog, inherits from Animal."""

    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """Return the sound a dog makes."""
        return "Woof!"

    def fetch(self, item: str) -> str:
        """Simulate fetching an item."""
        return f"{self.name} fetches the {item}!"

    def __str__(self) -> str:
        return f"{super().__str__()} (Breed: {self.breed})"

class Cat(Animal):
    """Class representing a cat, inherits from Animal."""

    def make_sound(self) -> str:
        """Return the sound a cat makes."""
        return "Meow!"

    def purr(self) -> str:
        """Simulate a cat purring."""
        return f"{self.name} purrs softly."

# Дружественная функция
def describe_animal(animal: Animal) -> str:
    """Return a description of the animal (friend function)."""
    return f"This is {animal.name}, it says: '{animal.make_sound()}'"

class Vector:
    """Class representing a 2D vector."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector') -> 'Vector':
        """Overload the + operator."""
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        """Overload the == operator."""
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

# ========== НОВЫЕ КЛАССЫ И МЕТОДЫ ========== #
class Bird(Animal):
    """Class representing a bird, inherits from Animal."""

    def __init__(self, name: str, age: int, wingspan: float):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self) -> str:
        """Return the sound a bird makes."""
        return "Chirp!"

    def fly(self) -> str:
        """Simulate flying."""
        return f"{self.name} is flying with a wingspan of {self.wingspan} meters."

class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
