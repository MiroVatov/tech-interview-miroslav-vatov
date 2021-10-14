import unittest
from mars_rover_task2_class import MarsRover


class MarsRoverTest2(unittest.TestCase):

    def test__init__(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
        self.assertEqual("N", self.mars_rover.direction)
        self.assertEqual(1, self.mars_rover.x)
        self.assertEqual(2, self.mars_rover.y)

    def test_method_check_print_final_output(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=5, y=2, direction='W')
        expected_result = "3 3 S"
        output = [[3, 3, "S"]]
        self.assertEqual(expected_result, self.mars_rover.print_final_output(output))

    def test_rover_move_method_working_correct(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
        self.mars_rover.rover_move("M")
        expected_result = '1' + ' ' + '3'
        actual_result = f"{self.mars_rover.x} {self.mars_rover.y}"
        self.assertEqual(expected_result, actual_result)

    def test_rover_move_method_not_working_correct(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
        self.mars_rover.rover_move("F")
        expected_result = '1' + ' ' + '2'
        actual_result = f"{self.mars_rover.x} {self.mars_rover.y}"
        self.assertEqual(expected_result, actual_result)

    def test_input_with_invalid_direction(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='G')
        expected_result = "G is wrong! Chosen direction not correct! Please chose from: N, E, W, S"
        actual_result = f"{self.mars_rover.direction} is wrong! Chosen direction not correct! Please chose from: N, E, W, S"
        self.assertEqual(expected_result, actual_result)

    def test_right_rotation_working_correct(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
        expected_result = "W"
        self.mars_rover.left_rotate()
        self.assertEqual(expected_result, self.mars_rover.direction)

    def test_left_rotation_working_correct(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=1, y=2, direction='N')
        expected_result = "E"
        self.mars_rover.right_rotate()
        self.assertEqual(expected_result, self.mars_rover.direction)

    def test_if_method_return_rover_to_previous_position_is_working_correct(self):
        self.mars_rover = MarsRover(plateau_width=5, plateau_height=5, x=0, y=2, direction='W')
        self.mars_rover.rover_move("M")
        self.mars_rover.return_rover_to_previous_position()
        expected_result = '0' + ' ' + '2'
        actual_result = f"{self.mars_rover.x} {self.mars_rover.y}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
