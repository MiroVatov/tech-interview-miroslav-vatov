from mars_rover_task_class import MarsRover
import unittest


class MarsTests(unittest.TestCase):

    def test_if_mars_rover_is_initialized_successfully(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'LMLMLMLMM'])
        self.assertEqual(1, self.mars_rover.rover_details[0][0])  # checking the initial X coordinate
        self.assertEqual(2, self.mars_rover.rover_details[0][1])  # checking the initial Y coordinate
        self.assertEqual(6, self.mars_rover.plateau_width)
        self.assertEqual(6, self.mars_rover.plateau_height)
        self.assertEqual('LMLMLMLMM', self.mars_rover.rover_moves)
        self.assertEqual([1, 2, 'N', 'LMLMLMLMM'], self.mars_rover.rover_details[0])
        expected_result = [[self.mars_rover.rover_moves_to_print[0][0], self.mars_rover.rover_moves_to_print[0][1], self.mars_rover.rover_moves_to_print[0][2]]]
        self.assertEqual(expected_result, self.mars_rover.rover_moves_to_print)  # checking if the final rover positions are correct, as expected

    def test_if_rover_initial_coordinates_are_correct(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'L'])
        expected_result = f"{1} {2}"
        self.assertEqual(expected_result, f"{self.mars_rover.rover_position_x} {self.mars_rover.rover_position_y}")

    def test_property_move_rover(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'LM'])
        expected_result = tuple([-1, 2])
        result = self.mars_rover.move_rover
        self.assertEqual(expected_result, result)

    def test_if_rover_left_direction_rotation_is_correct(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'LML'])
        expected_result = 'S'
        self.assertEqual(expected_result, f"{self.mars_rover.direction}")

    def test_if_rover_right_direction_rotation_is_correct(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'RMR'])
        expected_result = 'S'
        self.assertEqual(expected_result, f"{self.mars_rover.direction}")

    def test_property_return_rover_to_previous_position(self):
        self.mars_rover = MarsRover(5, 5, [1, 2, 'N', 'LM'])
        result = self.mars_rover.return_rover_to_previous_position
        expected_result = tuple([1, 2])
        self.assertEqual(expected_result, result)

    def test_check_if_method__check_rover_valid_coordinates_works_correctly(self):
        self.mars_rover = MarsRover(5, 5, [6, 4, 'N', 'LMLMLMLMM'])
        expected_result = f"The Input Coordinates are out of the Plateau field"
        self.assertEqual(expected_result, "The Input Coordinates are out of the Plateau field")

    def test_if_rover_details_are_missing_from_the_initial_input(self):
        self.mars_rover = MarsRover(5, 5, [3, 3, 'E',])
        expected_result = 'Not all rover movement details are provided'
        self.assertEqual(expected_result, 'Not all rover movement details are provided')


if __name__ == "__main__":
    unittest.main()
