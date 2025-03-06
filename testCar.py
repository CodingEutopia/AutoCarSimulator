import unittest
from unittest.mock import MagicMock
from Car import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.grid = MagicMock()
        self.grid.getXDimension.return_value = 3
        self.grid.getYDimension.return_value = 3
        
        

    def testForwardNorth(self):
        self.car1 = Car("A", 1, 1, "N", ["F"])
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)
        self.assertEqual(self.car1.getY(), 2)
        self.assertEqual(self.car1.getFacingDirection(), "N")

    def testForwardSouth(self):
        self.car1 = Car("A", 1, 1, "S", ["F"])
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)
        self.assertEqual(self.car1.getY(), 0)
        self.assertEqual(self.car1.getFacingDirection(), "S")
    
    def testForwardEast(self):
        self.car1 = Car("A", 1, 1, "E", ["F"])  # Moving East
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 2)  # X increases because moving East
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "E")

    def testForwardWest(self):
        self.car1 = Car("A", 1, 1, "W", ["F"])  # Moving West
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 0)  # X decreases because moving West
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "W")
    
    def testTurnLeftNorth(self):
        self.car1 = Car("A", 1, 1, "N", ["L"])  # Turning Left (West)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "W")

    def testTurnRightNorth(self):
        self.car1 = Car("A", 1, 1, "N", ["R"])  # Turning Right (East)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "E")

    def testTurnLeftSouth(self):
        self.car1 = Car("A", 1, 1, "S", ["L"])  # Turning Left (East)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "E")

    def testTurnRightSouth(self):
        self.car1 = Car("A", 1, 1, "S", ["R"])  # Turning Right (West)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "W")

    def testTurnLeftEast(self):
        self.car1 = Car("A", 1, 1, "E", ["L"])  # Turning Left (North)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "N")

    def testTurnRightEast(self):
        self.car1 = Car("A", 1, 1, "E", ["R"])  # Turning Right (South)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "S")

    def testTurnLeftWest(self):
        self.car1 = Car("A", 1, 1, "W", ["L"])  # Turning Left (South)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "S")

    def testTurnRightWest(self):
        self.car1 = Car("A", 1, 1, "W", ["R"])  # Turning Right (North)
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 1)  # X stays the same
        self.assertEqual(self.car1.getY(), 1)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "N")
    
    def testExceedBoundary(self):
        self.car1 = Car("A", 0, 0, "S", ["F"])
        self.car1.move(self.grid.getXDimension(), self.grid.getYDimension())
        self.assertEqual(self.car1.getX(), 0)  # X stays the same
        self.assertEqual(self.car1.getY(), 0)  # Y stays the same
        self.assertEqual(self.car1.getFacingDirection(), "S")
    


if __name__ == "__main__":
    unittest.main()