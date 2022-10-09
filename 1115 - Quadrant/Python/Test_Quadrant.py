from Coordinate import Coordinate
from Quadrant import Quadrant


def test_should_get_quadrant_coordinate():
    # Arrange / Setup
    
   # coordinates = Coordinate(10, 20)
    quadrant = Quadrant(Coordinate(10, 20))
    quadrant2 = Quadrant(Coordinate(-5, 10))
    quadrant3 = Quadrant(Coordinate(-3,-2))
    quadrant4 = Quadrant(Coordinate(2, -5))
    quadrant5 = Quadrant(Coordinate(0, -3))

    # Act / Action
    result = quadrant.get_quadrant_coordinate()
    result2 = quadrant2.get_quadrant_coordinate()
    result3 = quadrant3.get_quadrant_coordinate()
    result4 = quadrant4.get_quadrant_coordinate()
    result5 = quadrant5.get_quadrant_coordinate()

    # Assert
    assert result == "First"
    assert result2 == "Second"
    assert result3 == "Third"
    assert result4 == "Fourth"
    assert result5 == ""
    
